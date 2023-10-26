FROM python:3.11.6-alpine as builder

WORKDIR /app

COPY src ./src
COPY utils ./utils
COPY requirements.txt ./
COPY *.py ./

RUN apk add binutils && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pyinstaller --noconfirm --onefile --clean --exclude tkinter --exclude _tkinter app.py


FROM python:3.11.6-alpine

WORKDIR /app

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r0

RUN { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java-home \
    && chmod +x /usr/local/bin/docker-java-home && \
    set -x && apk add --no-cache openjdk8 && [ "$JAVA_HOME" = "$(docker-java-home)" ]


COPY --from=builder ./app/dist .
COPY data ./data

CMD ["./app"]

EXPOSE 8567



#docker build -t spam-filter-service:1.0 .