FROM python:3.11.4

WORKDIR /app

COPY . .

RUN pip install requirements.txt

CMD gunicorn --bunc 0.0.0.0:5000 wsgi:app