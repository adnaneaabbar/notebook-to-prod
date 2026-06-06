#!/usr/bin/env bash
# Prépare l'environnement des démos. À lancer UNE fois, avant de commencer.
set -e
cd "$(dirname "$0")"

python3 -m venv .venv

# Sur certaines installs Ubuntu, le venv arrive sans pip (paquet python3-venv
# manquant). On le récupère proprement : ensurepip, sinon get-pip.py.
if ! ./.venv/bin/python -m pip --version >/dev/null 2>&1; then
  ./.venv/bin/python -m ensurepip --upgrade 2>/dev/null || {
    echo "pip absent du venv -> bootstrap via get-pip.py"
    curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
    ./.venv/bin/python /tmp/get-pip.py
  }
fi

./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt

# Entraîne et fige le modèle (crée model.pkl)
./.venv/bin/python train_model.py

echo ""
echo "Pret. Pour lancer les demos :"
echo "  source .venv/bin/activate"
echo "  uvicorn api:app --reload      # Demo 1 (FastAPI)  -> http://127.0.0.1:8000/docs"
echo "  docker build -t iris . && docker run -p 8000:8000 iris   # Demo 2 (Docker)"
echo "  python demo3_mlflow.py && mlflow ui                      # Demo 3 (MLflow)"
