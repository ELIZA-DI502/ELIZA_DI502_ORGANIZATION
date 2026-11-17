"""Checks that the RAG service gives the same results as src/rag_vs_no_rag.ipynb (KAN-99, KAN-125).

Run from the repository root:

    python rag/verify_val.py              # retrieval only (bge-m3 on this computer, no Ollama needed)
    python rag/verify_val.py --answers    # also asks Ollama (OLLAMA_URL, default localhost:11434)
    python rag/verify_val.py --retrieval-out docs/eval/answers/val-service-retrieval.csv   # one row per question

1. For every val question, the chunks found by rag/app/retrieval.py are compared with the chunks the notebook
   saved in docs/eval/answers/val-with-retrieval-llama-3-1-8b.csv (column "retrieved"). The service sorts the
   BM25 scores with a stable sort; the notebook's sort put equal scores in an order that depends on the
   processor. So a question may differ only when its BM25 scores have a tie at the edge of the 20 candidates
   (rank 20 and 21 have the same score), and Recall@8 must be the notebook's 0.59.
2. With --answers, every val question is asked with the service's prompt builder and Ollama options, and the
   answer is compared with the saved one. The same retrieved chunks and prompt are the check that matters:
   the notebook ran on a Colab T4 GPU, so an answer on another computer can differ in a few words even with
   temperature 0 and seed 42.
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


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--answers", action="store_true", help="also compare the answers of Ollama")
    parser.add_argument("--out", help="with --answers: write the new answers to this CSV file")
    parser.add_argument("--retrieval-out", help="write the chunks of the notebook and of the service per question to this CSV file")
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
