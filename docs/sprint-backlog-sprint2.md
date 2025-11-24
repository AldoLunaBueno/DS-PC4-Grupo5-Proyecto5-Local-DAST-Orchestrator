# SPRINT 2 - Orquestación DAST y Reportes

## Issue 5: Integración del servicio DAST (ZAP) en Compose

* **Asignado a:** Luis
* **Descripción:** Añadir OWASP ZAP al stack Compose.
* **Tareas:**

  * Agregar servicio `zap` con `owasp/zap2docker-stable`.
  * Montar `./reports:/zap/wrk/`.
  * Validar visibilidad de red hacia el servicio web.

**Criterios de Aceptación:**
1. **Servicio ZAP Activo:** El archivo `docker-compose.yml` incluye el servicio `zap` y este inicia correctamente junto con `web` y `db.
2. **Visibilidad de Red:** El contenedor `zap` puede comunicarse con el contenedor `web` (probado mediante ping o curl desde dentro del contenedor `zap`).
3. **Persistencia de Reportes:** Un archivo creado dentro de la ruta `/zap/wrk/` en el contenedor `zap` es visible inmediatamente en la carpeta `reports/` de la máquina host.

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

**Criterios de Aceptación:**
1. **Verificación de Disponibilidad:** El script `dast/orchestrator.py` espera o verifica que el servicio web responda antes de iniciar el escaneo; si el servicio no responde, el script falla controladamente.
2. **Ejecución del Escaneo:** El script invoca exitosamente la herramienta ZAP contra el contenedor objetivo.
3. **Generación de Evidencia:** Al finalizar la ejecución del script, aparece un archivo de reporte (XML/HTML/JSON) en la carpeta `reports.
4. **Manejo de Errores:** El script captura excepciones de conexión y muestra mensajes de error legibles en consola.

---

## Issue 7: Procesamiento de reportes y métricas

* **Asignado a:** Aldo
* **Descripción:** Normalizar reportes de ZAP y actualizar métricas.
* **Tareas:**

  * `dast/parse_results.py`: extraer severidades, endpoints y generar `summary.json`.
  * Actualizar `docs/metrics.md` con endpoints, tiempos y hallazgos.

**Criterios de Aceptación:**
1. **Parseo de Datos:** El script `dast/parse_results.py` lee el reporte crudo y genera un archivo `reports/summary.json` válido.
2. **Contenido del Resumen:** El JSON generado contiene explícitamente la fecha de ejecución, el conteo de alertas por severidad y la lista de endpoints. 
3. **Actualización de Documentación:** El archivo `docs/metrics.md` ha sido editado para incluir las métricas reales obtenidas en las pruebas (endpoints escaneados, tiempo, hallazgos).

---

## Issue 8: Script de ejecución final y consolidación

* **Asignado a:** Luis
* **Descripción:** Crear un flujo “one-click” y su target Makefile.
* **Tareas:**

  * `run-dast.sh`: ejecutar orquestador + parser + mostrar ubicación del reporte.
  * Actualizar `make scan`.
  * Validar `.gitignore` y estructura final.

**Criterios de Aceptación:**
1. **Automatización "One-Click":** El comando `make scan` ejecuta la secuencia completa: orquestación DAST -> generación de reporte -> parseo de resultados, sin intervención manual. 
2. **Feedback al Usuario:** Al finalizar, la consola muestra la ruta absoluta o relativa donde se encuentra el reporte final generado.
3. **Robustez:** El script maestro `scripts/run-dast.sh` se detiene inmediatamente si alguno de los pasos intermedios falla (gracias a `set -e`).
4. **Limpieza de Repositorio:** No existen archivos basura, reportes antiguos o configuraciones de entorno (`.env`) trackeados en el repositorio remoto.

