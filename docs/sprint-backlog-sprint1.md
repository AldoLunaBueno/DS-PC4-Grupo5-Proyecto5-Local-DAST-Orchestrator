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

**Criterios de Aceptación:**
1. **Estructura de Carpetas:** El repositorio contiene exactamente las carpetas `app/`, `compose/`, `dast/`, `scripts/`, `reports/`, y `docs/` en la raíz. 
2. **Documentación Base:** Existen los archivos `vision.md`, `definition-of-done.md` y `metrics.md` dentro de la carpeta `docs/` con el contenido inicial requerido. 
3. **Configuración Git:** El archivo `.gitignore` bloquea efectivamente la subida de carpetas `env`, `__pycache__/`, `venv/` y el contenido de `reports/` (excepto `.gitkeep`).
4. **Makefile Inicial:** Ejecutar el comando `make setup` en la terminal no devuelve errores (incluso si solo imprime un mensaje).
---

## Issue 2: Desarrollo de aplicación web vulnerable y Dockerfile

* **Asignado a:** Jharvy
* **Descripción:** Implementar una aplicación vulnerable en Python y su contenedor.
* **Tareas:**

  * **App:** Crear `app/web.py` con endpoints `/health`, `/login`, `/cart`.
  * **Dependencias:** `app/requirements.txt`.
  * **Dockerfile:** Basado en `python:3.12-slim`, usuario no root y archivos mínimos.

**Criterios de Aceptación:**
1. **Endpoints Funcionales:** Al ejecutar la aplicación localmente, una petición `GET /health` retorna código HTTP 200.
2. **Seguridad de Imagen:** El `Dockerfile` utiliza la imagen base `python:3.12-slim` y no la etiqueta `latest.
3. **Usuario No Root:** Al inspeccionar el contenedor en ejecución (ej. `docker exec`), el proceso corre bajo el usuario `appuser` y no como `root.
4. **Contexto de Build:** El archivo `requirements.txt` existe dentro de la imagen y las dependencias se instalan correctamente durante el build.

---

## Issue 3: Configuración del Stack con Docker Compose

* **Asignado a:** Luis
* **Descripción:** Crear la infraestructura local con app + base de datos.
* **Tareas:**

  * **Servicios:** Web (build `../app`) + DB (`postgres:alpine` o `redis:alpine`).
  * **Redes:** Definir redes aisladas y límites de recursos.
  * **Variables:** Archivo `.env`, y `compose/.env.example`; evitar subir `.env`.

**Criterios de Aceptación:**
1. **Levantamiento de Servicios:** El comando `docker-compose up` levanta exitosamente los servicios `web` y `db`. 
2. **Aislamiento de Red:** Los servicios están asignados a las redes personalizadas (ej. `frontend-net`) y no usan la red `bridge` por defecto.
3. **Límites de Recursos:** Al ejecutar `docker stats`, los contenedores muestran los límites de memoria y CPU definidos en el archivo YAML.
4. **Seguridad de Secretos:** El archivo `.env` está presente localmente para la ejecución, pero **no** está rastreado por git; en su lugar existe `.env.example`. 

---

## Issue 4: Scripts de control de entorno y Makefile

* **Asignado a:** Aldo
* **Descripción:** Automatizar el ciclo del stack con scripts Bash y Makefile.
* **Tareas:**

  * Scripts: `start-stack.sh` y `stop-stack.sh`, con `#!/usr/bin/env bash` y `set -euo pipefail`.
  * Integración: `make dev` para levantar, `make compose-down`/`clean` para apagar.

**Criterios de Aceptación:**
1. **Calidad de Scripting:** Los scripts `start-stack.sh` y `stop-stack.sh` comienzan con `#!/usr/bin/env bash` y contienen la instrucción `set euo pipefail.
2. **Automatización del Inicio:** Ejecutar `make dev` invoca `scripts/start-stack.sh` y levanta los contenedores en modo *detached* (segundo plano).
3. **Limpieza Correcta:** Ejecutar `make compose-down` (o `clean`) detiene los contenedores y elimina los volúmenes asociados sin dejar procesos huérfanos.
4. **Documentación en Código:** Los scripts contienen comentarios explicativos en español.