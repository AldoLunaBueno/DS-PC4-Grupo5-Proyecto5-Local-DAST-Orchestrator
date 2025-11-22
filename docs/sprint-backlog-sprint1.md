# SPRINT 1 - Infraestructura y Stack Base

## Issue 1: Inicialización de repositorio, estructura base y documentación inicial

* **Asignado a:** Aldo
* **Descripción:** Crear la estructura mínima del proyecto y la documentación base.
* **Tareas:**

**Directorios:** `app/`, `compose/`, `dast/`, `scripts/`, `reports/`, `docs/`.
**Documentación:**
  * `sprint-backlog-sprint1.md`: tareas del sprint 1.
  * `vision.md`: contexto, problema y objetivos.
  * `definition-of-done.md`: criterios de finalización.
  * `metrics.md`: plantilla de métricas Scrum/técnicas.
**Configuración raíz:**
  * Makefile con `setup`, `dev`, `scan`, `clean`.
  * `.gitignore` para entornos, cachés y `reports/` (solo `.gitkeep`).

---

## Issue 2: Desarrollo de aplicación web vulnerable y Dockerfile

* **Asignado a:** Jharvy
* **Descripción:** Implementar una aplicación vulnerable en Python y su contenedor.
* **Tareas:**

  * **App:** Crear `app/web.py` con endpoints `/health`, `/login`, `/cart`.
  * **Dependencias:** `app/requirements.txt`.
  * **Dockerfile:** Basado en `python:3.12-slim`, usuario no root y archivos mínimos.

---

## Issue 3: Configuración del Stack con Docker Compose

* **Asignado a:** Luis
* **Descripción:** Crear la infraestructura local con app + base de datos.
* **Tareas:**

  * **Servicios:** Web (build `../app`) + DB (`postgres:alpine` o `redis:alpine`).
  * **Redes:** Definir redes aisladas y límites de recursos.
  * **Variables:** Archivo `.env`, y `compose/.env.example`; evitar subir `.env`.

---

## Issue 4: Scripts de control de entorno y Makefile

* **Asignado a:** Aldo
* **Descripción:** Automatizar el ciclo del stack con scripts Bash y Makefile.
* **Tareas:**

  * Scripts: `start-stack.sh` y `stop-stack.sh`, con `#!/usr/bin/env bash` y `set -euo pipefail`.
  * Integración: `make dev` para levantar, `make compose-down`/`clean` para apagar.