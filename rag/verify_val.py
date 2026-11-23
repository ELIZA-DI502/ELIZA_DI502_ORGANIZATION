"""Checks that the RAG service gives the same results as src/rag_vs_no_rag.ipynb (KAN-99, KAN-125).

Run from the repository root:

    python rag/verify_val.py              # retrieval only (bge-m3 on this computer, no Ollama needed)
    python rag/verify_val.py --answers    # also asks Ollama (OLLAMA_URL, default localhost:11434)
    python rag/verify_val.py --retrieval-out docs/eval/answers/val-service-retrieval.csv   # one row per question
    python rag/verify_val.py --score docs/eval/answers/val-service-answers.csv   # score saved answers, no Ollama

1. For every val question, the chunks found by rag/app/retrieval.py are compared with the chunks the notebook
   saved in docs/eval/answers/val-with-retrieval-llama-3-1-8b.csv (column "retrieved"). The service sorts the
   BM25 scores with a stable sort; the notebook's sort put equal scores in an order that depends on the
   processor. So a question may differ only when its BM25 scores have a tie at the edge of the 20 candidates
   (rank 20 and 21 have the same score), and Recall@8 must be the notebook's 0.59.
2. With --answers, every val question is asked with the service's prompt builder and Ollama options, and the
   answer is compared with the saved one. Answers on another computer are rarely word for word the same (the
   notebook ran on a Colab T4 GPU; one different word changes the rest of the answer, even with temperature 0
   and seed 42), so both sets of answers are also scored with the automatic checks of the notebook (cell
   "check": cites a provision, expected provision cited, cites only the chunks in the prompt, says the text
   does not answer). --score does only this step for answers saved earlier with --out.
"""
import argparse
import csv
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rag.app.config import ROOT  # noqa: E402
from rag.app.prompt import build_messages  # noqa: E402

VAL = ROOT / "docs" / "eval" / "eval-set-v1-val.csv"
SAVED = ROOT / "docs" / "eval" / "answers" / "val-with-retrieval-llama-3-1-8b.csv"
PROVISIONS = ROOT / "data" / "provision-list.csv"

# The automatic checks of src/rag_vs_no_rag.ipynb (cell "check"), unchanged.
CITE = re.compile(r"(Article\s+\d+[a-z]?(?:\s*\(\d+\))?(?:,?\s*(?:first|second|third|fourth|fifth)\s+subparagraph)?(?:,?\s*point)?(?:\s*\([a-z0-9]+\))*|Annex\s+[IVX]+(?:,?\s*point\s*\d+(?:\s*\([a-z]\))?)?)", re.I)
CHECKS = ["cites a provision", "expected provision cited (strict)", "expected provision cited (lenient)",
          "cites only retrieved chunks", "says the text does not answer"]


def norm(ref):
    ref = ref.lower()
    ref = re.sub(r"(first|second|third|fourth|fifth) subparagraph", "", ref)
    for n, word in enumerate(["first", "second", "third", "fourth"], 1):
        ref = ref.replace(f", {word} paragraph", f"({n})")
    return re.sub(r"[\s,]|point|paragraph", "", ref)


def check(q, answer, retrieved, reference, by_chunk):
    cited = sorted({norm(c) for c in CITE.findall(answer)})
    gold = [norm(reference[p]) for p in q["gold_ids"].split(";") if p in reference] if q["gold_ids"].strip() else []
    out = {"cites a provision": bool(cited), "says the text does not answer": "does not answer this question" in answer}
    if gold:
        out["expected provision cited (strict)"] = any(c == g for c in cited for g in gold)
        out["expected provision cited (lenient)"] = any(g.startswith(c) for c in cited for g in gold)
    if retrieved and cited:
        allowed = [norm(by_chunk[c]["ref"]) for c in retrieved]
        out["cites only retrieved chunks"] = all(any(a.startswith(c) or c.startswith(a) for a in allowed) for c in cited)
    return out


