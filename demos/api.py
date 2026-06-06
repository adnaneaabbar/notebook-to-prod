# api.py — sert le modèle figé comme une API.
# DÉMO 1. Lancer :  uvicorn api:app --reload
# Puis ouvrir :     http://127.0.0.1:8000/docs
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="Iris en prod")
model = joblib.load("model.pkl")
CLASSES = ["setosa", "versicolor", "virginica"]


class Fleur(BaseModel):
    # 4 mesures d'une fleur (cm). /docs te donne un exemple pré-rempli.
    features: list[float] = [5.1, 3.5, 1.4, 0.2]


@app.get("/")
def home():
    return {"message": "Le modele est en ligne. Va sur /docs pour l'essayer."}


@app.post("/predict")
def predict(fleur: Fleur):
    i = int(model.predict([fleur.features])[0])
    return {"prediction": i, "espece": CLASSES[i]}
