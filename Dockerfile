FROM alpine

RUN apk update && apk -U upgrade
RUN apk add python3 py3-pip curl tzdata
RUN apk cache clean

COPY . /duty-notifier/
WORKDIR /duty_notifier
RUN python -m venv venv && source venv/bin/activate && curl -sSL https://bootstrap.pypa.io/get-pip.py | python && pip install --no-cache -r requirements.txt && deactivate

CMD ["venv/bin/python", "main.py"]    