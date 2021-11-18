FROM python:3.8-slim

RUN mkdir /app 

COPY /services /app
COPY pyproject.toml /app 

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV MODEL_NAME="facebook/bart-large-cnn"
ENV TOKENIZER_NAME="philschmid/bart-large-cnn-samsum"

RUN pip3 install poetry==1.1.11 \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

ENTRYPOINT ["python"]

CMD ["app.py"]