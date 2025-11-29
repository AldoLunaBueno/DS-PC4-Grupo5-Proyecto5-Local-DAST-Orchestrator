# Makefile para automatizar el ciclo de vida del entorno de desarrollo y escaneo DAST.

.PHONY: setup dev compose-down clean scan help

SHELL := /bin/bash
.DEFAULT_GOAL := help

setup: ## Configurar entorno inicial
	@echo "Configurando el entorno de desarrollo..."
	@if [ ! -f "compose/.env" ]; then \
		echo "Creando archivo .env a partir de .env.example..."; \
		cp compose/.env.example compose/.env; \
		echo "Archivo .env creado. Por favor, revisa y ajusta las variables si es necesario."; \
	else \
		echo "El archivo .env ya existe. No se realizaron cambios."; \
	fi

# Levanta el stack de Docker Compose en modo detached.
# Utiliza el script 'start-stack.sh' para centralizar la lógica.
dev: ## Levantar stack
	@echo "Iniciando stack de desarrollo..."
	@./scripts/start-stack.sh

# Detiene y limpia los contenedores y volúmenes del stack.
# Utiliza el script 'stop-stack.sh'.
compose-down:
	@echo "Deteniendo y limpiando el stack..."
	@./scripts/stop-stack.sh

# Target de limpieza, alias para 'compose-down'.
clean: compose-down ## Borrar stack

# Ejecutar escaneo DAST completo.
scan: ## Escaneo DAST
	@echo "Ejecutando flujo completo de escaneo DAST..."
	@./scripts/run-dast.sh

# Muestra una lista de los targets disponibles con su descripción.
# Utiliza autodescripción basada en comentarios.
help: ## Listar tarjets
	@echo "Uso: make [target]"
	@echo ""
	@echo "Targets disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
