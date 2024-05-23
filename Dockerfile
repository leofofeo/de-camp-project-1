FROM python:3.12.0-slim-bookworm

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

CMD python main.py run -h 0.0.0.0