def score_table(val, sides, reference, by_chunk):
    """sides: {name: (answers by id, retrieved chunk IDs by id)}. Prints each check as 'n of m' per side."""
    counts = {}
    for name, (answers, retrieved) in sides.items():
        rows = [check(q, answers[q["id"]], retrieved[q["id"]], reference, by_chunk) for q in val]
        counts[name] = {c: (sum(bool(r[c]) for r in rows if c in r), sum(1 for r in rows if c in r)) for c in CHECKS}
    width = max(len(c) for c in CHECKS)
    print("\n" + " " * width + "".join(f"  {name:>22s}" for name in sides))
    for c in CHECKS:
        print(f"{c:{width}s}" + "".join(f"  {f'{k} of {n}':>22s}" for k, n in (counts[name][c] for name in sides)))
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--answers", action="store_true", help="also compare the answers of Ollama")
    parser.add_argument("--out", help="with --answers: write the new answers to this CSV file")
    parser.add_argument("--retrieval-out", help="write the chunks of the notebook and of the service per question to this CSV file")
    parser.add_argument("--score", help="score the answers in this CSV file (written by --out) against the notebook's")
    args = parser.parse_args()

    val = list(csv.DictReader(VAL.open(encoding="utf-8-sig")))        # test is never opened
    by_id = {q["id"]: q for q in val}
    saved = {r["id"]: r for r in csv.DictReader(SAVED.open(encoding="utf-8"))}
    assert set(saved) == set(by_id), "the saved answers must cover exactly the val questions"

    from rag.app.retrieval import Retriever
    started = time.time()
    retriever = Retriever()
    print(f"retriever ready in {time.time() - started:.0f} s ({len(retriever.ids)} chunks)")

    import numpy as np
    from rag.app.retrieval import R, words
    found, different, tie = {}, [], {}
    for q in val:
        found[q["id"]] = retriever.search(q["question"])
        scores = np.sort(retriever.bm25.get_scores([w for w in words(q["question"]) if w not in retriever.remove]))[::-1]
        tie[q["id"]] = bool(scores[R["candidates"] - 1] == scores[R["candidates"]])
        ids = ";".join(c["chunk_id"] for c in found[q["id"]])
        if ids != saved[q["id"]]["retrieved"]:
            different.append((q["id"], saved[q["id"]]["retrieved"], ids))
    for qid, old, new in different:
        print(f"  {qid} (BM25 tie at rank 20: {'yes' if tie[qid] else 'NO'})\n    notebook: {old}\n    service:  {new}")
    print(f"same chunks in the same order: {len(val) - len(different)} of {len(val)} val questions")
    unexplained = [qid for qid, _, _ in different if not tie[qid]]
    print(f"different without a BM25 tie at rank 20: {len(unexplained)}")

    scored = [q for q in val if q["gold_ids"].strip()]
    recall = sum(len(set(q["gold_ids"].split(";")) & {c["chunk_id"].split("#")[0] for c in found[q["id"]]})
                 / len(q["gold_ids"].split(";")) for q in scored) / len(scored)
    print(f"Recall@8 on {len(scored)} val questions: {recall:.2f} (notebook: 0.59)")
    if args.retrieval_out:
        with open(args.retrieval_out, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "retrieved_notebook", "retrieved_service", "same", "bm25_tie_at_rank_20"])
            for q in val:
                new = ";".join(c["chunk_id"] for c in found[q["id"]])
                writer.writerow([q["id"], saved[q["id"]]["retrieved"], new, new == saved[q["id"]]["retrieved"], tie[q["id"]]])
        print("written:", args.retrieval_out)
    ok = not unexplained and f"{recall:.2f}" == "0.59"

    reference = {r["provision_id"]: r["reference"] for r in csv.DictReader(PROVISIONS.open(encoding="utf-8"))}
    notebook_side = ({i: saved[i]["answer"] for i in saved}, {i: saved[i]["retrieved"].split(";") for i in saved})
    service_retrieved = {i: [c["chunk_id"] for c in found[i]] for i in found}

    if args.score:
        new = {r["id"]: r["answer"] for r in csv.DictReader(open(args.score, encoding="utf-8"))}
        assert set(new) == set(by_id), "the scored file must cover exactly the val questions"
        print(f"answers identical to the notebook: {sum(new[i] == saved[i]['answer'] for i in new)} of {len(new)}")
        score_table(val, {"notebook (Colab GPU)": notebook_side, "service": (new, service_retrieved)},
                    reference, retriever.by_chunk)

    if args.answers:
        from rag.app import llm
        rows, same = [], 0
        for n, q in enumerate(val, 1):
            m = re.match(r"follows (\S+)", q["context"].strip())          # as previous_of() in the notebook
            history = [{"question": by_id[m[1]]["question"]}] if m else []
            t = time.time()
            answer, _ = llm.chat(build_messages(q["question"], history, found[q["id"]]))
            seconds = round(time.time() - t, 1)
            same += answer == saved[q["id"]]["answer"]
            rows.append({"id": q["id"], "answer": answer, "same_as_notebook": answer == saved[q["id"]]["answer"],
                         "seconds": seconds})
            print(f"{n}/{len(val)} {q['id']} ({seconds} s) {'same' if rows[-1]['same_as_notebook'] else 'different'}")
        print(f"answers identical to the notebook: {same} of {len(val)}")
        score_table(val, {"notebook (Colab GPU)": notebook_side,
                          "service": ({r["id"]: r["answer"] for r in rows}, service_retrieved)},
                    reference, retriever.by_chunk)
        if args.out:
            with open(args.out, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            print("written:", args.out)

    print("OK: the service retrieves as the notebook (differences only where BM25 has a tie at rank 20)"
          if ok else "NOT THE SAME: see the lines above")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
