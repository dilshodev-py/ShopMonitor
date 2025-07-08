mig:
	alembic revision --autogenerate -m "Create a baseline migrations"
	alembic upgrade head

admin:
	uvicorn web.app:app --host localhost --port 8005