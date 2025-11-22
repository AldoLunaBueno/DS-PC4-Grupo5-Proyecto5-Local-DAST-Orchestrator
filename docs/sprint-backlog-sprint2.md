# SPRINT 2 - Orquestación DAST y Reportes

## Issue 5: Integración del servicio DAST (ZAP) en Compose

* **Asignado a:** Luis
* **Descripción:** Añadir OWASP ZAP al stack Compose.
* **Tareas:**

  * Agregar servicio `zap` con `owasp/zap2docker-stable`.
  * Montar `./reports:/zap/wrk/`.
  * Validar visibilidad de red hacia el servicio web.

---

## Issue 6: Desarrollo del Orquestador en Python

* **Asignado a:** Jharvy
* **Descripción:** Programar el orquestador del escaneo DAST.
* **Tareas:**

  * `dast/orchestrator.py`:

    * Verificar que la app esté arriba.
    * Ejecutar ZAP (`zap-baseline.py` o API).
    * Guardar reporte en `/zap/wrk/`.
    * Manejo de errores.

---

## Issue 7: Procesamiento de reportes y métricas

* **Asignado a:** Aldo
* **Descripción:** Normalizar reportes de ZAP y actualizar métricas.
* **Tareas:**

  * `dast/parse_results.py`: extraer severidades, endpoints y generar `summary.json`.
  * Actualizar `docs/metrics.md` con endpoints, tiempos y hallazgos.

---

## Issue 8: Script de ejecución final y consolidación

* **Asignado a:** Luis
* **Descripción:** Crear un flujo “one-click” y su target Makefile.
* **Tareas:**

  * `run-dast.sh`: ejecutar orquestador + parser + mostrar ubicación del reporte.
  * Actualizar `make scan`.
  * Validar `.gitignore` y estructura final.
