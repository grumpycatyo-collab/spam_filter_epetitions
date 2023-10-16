FROM python:3.11.6-alpine3.17 as builder

WORKDIR /app

COPY src ./src
COPY utils ./utils
COPY data ./data
COPY requirements.txt ./
COPY *.py ./
RUN pip install -r requirements.txt
RUN { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java-home \
    && chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r0

RUN set -x && apk add --no-cache openjdk8 && [ "$JAVA_HOME" = "$(docker-java-home)" ]

CMD ["python", "-B", "./app.py"]

EXPOSE 8567

#docker build -t spam-filter-service:1.0 .