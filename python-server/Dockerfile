# basic image with installed python
FROM python:3.9-alpine
WORKDIR /app
# copy only req
COPY requirements.txt requirements.txt
# run install dependency
RUN pip install --no-cache /wheels/*
# copy all
COPY . .
#exspose port
EXPOSE 8080
CMD ["python3","-m", "APP"]
