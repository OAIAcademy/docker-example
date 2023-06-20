# basic image with installed python
FROM python:3.9-slim
WORKDIR /app
# install curl
RUN apt update && apt install curl -y
# copy only req
COPY requirements.txt requirements.txt
# run install dependency
RUN pip install -r requirements.txt
# copy all
COPY .. .
#exspose port
EXPOSE 8080
CMD ["python3","-m", "APP"]
