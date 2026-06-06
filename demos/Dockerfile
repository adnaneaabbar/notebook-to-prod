# Dockerfile — DÉMO 2 : emballer l'API dans un container.
# Le modèle (model.pkl) doit déjà exister : lance train_model.py avant.
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl api.py ./

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
