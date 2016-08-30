FROM python:2

ADD writer/requirements.txt /opt/writer/requirements.txt

WORKDIR /opt/writer


RUN pip install -r requirements.txt


CMD ["python", "./dbTest.py"]

CMD ["python", "./writer.py"]
