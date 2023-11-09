FROM python:3.11.6-slim-bookworm as builder

WORKDIR /app

COPY src ./src
COPY utils ./utils
COPY requirements.txt ./
COPY *.py ./

RUN apt update && apt install -y binutils && \
    pip install -r requirements.txt && \
    pip install pyinstaller && \
    pyinstaller --noconfirm --onefile --clean --exclude tkinter --exclude _tkinter app.py

FROM python:3.11.6-slim-bookworm

WORKDIR /app

COPY --from=builder ./app/dist .
COPY data ./data

CMD ["./app"]

EXPOSE 8567
