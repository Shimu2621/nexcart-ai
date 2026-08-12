FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8001} --loop app.core.loop:loop_factory

# The flow is:

# Python 3.13 → create /app → install dependencies → copy application → start FastAPI

# Docker Image
    │
    ├── Python 3.13
    │
    ├── /app
    │
    ├── requirements.txt
    │      └── pip install dependencies
    │
    ├── Application source code
    │
    └── Uvicorn
           └── app.main:app
                  └── FastAPI