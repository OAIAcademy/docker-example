FROM python:3.9-slim as installer
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=installer /app/wheels /wheels
COPY --from=installer /app/requirements.txt .
RUN pip install --no-cache /wheels/*
EXPOSE ${PORT}
COPY . .
CMD ["python3","-m", "APP"]