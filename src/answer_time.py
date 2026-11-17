"""Answer time of the answer model (O1, R-12) on this computer: CPU only, or with the GPU for comparison.

Repeats "Answer time on one team computer" of docs/spikes/model-selection-spike.md on the 30 val questions
(O1: median answer time on the val questions at most 60 s), with the prompt and settings of the answer model (D9):
prompts/answer.yaml, filled as the RAG service does it (rag/app/prompt.py, KAN-122), and the model and options of
rag/app/config.py (llama3.1:8b-instruct-q4_K_M, temperature 0, at most 300 tokens, context window 4,096). Each question gets
the 8 chunks the search retrieved for it in the Sprint 2 baseline (docs/eval/answers/val-with-retrieval-chunks.jsonl),
so the retriever (bge-m3) is not needed; only the LLM time is measured.

Before measuring, the script asks Ollama where the model is loaded (/api/ps). With --device cpu it stops if any
part of the model is in GPU memory (size_vram > 0), so a CPU result cannot use the GPU without anyone noticing.

Run from the repository root (needs pyyaml from requirements.txt and a running Ollama), see docs/eval/answer-time.md:
    python src/answer_time.py                                        # Ollama app on the Mac, CPU only (num_gpu 0)
    python src/answer_time.py --url http://localhost:11435 --label docker   # the ollama container of docker-compose.yml
    python src/answer_time.py --device gpu                           # Ollama app with the GPU (Metal), for comparison
"""
import argparse, csv, datetime, json, os, platform, re, statistics, subprocess, sys, time
import urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
try:
    import yaml
except ImportError:
    raise SystemExit("pyyaml is missing. Install the packages of requirements.txt (pip install pyyaml==6.0.3 is enough here).")

# The answer model and its options (D9), the same values as rag/app/config.py.
GENERATION = {"model": "llama3.1:8b-instruct-q4_K_M", "temperature": 0, "num_predict": 300, "num_ctx": 4096}
PROMPT = yaml.safe_load((ROOT / "prompts" / "answer.yaml").read_text(encoding="utf-8"))


def build_messages(question, history, chunks):
    """The messages of the answer prompt, built as in rag/app/prompt.py (mode "rag")."""
    previous = PROMPT["previous_question"].format(previous_question=history[-1]["question"]) if history else ""
    provisions = "\n\n".join(f"[{c['ref']}] {c['text']}" for c in chunks)
    return [{"role": "system", "content": PROMPT["system"]},
            {"role": "user", "content": PROMPT["example_user"]},
            {"role": "assistant", "content": PROMPT["example_answer"]},
            {"role": "user", "content": PROMPT["user"].format(provisions=provisions, previous=previous, question=question)}]

OUT = ROOT / "docs" / "eval" / "answer-time"


