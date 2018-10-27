FROM python:3.6

ADD ./requirements.txt /tmp/
ADD ./entrypoint.sh /tmp/
ADD ./bot/ /bot/
ADD ./docker/bot/endpoints.yml /tmp/

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

WORKDIR bot/

ENTRYPOINT ["sh","/tmp/entrypoint.sh"]
