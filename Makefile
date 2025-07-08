mig:
	alembic revision --autogenerate -m "Create a baseline migrations"
	alembic upgrade head

run:
	uvicorn main:app --reload