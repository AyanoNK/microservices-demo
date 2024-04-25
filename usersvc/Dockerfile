FROM python:3.8-slim

WORKDIR /app
RUN apt update
RUN apt install libpq-dev gcc -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
