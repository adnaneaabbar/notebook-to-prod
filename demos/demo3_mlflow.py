# demo3_mlflow.py — DÉMO 3 : tracker plusieurs entraînements.
# Lancer :  python demo3_mlflow.py
# Puis :    mlflow ui   ->  http://127.0.0.1:5000
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import mlflow, mlflow.sklearn

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

mlflow.set_experiment("iris-prod")

# On entraîne 3 versions avec des hyperparamètres différents.
# MLflow garde la trace de CHAQUE run : params + score + le modèle lui-même.
for n in [10, 50, 200]:
    with mlflow.start_run(run_name=f"rf_{n}arbres"):
        m = RandomForestClassifier(n_estimators=n, random_state=0).fit(Xtr, ytr)
        acc = m.score(Xte, yte)
        mlflow.log_param("n_estimators", n)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(m, name="model")
        print(f"  n_estimators={n:>3}  ->  accuracy={acc:.3f}  (logge dans MLflow)")

print("\nOK. Lance maintenant :  mlflow ui   puis ouvre http://127.0.0.1:5000")
