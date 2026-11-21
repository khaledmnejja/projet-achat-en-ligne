# Application · Intention d'achat (étape 6 · déploiement)

Ce dossier devient le dépôt GitHub déployé sur Streamlit Community Cloud.

| Fichier | Origine |
| --- | --- |
| `app.py` | Interface : saisie d'une session, validation, prédiction, rappel des limites |
| `model.joblib` | Produit par le notebook 3 (section 4) **dans Colab** |
| `requirements.txt` | Produit par le même cellule : versions exactes de Colab |

## Mettre à jour le modèle

1. Exécuter `03_evaluation.ipynb` dans Colab jusqu'au bout.
2. Remplacer ici `model.joblib` **et** `requirements.txt` par les fichiers téléchargés.
3. `git add`, `git commit`, `git push` : Streamlit Cloud redéploie tout seul.

Les deux fichiers vont toujours ensemble : un modèle enregistré avec une version de scikit-learn
peut refuser de se charger avec une autre.

## Lancer en local

```
pip install -r requirements.txt
streamlit run app.py
```
