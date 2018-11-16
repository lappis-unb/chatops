FROM python:3.6-slim

RUN apt update && apt install -y make

ADD ./requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR bot/

ADD ./docker/bot.entrypoint.sh /tmp/
ADD ./bot/ /bot/

ENTRYPOINT ["sh","/tmp/bot.entrypoint.sh"]
