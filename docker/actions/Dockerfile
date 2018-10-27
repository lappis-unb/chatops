FROM python:3.6

ADD ./bot/actions.py /actions/
ADD ./bot/Makefile /actions/
ADD ./docker/actions/requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

WORKDIR actions/

ENTRYPOINT ["make","run-actions"]
