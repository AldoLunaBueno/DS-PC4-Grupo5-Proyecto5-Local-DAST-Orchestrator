#!/usr/bin/env bash
#
# Detiene y elimina los contenedores, redes y volúmenes del stack.
# Ejecuta 'docker-compose down' desde el directorio 'compose'.

# Modo estricto para scripts de Bash.
set -euo pipefail

# Obtener la ruta absoluta del directorio que contiene este script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
COMPOSE_FILE="${SCRIPT_DIR}/../compose/docker-compose.yml"

echo "Deteniendo y limpiando el stack de Docker..."

# Ejecutar docker-compose down.
# -f: Especifica la ruta al archivo docker-compose.yml.
# -v: Elimina los volúmenes anónimos asociados a los contenedores.
docker-compose -f "${COMPOSE_FILE}" down -v

echo "Stack detenido y limpiado correctamente."
