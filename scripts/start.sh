#! /usr/bin/env bash

# Start API
poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
