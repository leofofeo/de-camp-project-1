FROM python:3.12.1-slim-bookworm

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install pandas

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

CMD python main.py run -h 0.0.0.0