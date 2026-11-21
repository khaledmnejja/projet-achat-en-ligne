# Architecture du projet · Sujet 18, intentions d'achat sur un site marchand

Ce document relie les **six étapes du cycle de vie d'un modèle** (cours S1) aux fichiers du projet.
Il sert de carte : chaque étape a un endroit précis, et chaque fichier sait d'où viennent ses entrées.

## 1. Les six étapes, fichier par fichier

| Étape | Rôle | Fichier | Jalon | Sortie |
| --- | --- | --- | --- | --- |
| 1 · Collecte | Charger les données depuis la page officielle UCI, contrôler la qualité | `notebooks/synora_projet_ml.ipynb` (partie 1) | J1 · 25/11 | DataFrame propre, constats qualité |
| 2 · Préparation | Nettoyer, encoder, normaliser, **séparer train / test avant toute préparation** | `notebooks/synora_projet_ml.ipynb` (partie 2) | J1 · 25/11 | `ColumnTransformer` ajusté sur le train seul |
| 3 · Modèle | Choisir les algorithmes candidats et une référence naïve | `notebooks/synora_projet_ml.ipynb` (partie 3) | J2 · fin S4 | Liste de `Pipeline` candidats |
| 4 · Entraînement | Validation croisée stratifiée, avec et sans `PageValues`, puis `GridSearchCV` | `notebooks/synora_projet_ml.ipynb` (partie 4) | J2 · fin S4 | Tableau des scores, meilleurs hyperparamètres |
| 5 · Évaluation | Mesurer **une seule fois** sur le test, choisir le seuil, analyser les erreurs | `notebooks/synora_projet_ml.ipynb` (parties 5 et 6.1) | J3 · fin S5 | Matrice de confusion, rapport, `model.joblib` |
| 6 · Déploiement | Servir le modèle, refuser les saisies absurdes, rappeler les limites | `app/app.py` + `app/requirements.txt` + `app/model.joblib` | J3 · fin S5 | Application Streamlit Community Cloud |

La boucle de retour du schéma (« une mauvaise évaluation renvoie à la préparation ») est possible
parce que tout le projet est dans **un seul notebook** : un même découpage, une seule cellule de configuration, et la partie 5 reprend automatiquement les réglages de la partie 4 (`BEST = best`).

## 2. Arborescence

```
synora_achat_en_ligne/
├── ARCHITECTURE.md          ← ce document
├── README.md                ← livrable (modèle du cours, section 1 pré-remplie)
├── JOURNAL_IA.md            ← livrable (10 % de la note)
├── .gitignore               ← exclut data/ et les fichiers temporaires
├── data/                    ← copie locale du CSV, jamais rendue ni poussée sur GitHub
├── notebooks/
│   └── synora_projet_ml.ipynb  ← notebook unique : parties 1 à 6 (étapes 1 à 6, J1 à J3)
├── app/                     ← étape 6, c'est ce dossier qui devient le dépôt GitHub
│   ├── app.py
│   ├── requirements.txt     ← régénéré par la partie 6 du notebook avec les versions exactes de Colab
│   └── model.joblib         ← produit par la partie 6 du notebook
└── presentation/            ← 6 diapositives (PDF)
```

## 3. Règles de fiabilité appliquées partout

1. **Une seule configuration.** Le notebook commence par une cellule `CONFIG` unique : graine, taille du test, listes de colonnes.
2. **Doublons retirés avant le découpage.** Sinon une même session peut se retrouver à la fois dans le train et dans le test (fuite).
3. **Découpage avant préparation.** `train_test_split(..., stratify=y)` d'abord ; le `ColumnTransformer` n'est ajusté que sur le train,
   et toujours à l'intérieur d'un `Pipeline` pour que la validation croisée le réajuste à chaque pli.
4. **Les codes sont des catégories.** `Month`, `VisitorType`, `OperatingSystems`, `Browser`, `Region` et `TrafficType`
   passent par `OneHotEncoder(handle_unknown="ignore")`, jamais par `StandardScaler`.
5. **Le test ne sert qu'une fois.** Choix du modèle, des hyperparamètres et du seuil : uniquement en validation croisée sur le train.
6. **Classes déséquilibrées (≈ 15 % d'achats).** Métriques : rappel et F1 sur la classe « achat », AUC.
   Les modèles utilisent `class_weight="balanced"` ; l'exactitude seule n'est jamais utilisée pour décider.
7. **`PageValues` en question.** Chaque modèle est évalué avec et sans cette variable ;
   l'application utilise par défaut la version **sans** `PageValues`, la seule entièrement connue pendant la visite.
8. **Mêmes versions en Colab et en production.** La partie 6 du notebook écrit `requirements.txt` avec les versions installées dans Colab.

## 4. Flux de données

```
UCI (CSV officiel)
   │  parties 1-2 · charger, contrôler, dédoublonner
   ▼
DataFrame propre ──► train_test_split(stratify, random_state=42)
                          │                     │
                        train (80 %)          test (20 %, mis de côté)
                          │                     │
   parties 3-4 · CV 5 plis, GridSearchCV        │
                          │                     │
   partie 5 · seuil choisi en CV sur le train ──┤ évaluation unique
                          │                     ▼
                     model.joblib  ──►  app/app.py (Streamlit)
```
