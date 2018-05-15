FROM python:3

ADD ./run.py /

RUN pip install docker

CMD [ "python", "./run.py" ]