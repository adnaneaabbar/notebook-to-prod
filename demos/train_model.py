# train_model.py — entraîne un modèle et le FIGE dans un fichier.
# Le déclic : on n'entraîne plus à chaque fois, on charge un .pkl prêt à l'emploi.
#
# Lancer :  python train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

X, y = load_iris(return_X_y=True)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(X, y)

joblib.dump(model, "model.pkl")
print("OK -> model.pkl  (accuracy train: %.3f)" % model.score(X, y))
print("Le modele est fige. Plus besoin du notebook pour s'en servir.")
