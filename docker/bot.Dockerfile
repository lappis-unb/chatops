FROM python:3.6-slim

RUN apt update && apt install -y git gcc make curl

ADD ./requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR bot/

ADD ./bot/ /bot/

CMD make train-nlu && make train-core && make run-telegram
