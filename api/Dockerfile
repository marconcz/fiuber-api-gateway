FROM python:3.8-slim

WORKDIR /app

#OPCION 1: DEPENDENCIAS CON POETRY, PESA CASI 500MB -> LIMITE DE HEROKU 512MB
# RUN pip3 install poetry
# RUN poetry config virtualenvs.create false
# COPY pyproject.toml pyproject.toml
# RUN poetry install --no-interaction --no-ansi

#OPCION 2: EXPORTAR DEPENDENCIAS DE POETRY A REQUIREMENTS.TXT Y AHORRARNOS POETRY EN DOCKER
#CORRER ESTE COMANDO ANTES DE DOCKERIZAR: poetry export --without-hashes --format=requirements.txt > requirements2.txt
COPY requirements2.txt requirements.txt 
RUN pip3 install -r requirements.txt

EXPOSE 8000
EXPOSE 8501

COPY . .
CMD ["uvicorn", "manage:app", "--host","0.0.0.0", "--port","8000"]
