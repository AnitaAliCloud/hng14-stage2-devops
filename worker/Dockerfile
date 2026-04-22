FROM python:3.11-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:3.11-slim

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

WORKDIR /app

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --find-links=/wheels /wheels/*

COPY --chown=appuser:appgroup . .

RUN rm -f .env *.env

USER appuser

HEALTHCHECK --interval=20s --timeout=5s --start-period=15s --retries=3 \
    CMD pgrep -f "python worker.py" || exit 1

CMD ["python", "worker.py"]