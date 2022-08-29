FROM python:3.10.5-slim-buster as base

WORKDIR /app

# Install Poetry
RUN pip3 install poetry

COPY ./pyproject.toml ./poetry.lock ./scripts/poetry-install.sh /app/

ENV PATH="/root/.local/bin:$PATH"

# Install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-dev

COPY . .

RUN chmod +x scripts/start.sh

CMD ["scripts/start.sh"]

# Testing Stage Image
FROM base AS test
RUN poetry install --no-root
