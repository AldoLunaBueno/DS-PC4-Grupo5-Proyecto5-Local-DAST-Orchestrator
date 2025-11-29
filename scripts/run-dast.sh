#!/usr/bin/env bash

# Script se detiene en cualquier error.
set -euo pipefail

# Obtener ruta absoluta del directorio raíz del proyecto.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."

echo "Iniciando flujo completo de escaneo DAST"

# Ejecutar orquestador que ejecuta escaneo ZAP.
echo "[1/3] Ejecutando orquestador de escaneo..."
python "${PROJECT_ROOT}/dast/orchestrator.py"

# Procesar resultados y generar resumen.
echo "[2/3] Procesando resultados del escaneo..."
python "${PROJECT_ROOT}/dast/parse_results.py"

# Mostrar ubicación de reportes generados.
echo "[3/3] Escaneo completado exitosamente."
echo "Reportes generados en:"
echo "  ${PROJECT_ROOT}/reports/"
echo "Archivos disponibles:"
ls -lh "${PROJECT_ROOT}/reports/" | grep -v "^total" | grep -v ".gitkeep" || echo "  (ningún reporte encontrado)"
