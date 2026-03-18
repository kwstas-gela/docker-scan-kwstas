FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install flask==2.0.1 requests==2.25.1

CMD ["python", "app.py"]