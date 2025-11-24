# Visión del Proyecto

## Contexto

Este proyecto se enmarca en la necesidad de automatizar pruebas de seguridad dinámicas (DAST) de manera temprana en el ciclo de desarrollo de forma local utilizando contenedores (OWASP ZAP) integrados en un flujo de Docker Compose.

## Problema
La dependencia de escáneres externos o manuales retrasa la detección de vulnerabilidades. Se requiere una solución "local-first" y desconectada (simulando entorno *air-gapped*) para pruebas rápidas y seguras.

## Alcance
* **Duración:** 10 días (2 Sprints).
* **Incluye:** App web Python, base de datos, contenedor ZAP, y orquestador en Python/Bash.
* **Excluye:** Uso de proveedores Cloud (AWS/GCP/Azure) o Kubernetes.

## Objetivos Técnicos
* **Orquestación:** Configurar `docker-compose.yml` para levantar la app (`web`), base de datos (`db`) y el escáner (`zap`) en redes aisladas.
* **Automatización:** Desarrollar `orchestrator.py` y `run-dast.sh` para ejecutar el ataque y recolectar evidencias en `reports/` automáticamente.
* **Hardening:** Implementar contenedores seguros (imágenes slim, `USER` no root).

## Objetivos de Aprendizaje
Dominar la integración de herramientas de seguridad (DAST) en entornos locales, scripting defensivo para orquestación y gestión de evidencias de seguridad.