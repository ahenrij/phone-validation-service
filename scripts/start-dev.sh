#!/bin/bash

set -e

docker-compose -f docker-compose.dev.yml up --force-recreate --remove-orphans -d

uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
