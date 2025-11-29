#!/usr/bin/env bash
#
# Levanta el stack de Docker Compose en modo detached.
# Ejecuta 'docker-compose up' desde el directorio 'compose'.

# Modo estricto para scripts de Bash.
set -euo pipefail

# Obtener la ruta absoluta del directorio que contiene este script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
COMPOSE_FILE="${SCRIPT_DIR}/../compose/docker-compose.yml"

echo "Levantando el stack de Docker en segundo plano..."

# Ejecutar docker-compose up.
# -f: Especifica la ruta al archivo docker-compose.yml.
# --build: Reconstruye las imágenes si hay cambios en el Dockerfile.
# -d: Modo "detached" para que se ejecute en segundo plano.
docker-compose -f "${COMPOSE_FILE}" up --build -d

echo "Stack iniciado correctamente."
