FROM python:3.9.5-alpine3.13

LABEL MAINTAINER="Leonardo Wolter"

WORKDIR /usr/src/

ENTRYPOINT [ "poetry", "run", "python", "app/api.py" ]

ENV PORT=8080

EXPOSE $PORT

HEALTHCHECK CMD curl --fail http://localhost:$PORT/health || exit 1

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --no-cache gcc libffi-dev musl-dev openssl-dev

RUN pip3 install poetry     

COPY pyproject.toml poetry.lock ./   

RUN poetry install --no-dev --no-root  

COPY app app

RUN poetry install --no-dev 


