FROM python:3.12.1-alpine3.19

WORKDIR /numerology_bot


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod -R 755 .

CMD ["python", "main.py"]
