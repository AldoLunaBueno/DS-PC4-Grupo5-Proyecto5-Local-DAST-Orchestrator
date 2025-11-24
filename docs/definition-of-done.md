# Definition of Done (DoD)

Mientras que los Criterios de Aceptación verifican que **funciona**, estos DoD verifican que está **listo para entrega/producción** con la calidad requerida.

---

## SPRINT 1 - Infraestructura

### Issue 1: Inicialización y Docs
* **Estándar Markdown:** Todos los documentos en `docs/` tienen formato Markdown válido y son legibles.
* **Higiene del Repositorio:** No existen archivos temporales ni carpetas vacías innecesarias (fuera de los `.gitkeep` requeridos) ensuciando la raíz.
* **Targets Funcionales:** Los targets del Makefile definidos (`setup`, etc.) ejecutan sin arrojar errores de sintaxis, aunque estén vacíos.

### Issue 2: App Vulnerable y Dockerfile
* **Buenas Prácticas Docker:** El análisis de la imagen (linter de Docker) no arroja alertas críticas sobre el uso de usuario root o etiquetas `latest.
* **Limpieza de Dependencias:** El archivo `requirements.txt` contiene versiones fijas (pinned versions) para evitar roturas futuras, no solo nombres de librerías.
* **Código Limpio:** El código Python (`app/web.py`) cumple con convenciones básicas de estilo (PEP 8) y no tiene credenciales hardcodeadas.

### Issue 3: Stack Docker Compose
* **Validación de Configuración:** El comando `docker-compose config` devuelve una sintaxis válida sin errores.
* **Seguridad de Secretos:** Se ha verificado manualmente que el archivo `.env` está listado en `.gitignore` y no aparece en el control de versiones.
* **Documentación de Variables:** Cada variable usada en el `docker-compose.yml` tiene su contraparte documentada en `.env.example.

### Issue 4: Scripts Bash
* **Análisis Estático:** Los scripts pasan una validación de sintaxis (ej. `bash -n scripts/start-stack.sh`) y tienen permisos de ejecución (`chmod +x`).
* **Idioma:** Los comentarios explicativos dentro del código están redactados en español, como se solicitó explícitamente.
* **Modo Estricto:** Se verifica visualmente que la primera línea efectiva de código sea `set euo pipefail.

---

## SPRINT 2 - Orquestación DAST

### Issue 5: Integración ZAP
* **Integridad de Volúmenes:** El mapeo de volúmenes `./reports` funciona en ambos sentidos (lectura/escritura) sin problemas de permisos de usuario (UID/GID) en el host.
* **Optimización:** Se utiliza la imagen específica solicitada (`stable` o `fake-zap`) y no una versión pesada innecesaria.

### Issue 6: Orquestador Python
* **Manejo de Excepciones:** El código no "truena" (crashing) mostrando el *stack trace* completo al usuario final ante un error de conexión, sino que sale ordenadamente.
* **Independencia:** El script puede ejecutarse múltiples veces consecutivas sin fallar porque el archivo de reporte anterior ya exista (debe sobrescribir o versionar).

### Issue 7: Parseo y Métricas
* **Validez JSON:** El archivo de salida `summary.json` es un JSON válido (parseable por herramientas estándar como `jq`).
* **Actualización de Métricas:** El archivo `docs/metrics.md` no contiene "placeholders" o datos de ejemplo, sino datos de una ejecución real del sprint.

### Issue 8: Script Maestro y Entrega
* **Prueba "Desde Cero":** El script `scripts/run-dast.sh` funciona correctamente en un entorno limpio (tras ejecutar `make clean` o `docker system prune`), garantizando que no depende de estados anteriores.
* **Verificación de Entregables:** La estructura final de carpetas coincide exactamente con la especificada en el Issue 1, sin archivos sobrantes.
* **Sin Errores Silenciosos:** El uso de `set -e` en el script maestro está verificado; si el orquestador falla, el parser no debe intentar ejecutarse.