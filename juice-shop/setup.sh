#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.yml"

command -v docker >/dev/null 2>&1 || { echo 'Docker CLI não encontrado.' >&2; exit 1; }
docker info >/dev/null 2>&1 || { echo 'Docker Engine não está disponível.' >&2; exit 1; }
docker compose version >/dev/null 2>&1 || { echo 'Docker Compose v2 não está disponível.' >&2; exit 1; }

docker compose -f "$COMPOSE_FILE" pull
docker compose -f "$COMPOSE_FILE" up -d

echo 'Juice Shop: http://localhost:3000'