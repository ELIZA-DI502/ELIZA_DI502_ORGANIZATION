# rag container (D2): the FastAPI RAG service. Build context: the repository root (docker-compose.yml).
FROM python:3.12.16-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    HF_HOME=/root/.cache/huggingface \
    ELIZA_ROOT=/app

WORKDIR /app

# The CPU build of PyTorch first (no GPU in the containers, C-05), then the same packages as rag/ingest.py (D5).
COPY requirements.txt /app/requirements.txt
COPY rag/requirements.txt /app/rag/requirements.txt
RUN pip install torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu \
 && pip install -r /app/rag/requirements.txt

COPY config /app/config
COPY prompts /app/prompts
COPY data/chunks.jsonl /app/data/chunks.jsonl
COPY rag /app/rag

EXPOSE 8000
CMD ["uvicorn", "rag.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
