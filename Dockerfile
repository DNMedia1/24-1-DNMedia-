FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir torch && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TRANSFORMERS_OFFLINE=1 \
    HF_DATASETS_OFFLINE=1 \
    HF_HOME=/models

VOLUME ["/input", "/output", "/logs", "/models"]

ENTRYPOINT ["python", "-m", "ki_system.cli"]
CMD ["--help"]
