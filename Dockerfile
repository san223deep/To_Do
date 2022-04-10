FROM python:3

ENV VENV 1

RUN pip install --upgrade pip

WORKDIR /To_Do

ADD . /To_Do

COPY ./requirements.txt /To_Do/requirements.txt

RUN pip install -r requirements.txt

COPY . /To_Do
