FROM ubuntu:22.04

RUN apt update

RUN apt install -y git python3 docker.io docker-buildx

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python3", "build.py"]
