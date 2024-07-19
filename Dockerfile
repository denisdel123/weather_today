FROM ubuntu:latest
LABEL authors="denisbelenko"

ENTRYPOINT ["top", "-b"]