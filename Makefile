.PHONY: help build up down logs migrate createsuperuser dev prod

help:
	@echo "Available commands:"
	@echo "  make build          - Build Docker images"
	@echo "  make up             - Start containers (development)"
	@echo "  make down           - Stop containers"
	@echo "  make logs           - View logs"
	@echo "  make migrate        - Run migrations"
	@echo "  make createsuperuser - Create superuser"
	@echo "  make dev            - Start development environment"
	@echo "  make prod           - Start production environment"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

migrate:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

dev:
	docker-compose up -d

prod:
	docker-compose -f docker-compose.prod.yml up -d --build

prod-down:
	docker-compose -f docker-compose.prod.yml down

prod-logs:
	docker-compose -f docker-compose.prod.yml logs -f
