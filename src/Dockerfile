FROM ubuntu:20.04

RUN    apt-get clean && apt-get update -y
RUN    apt-get install python3 -y && ln -s /usr/bin/python3 /usr/bin/python
RUN    apt-get update -y
RUN    apt-get install python3-pip -y
RUN    apt-get install libpq-dev gcc -y
RUN    apt-get update -y

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/
COPY templates/profile.html /usr/src/app/templates/

EXPOSE 5000

CMD ["python", "/usr/src/app/app.py"]
