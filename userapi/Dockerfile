# Deploys a simple Python API with simple CRUD functionality.
# Requires a Redis DB to function. Made for DevOps @ DSTI 2022

FROM python:3.8-slim AS builder
COPY . /userapi
WORKDIR /userapi
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN python3 -m pip install -r requirements.txt

FROM python:3.8-alpine
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /userapi
WORKDIR /userapi/src
EXPOSE 3000
CMD uvicorn api:app --host 0.0.0.0