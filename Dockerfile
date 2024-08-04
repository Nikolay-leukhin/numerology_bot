FROM python:3.9
WORKDIR app/
COPY requirements.txt requirements.txt
RUN py -m pip install --upgrade setuptools
RUN py -m pip install -r requirements.txt
RUN chmod 755 .
COPY . .