def call(url, path, body=None, timeout=1800):
    req = urllib.request.Request(url + path, data=None if body is None else json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404 and path == "/api/show":
            return None
        raise SystemExit(f"Ollama error on {path}: {e.code} {e.read().decode()[:500]}")
    except urllib.error.URLError as e:
        raise SystemExit(f"Ollama is not reachable at {url} ({e.reason}). Start the Ollama app, or the container (docs/eval/answer-time.md).")


def sh(cmd):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        return ""


def machine_info():
    """The computer, without its name, user name or paths."""
    info = {"os": platform.platform(terse=True), "python": platform.python_version()}
    if sys.platform == "darwin":
        info["cpu"] = sh("sysctl -n machdep.cpu.brand_string")
        info["performance_cores"] = sh("sysctl -n hw.perflevel0.physicalcpu")
        info["efficiency_cores"] = sh("sysctl -n hw.perflevel1.physicalcpu")
        mem = sh("sysctl -n hw.memsize")
        info["ram_gb"] = round(int(mem) / 2 ** 30) if mem.isdigit() else None
        info["on_battery"] = "Battery Power" in sh("pmset -g batt")
    docker = sh("docker info --format '{{.NCPU}} {{.MemTotal}}'").split()
    if len(docker) == 2 and docker[0].isdigit() and int(docker[0]) > 0 and docker[1].isdigit():
        info["docker_vm_cpus"], info["docker_vm_ram_gb"] = int(docker[0]), round(int(docker[1]) / 2 ** 30)
    return info


def ps_entry(url, model):
    """The raw /api/ps entry of the model (with size and size_vram), or None if it is not loaded."""
    for m in call(url, "/api/ps").get("models", []):
        if model in (m.get("name"), m.get("model")):
            return m
    return None


def placement(url, model):
    """(size, size_vram) of the loaded model from /api/ps, or None if it is not loaded."""
    m = ps_entry(url, model)
    return None if m is None else (m.get("size", 0), m.get("size_vram", 0))


OLLAMA_LOG = Path.home() / ".ollama" / "logs" / "server.log"     # the log of the Ollama app on macOS


def log_size():
    try:
        return OLLAMA_LOG.stat().st_size
    except OSError:
        return None


def offload_lines(start):
    """Lines of the Ollama app's log written since byte `start` that say how many layers went to the GPU."""
    if start is None:
        return []
    with open(OLLAMA_LOG, "rb") as f:
        f.seek(start)
        text = f.read().decode("utf-8", "replace")
    keys = ("offload", "layers to GPU", "layers.offload", "inference compute", "using device")
    return [line.strip() for line in text.splitlines() if any(k in line for k in keys)]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--device", choices=["cpu", "gpu"], default="cpu",
                   help="cpu: num_gpu 0, and stop if the model is in GPU memory (default); gpu: Ollama's default")
    p.add_argument("--url", default="http://localhost:11434", help="Ollama (default: the Ollama app on this computer)")
    p.add_argument("--label", help="name of the results folder after the date (default: the device)")
    p.add_argument("--model", default=GENERATION["model"], help=f"Ollama model (default: {GENERATION['model']})")
    p.add_argument("--ids", nargs="*", help="only these val question IDs")
    p.add_argument("--cold", action="store_true",
                   help="reload the model before every question, so no part of the prompt comes from Ollama's cache (stricter, slower)")
    a = p.parse_args()

    chunks = {c["chunk_id"]: c for c in map(json.loads, open(ROOT / "data" / "chunks.jsonl", encoding="utf-8"))}
    val = list(csv.DictReader(open(ROOT / "docs" / "eval" / "eval-set-v1-val.csv", encoding="utf-8-sig")))
    by_id = {q["id"]: q for q in val}
    baseline = {r["id"]: r for r in map(json.loads, open(ROOT / "docs" / "eval" / "answers" / "val-with-retrieval-chunks.jsonl", encoding="utf-8"))}
    ids = a.ids or [q["id"] for q in val]
    unknown = [i for i in ids if i not in by_id]
    if unknown:
        raise SystemExit(f"Not val question IDs: {', '.join(unknown)}")

    model = a.model
    options = {k: GENERATION[k] for k in ("temperature", "num_predict", "num_ctx")}
    if a.device == "cpu":
        options["num_gpu"] = 0

    version = call(a.url, "/api/version").get("version", "?")
    if call(a.url, "/api/show", {"model": model}) is None:
        raise SystemExit(f"{model} is not in this Ollama. Download it once: ollama pull {model}"
                         " (container: docker exec eliza-ollama-time ollama pull ...)")
    info = machine_info()
    print(f"Ollama {version} at {a.url} | {model} | device {a.device} | options {options}")
    if info.get("on_battery"):
        print("WARNING: the Mac is on battery; plug it in for a fair measurement.")

    def unload():
        call(a.url, "/api/generate", {"model": model, "keep_alive": 0})
        for _ in range(30):
            if placement(a.url, model) is None:
                return
            time.sleep(1)

    def load():
        return call(a.url, "/api/generate", {"model": model, "prompt": "", "options": options, "keep_alive": "30m"}).get("load_duration", 0) / 1e9

    snapshots = []                                 # raw /api/ps answers: the evidence of where the model was

    def where(when):
        m = ps_entry(a.url, model)
        if m is None:
            raise SystemExit(f"The model is not loaded ({when}).")
        snapshots.append({"when": when, "time": datetime.datetime.now().isoformat(timespec="seconds"),
                          "api_ps": {k: m.get(k) for k in ("name", "size", "size_vram", "context_length", "details") if k in m}})
        size, vram = m.get("size", 0), m.get("size_vram", 0)
        label = "100% CPU" if vram == 0 else f"{100 * vram / size:.0f}% GPU" if size else "GPU"
        if a.device == "cpu" and vram > 0:
            raise SystemExit(f"STOP: the model is placed {label} ({when}), so this is not a CPU-only run.")
        return label

    unload()                                       # start without the model in memory
    local = a.url.rstrip("/") in ("http://localhost:11434", "http://127.0.0.1:11434")
    log_start = log_size() if local else None      # only the Ollama app on this computer writes this log
    load_s = load()
    where_loaded = where("after loading")
    print(f"Model loaded in {load_s:.1f} s, placement: {where_loaded}")

    rows = []
    for n, qid in enumerate(ids, 1):
        q = by_id[qid]
        m = re.match(r"follows (\S+)", q["context"].strip())
        history = [{"question": by_id[m[1]]["question"]}] if m else []
        retrieved = [chunks[c["chunk_id"]] for c in baseline[qid]["chunks"]]
        messages = build_messages(q["question"], history, retrieved)
        if a.cold and n > 1:
            unload()
            load()
        start = time.time()
        r = call(a.url, "/api/chat", {"model": model, "stream": False, "messages": messages, "options": options, "keep_alive": "30m"})
        wall = time.time() - start
        load_q = r.get("load_duration", 0) / 1e9
        pe_n, pe_s = r.get("prompt_eval_count", 0), r.get("prompt_eval_duration", 0) / 1e9
        ev_n, ev_s = r.get("eval_count", 0), r.get("eval_duration", 0) / 1e9
        rows.append({"id": qid, "answer_time_s": round(wall - load_q, 1), "load_s": round(load_q, 1),
                     "prompt_tokens_read": pe_n, "reading_tok_s": round(pe_n / pe_s, 1) if pe_s else "",
                     "answer_tokens": ev_n, "writing_tok_s": round(ev_n / ev_s, 1) if ev_s else "",
                     "hit_token_limit": ev_n >= options["num_predict"], "answer": r["message"]["content"].strip()})
        x = rows[-1]
        print(f"{n:2}/{len(ids)} {qid:<5} {x['answer_time_s']:6.1f} s  (read {pe_n} tok at {x['reading_tok_s']} tok/s, wrote {ev_n} tok at {x['writing_tok_s']} tok/s)")
        if n == len(ids) // 2:
            where("in the middle of the run")
    where_end = where("at the end of the run")
    log = offload_lines(log_start)

    times = sorted(x["answer_time_s"] for x in rows)
    med = statistics.median(times)
    summary = {"date": datetime.datetime.now().isoformat(timespec="minutes"), "device": a.device, "placement": where_end,
               "ollama": version, "model": model, "options": options, "cold": a.cold, "questions": len(rows),
               "load_s": round(load_s, 1), "median_s": round(med, 1), "mean_s": round(statistics.mean(times), 1),
               "p90_s": times[round(0.9 * (len(times) - 1))], "min_s": times[0], "max_s": times[-1],
               "over_60_s": [x["id"] for x in rows if x["answer_time_s"] > 60], "O1_met": med <= 60, "machine": info,
               "evidence": {"size_vram_bytes": [s["api_ps"].get("size_vram") for s in snapshots],
                            "ollama_log": log or ("not found" if local else "not read: Ollama is not the app on this computer")}}
    folder = OUT / f"{datetime.date.today().isoformat()}_{a.label or a.device}"
    folder.mkdir(parents=True, exist_ok=True)
    with open(folder / "answers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (folder / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (folder / "ollama-ps.json").write_text(json.dumps(snapshots, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"\nEvidence: size_vram {summary['evidence']['size_vram_bytes']} bytes (after loading, middle, end)")
    for line in log:
        print("  Ollama log:", line[-160:])
    print(f"\n{where_end} | median {med:.1f} s | mean {summary['mean_s']} s | p90 {summary['p90_s']} s | max {times[-1]} s | load {load_s:.1f} s")
    print(f"O1 (median at most 60 s): {'met' if med <= 60 else 'NOT met'}" + (f" | over 60 s: {', '.join(summary['over_60_s'])}" if summary["over_60_s"] else ""))
    print(f"Saved in {folder.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
