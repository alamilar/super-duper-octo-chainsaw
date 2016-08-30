FROM python:2

ADD reader/requirements.txt /opt/reader/requirements.txt

WORKDIR /opt/reader


RUN pip install -r requirements.txt


CMD ["python", "./dbTest.py"]

CMD ["gunicorn", "--workers=4", "-b 0.0.0.0:5000", "wsgi:app"]
