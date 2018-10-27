FROM python:3.6

ADD ./bot/actions.py /actions/
ADD ./bot/Makefile /actions/

RUN pip install --upgrade pip && \
    pip install rasa-core-sdk==0.11.5

WORKDIR actions/

ENTRYPOINT ["make","run-actions"]
