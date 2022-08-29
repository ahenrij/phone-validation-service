#!/bin/bash

set -e

docker-compose -f docker-compose.dev.yml up --force-recreate --remove-orphans -d

./scripts/start.sh
