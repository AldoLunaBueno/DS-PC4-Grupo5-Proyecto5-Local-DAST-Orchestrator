# Local DAST Orchestrator

## Descripción del Proyecto

Este proyecto implementa un sistema automatizado para realizar pruebas de seguridad dinámicas (DAST) sobre aplicaciones web en un entorno local. La idea principal es poder analizar vulnerabilidades de seguridad en aplicaciones antes de llevarlas a producción, todo esto ejecutándose en la propia máquina del desarrollador.

El sistema utiliza OWASP ZAP como herramienta de escaneo y está completamente containerizado con Docker, lo que facilita su portabilidad y reproducibilidad entre diferentes entornos de desarrollo.

## Componentes Principales

El proyecto está compuesto por varios elementos que trabajan en conjunto:

### Aplicación Web Objetivo

Una aplicación Flask simple que simula un sistema real con endpoints típicos como login, health check y un carrito de compras. Esta aplicación sirve como objetivo para las pruebas de seguridad.

### Base de Datos

PostgreSQL corriendo en un contenedor separado, simulando un stack completo de aplicación con componentes de backend y base de datos.

### Escáner de Seguridad

OWASP ZAP configurado en modo daemon que analiza la aplicación web buscando vulnerabilidades comunes como inyecciones SQL, cross-site scripting, configuraciones inseguras, entre otras.

### Orquestador

Scripts en Python que coordinan todo el proceso: verifican que la aplicación esté lista, ejecutan el escaneo usando la API de ZAP, y procesan los resultados para generar reportes legibles.

### Automatización

Scripts en Bash y un Makefile que simplifican la ejecución de todo el flujo, permitiendo iniciar el entorno completo y ejecutar escaneos con comandos cortos.

## Flujo de Trabajo

El proceso de uso del sistema sigue estos pasos:

1. Se levanta el stack completo con la aplicación web, base de datos y ZAP usando Docker Compose
2. Se ejecuta el orquestador que valida la disponibilidad de la aplicación
3. ZAP realiza el escaneo de seguridad contra los endpoints de la aplicación
4. Los resultados se procesan y se generan reportes en formato HTML y JSON
5. Se actualiza la documentación de métricas con los hallazgos del escaneo

Todo esto se puede ejecutar con comandos simples del Makefile, facilitando su uso en el día a día.

## Estructura del Repositorio

- `app/` - Código de la aplicación web objetivo y su Dockerfile
- `compose/` - Archivos de Docker Compose para levantar el stack completo
- `dast/` - Scripts de orquestación y procesamiento de resultados
- `scripts/` - Scripts Bash para controlar el ciclo de vida del entorno
- `reports/` - Directorio donde se almacenan los reportes generados
- `docs/` - Documentación del proyecto y métricas

## Uso Básico

Configurar el entorno por primera vez:
```bash
make setup
```

Levantar el stack completo:
```bash
make dev
```

Ejecutar un escaneo de seguridad:
```bash
make scan
```

Detener todo:
```bash
make clean
```

## Requisitos

- Docker y Docker Compose instalados
- Python 3.12 o superior
- Make
- Conexión a internet para descargar las imágenes Docker

## Resultados

Después de ejecutar un escaneo, se generan tres archivos principales:

- `reports/zap_report.html` - Reporte visual detallado con todas las vulnerabilidades encontradas
- `reports/zap_report.json` - Datos crudos del escaneo en formato JSON
- `reports/summary.json` - Resumen ejecutivo con conteo de alertas por severidad
- `docs/metrics.md` - Documentación actualizada con métricas del último escaneo