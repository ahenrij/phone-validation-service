FROM python:3.10-slim-buster as base

LABEL maintainer="Henri Aïdasso <ahenrij@gmail.com>"
LABEL name="darkpearl/phone-validation-service"
LABEL version="0.1.0"

EXPOSE 8000

WORKDIR /app

# Install Poetry
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /app/

# Install dependencies
RUN poetry install --no-root --no-dev

COPY . .

RUN chmod +x scripts/start.sh

CMD ["scripts/start.sh"]

#################################
# TESTING STAGE IMAGE
#################################
FROM base AS test

RUN poetry install --no-root
