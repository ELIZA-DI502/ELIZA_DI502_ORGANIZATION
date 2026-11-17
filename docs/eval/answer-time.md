# Answer time on the CPU (O1, R-12)

**Why:** the spike measured 15.4 s for Llama-3.1-8B on a Mac with an M3 Pro chip ([model selection spike](../spikes/model-selection-spike.md), "Answer time on one team computer"). Reviewer 3 asked whether that time really came from the CPU only, because Apple silicon shares its memory between the CPU and the GPU. The spike set `num_gpu` 0 but did not check where the model was loaded.

**What [`src/answer_time.py`](../../src/answer_time.py) measures:** the time the answer model needs for each of the 30 `val` questions. O1 asks for a median of at most 60 s. The prompt and settings are those of the RAG service (KAN-122): `prompts/answer.yaml`, filled as `rag/app/prompt.py` does it, and the model and options of `rag/app/config.py` (`llama3.1:8b-instruct-q4_K_M`, temperature 0, at most 300 tokens, context window 4,096). The script does not import `rag/`, so it also runs without the demo code. Each question gets the 8 chunks the search retrieved for it in the Sprint 2 baseline (`answers/val-with-retrieval-chunks.jsonl`). Retrieval time is not included.

**How the CPU is checked:** after loading the model, in the middle of the run and at the end, the script asks Ollama where the model is (`/api/ps`). With `--device cpu` it stops if any part of the model is in GPU memory (`size_vram` > 0). The evidence is saved with the results:
- `ollama-ps.json`: Ollama's raw answers at these three moments, with `size` (the model's memory) and `size_vram` (the part in GPU memory; 0 = CPU only)
- `summary.json` → `evidence`: the three `size_vram` values and, for the Ollama app on the Mac, the lines of its log (`~/.ollama/logs/server.log`) written while loading that say how many layers went to the GPU
- a run with `--device gpu` for contrast: there `size_vram` is above 0 and the reading speed (tokens/s) is much higher

## Run

From the repository root, with the packages of `requirements.txt` (only `pyyaml` is needed). Keep the Mac plugged in, close heavy apps, and run only one measurement at a time.

**1. The `ollama` container (how the system runs, CPU only, also on a Mac).** The container of `docker-compose.yml` publishes no port, so start the same image with the same model volume on port 11435:

```bash
docker compose stop                       # so the model is not loaded twice
docker run -d --rm --name eliza-ollama-time -p 127.0.0.1:11435:11434 \
  -v eliza_ollama-models:/root/.ollama ollama/ollama:0.40.15
docker exec eliza-ollama-time ollama pull llama3.1:8b-instruct-q4_K_M   # only if the volume does not have it yet
python src/answer_time.py --url http://localhost:11435 --label docker
docker stop eliza-ollama-time
```

The result depends on the CPUs and memory given to Docker (Docker Desktop → Settings → Resources). The script saves them with the results.

**2. The Ollama app on the Mac, CPU only (`num_gpu` 0), as in the spike:**

```bash
ollama pull llama3.1:8b-instruct-q4_K_M   # once
python src/answer_time.py
```

**3. For comparison, the same with the GPU (Metal):** `python src/answer_time.py --device gpu`

Other options: `--ids A-01 D-08` runs only some questions. `--cold` reloads the model before every question, so no part of the prompt comes from Ollama's cache; this is stricter but slower.

## Results

Saved in `answer-time/<date>_<label>/`:
- `answers.csv`: for each question, the answer time, the tokens read and written with their speeds, whether the 300-token limit was hit, and the answer
- `summary.json`: median, mean, p90, minimum and maximum, loading time, where the model was placed (for example `100% CPU`), Ollama version, CPU, RAM, Docker resources, whether O1 is met, and the evidence above
- `ollama-ps.json`: the raw `/api/ps` answers

A second run with the same label on the same day replaces the folder.
