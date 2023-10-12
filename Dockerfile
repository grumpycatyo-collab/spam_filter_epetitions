FROM python:3.11.6-alpine3.17 as builder

WORKDIR /app

COPY src ./src
COPY utils ./utils
COPY data ./data
COPY requirements.txt ./
COPY *.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-B", "./app.py"]

EXPOSE 8567

#docker build -t spam-filter:1.0 .