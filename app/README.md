# Application · Intention d'achat (étape 6 · déploiement)

Ce dossier devient le dépôt GitHub déployé sur Streamlit Community Cloud.

| Fichier | Origine |
| --- | --- |
| `app.py` | Interface : saisie d'une session, validation, prédiction, rappel des limites |
| `model.joblib` | Produit par la partie 6 de `synora_projet_ml.ipynb` **dans Colab** |
| `requirements.txt` | Produit par le même cellule : versions exactes de Colab |

## Mettre à jour le modèle

1. Exécuter `synora_projet_ml.ipynb` dans Colab jusqu'au bout.
2. Remplacer ici `model.joblib` **et** `requirements.txt` par les fichiers téléchargés.
3. `git add`, `git commit`, `git push` : Streamlit Cloud redéploie tout seul.

Les deux fichiers vont toujours ensemble : un modèle enregistré avec une version de scikit-learn
peut refuser de se charger avec une autre.

## Lancer en local

```
pip install -r requirements.txt
streamlit run app.py
```

## Tester

```
pip install pytest
python -m pytest test_app.py
```

Six tests : modèle cohérent (variante sans `PageValues`), limites lues dans `model.joblib`, session sans page refusée, durée sans page refusée, saisies normales qui donnent une probabilité.
