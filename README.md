# Du notebook à la production 🚀

Le repo compagnon du workshop **« Du notebook à la production — à quoi ressemblent les vrais jobs ML »**.

Tu sais entraîner un modèle dans un notebook. Ici, tu vas le faire **sortir** du notebook :
le figer, le servir comme une API, l'emballer dans un container, et tracer tes expériences.
Trois petites démos, courtes et exécutables, qui montrent ce que les entreprises attendent vraiment.

---

## Ce que tu vas apprendre

| Démo | Outil | L'idée |
|------|-------|--------|
| 1 | **FastAPI** | Transformer un modèle figé en API que n'importe qui peut appeler |
| 2 | **Docker** | Emballer cette API pour qu'elle tourne **partout** à l'identique |
| 3 | **MLflow** | Garder la trace de chaque entraînement : params, score, modèle |

---

## Prérequis

- **Python 3.10+**
- **Docker** (optionnel — uniquement pour la démo 2)
- Un terminal, et l'envie de casser le mythe « ça marche chez moi »

---

## Installation (une seule fois)

```bash
cd demos
bash setup.sh
```

`setup.sh` crée un environnement virtuel, installe les dépendances et entraîne le modèle
(`model.pkl`). Le script gère même le cas où `venv` arrive sans `pip` sur certaines installs Ubuntu.

<details>
<summary>Installation manuelle (si tu préfères)</summary>

```bash
cd demos
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python train_model.py        # crée model.pkl
```
</details>

---

## Démo 1 — FastAPI : ton modèle devient une URL

```bash
cd demos
source .venv/bin/activate
uvicorn api:app --reload
```

Ouvre **http://127.0.0.1:8000/docs** → `POST /predict` → **Try it out** → **Execute**.

Ou en ligne de commande :

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6.3, 3.3, 6.0, 2.5]}'
# -> {"prediction": 2, "espece": "virginica"}
```

**À observer :** tu envoies 4 chiffres, tu reçois une prédiction en JSON. Le modèle a quitté le
notebook — n'importe quelle app web ou mobile peut maintenant l'appeler. Ça tient en ~15 lignes
([`api.py`](demos/api.py)).

> **Essaie toi-même :** change les `features` et regarde l'espèce prédite changer.

---

## Démo 2 — Docker : « ça marche chez moi » → ça marche partout

```bash
cd demos
docker build -t iris .
docker run -p 8000:8000 iris
```

Reteste la même URL : **http://127.0.0.1:8000/docs**. L'API repart — mais cette fois dans un
container isolé, avec sa propre version de Python et ses librairies figées.

**À observer :** ton code, tes dépendances et un mini-OS partent dans une boîte étanche. Tu peux
l'envoyer à un collègue ou la déployer sur un serveur cloud : elle tournera **à l'identique**.

> Pas de Docker installé ? Lis quand même le [`Dockerfile`](demos/Dockerfile) : 8 lignes suffisent
> à rendre ton API déployable n'importe où.

---

## Démo 3 — MLflow : quel modèle tourne, et pourquoi ?

```bash
cd demos
source .venv/bin/activate
python demo3_mlflow.py
mlflow ui        # -> http://127.0.0.1:5000
```

Le script entraîne 3 versions du modèle avec des hyperparamètres différents et logge chaque run.

**À observer :** dans l'UI MLflow, chaque ligne du tableau est un entraînement, avec ses
paramètres, son score et le modèle lui-même, horodaté. En entreprise on entraîne des centaines de
modèles — sans tracking, impossible de dire lequel tourne en prod. MLflow, c'est le carnet de labo
de tes modèles.

> **Essaie toi-même :** ajoute une valeur dans la liste `[10, 50, 200]` de
> [`demo3_mlflow.py`](demos/demo3_mlflow.py), relance, et compare les runs.

---

## Structure du repo

```
.
├── du-notebook-a-la-prod.pptx   # Les slides du workshop
├── build_slides.py              # Le générateur du deck (bonus, pour voir comment il est fait)
└── demos/
    ├── setup.sh                 # Installe tout + entraîne le modèle (à lancer une fois)
    ├── train_model.py           # Entraîne et fige le modèle dans model.pkl
    ├── api.py                   # Démo 1 — sert le modèle via FastAPI
    ├── Dockerfile               # Démo 2 — emballe l'API dans un container
    ├── demo3_mlflow.py          # Démo 3 — tracke plusieurs entraînements
    └── requirements.txt
```

---

## Pour aller plus loin

Le vrai apprentissage commence quand tu le refais avec **ton** modèle :

1. Reprends un de tes notebooks Kaggle et **fige** ton modèle dans un `.pkl`.
2. Sers-le derrière une route FastAPI `POST /predict`.
3. Emballe le tout dans un `Dockerfile` et lance-le en container.

Si tu arrives au bout des 3, tu as fait ce que beaucoup de juniors n'ont jamais fait : tu as mis
un modèle **en production**. 🎯
