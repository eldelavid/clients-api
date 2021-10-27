FROM python:latest
COPY . /app
WORKDIR /app
RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["/bin/bash", "entrypoint.sh"]
