FROM python:2

ADD writer /opt/writer
WORKDIR /opt/writer


RUN pip install -r requirements.txt


CMD ["python", "./dbTest.py"]

CMD ["python", "./writer.py"]
