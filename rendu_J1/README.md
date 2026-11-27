# Synora · 18. Intentions d'achat sur un site marchand

## Liens

| Livrable | Lien |
| --- | --- |
| Notebook Colab 1 · Données (J1, 25/11) | https://colab.research.google.com/drive/1WDsyqDsZlHAFGgUwjHlLMjeveNjFrwqY?usp=sharing (`notebooks/01_donnees.ipynb`, parties 1 et 2 seulement : ni modèle, ni score) |
| Notebook Colab 2 · Modèles (J2, fin S4) | À venir au jalon 2 |
| Notebook Colab 3 · Évaluation (J3, fin S5) | À venir au jalon 3 |
| Application Streamlit déployée | À venir au jalon 3 |
| Dépôt GitHub de l'application (`app.py`, `requirements.txt`, `model.joblib`) | À venir au jalon 3 |
| Journal IA | `JOURNAL_IA.md` (rendu avec ce fichier) |

## 1. Problème · cadrage (fin S2, validé en séance)

| Rubrique | Notre réponse |
| --- | --- |
| Utilisateur et décision | L'équipe marketing d'un site marchand. Pendant une visite, le modèle signale les sessions susceptibles de se terminer par un achat, pour décider à qui proposer une aide, une offre ou un rappel de panier. |
| Type de tâche | Classification binaire supervisée : la cible ne prend que deux valeurs. |
| Variable cible | `Revenue` : `True` si la session s'est terminée par un achat. Environ 15,5 % de `True` sur 12 330 sessions (classes déséquilibrées). |
| Variables exclues | Aucun identifiant dans le jeu. `PageValues` est testée **avec et sans** : elle est calculée à partir des transactions passées liées aux pages vues et n'est pas entièrement connue pendant la visite (risque de fuite). L'application utilise la version sans `PageValues`. |
| Métrique principale | F1 sur la classe « achat », avec le rappel et l'AUC en complément. L'erreur la plus coûteuse est de rater un futur acheteur (faux négatif), d'où l'importance du rappel ; trop de faux positifs gaspille les offres, d'où le F1. |
| Référence à battre | Classe majoritaire (« jamais d'achat ») : exactitude ≈ 84,5 % mais rappel et F1 nuls sur la classe « achat ». |
| Risques | Données d'un seul site sur une année, sans janvier ni avril : le modèle peut mal se comporter sur d'autres périodes ou d'autres sites. Pas de données personnelles directes, mais `Region` et le type de visiteur ne doivent pas servir à discriminer des clients (prix différenciés, par exemple). |

## 2. Données (J1)

- **Source** : Online Shoppers Purchasing Intention Dataset, UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset, licence CC BY 4.0
- **Taille** : 12 330 lignes × 18 colonnes ; cible : `Revenue`
- **Qualité** : aucune valeur manquante ; 125 lignes en double retirées avant le découpage ; mois `June` renommé `Jun` pour être cohérent avec les autres ; janvier et avril absents. Durées très étirées : médiane ≈ 10 min sur les pages produits, mais 867 sessions de plus d'1 h et un maximum ≈ 18 h (onglet probablement resté ouvert), conservées ; 6 sessions sans aucune page vue.
- **Préparation** (Pipeline ajusté sur l'entraînement seulement) :

| Colonnes | Traitement | Pourquoi |
| --- | --- | --- |
| `Administrative`, `Administrative_Duration`, `Informational`, `Informational_Duration`, `ProductRelated`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `SpecialDay` | `StandardScaler` | Échelles très différentes (secondes contre taux entre 0 et 0,2) |
| `Month`, `VisitorType`, `OperatingSystems`, `Browser`, `Region`, `TrafficType` ; `Weekend` | `OneHotEncoder(handle_unknown="ignore")` ; `Weekend` converti en 0 / 1 | Ce sont des catégories ; un code 8 n'est pas « plus grand » qu'un code 2 ; `Weekend` est déjà binaire |
| `PageValues` | retirée | Fuite repérée au cadrage : calculée à partir des transactions, donc pas vraiment connue pendant la visite |
| (identifiant) | aucune colonne à retirer | Le jeu n'a pas d'identifiant : chaque ligne est une session anonyme |

- **Découpage** : 20 % pour le test, `stratify` oui, `random_state` = 42 ; fait **avant** la préparation : 9 764 sessions d'entraînement, 2 441 de test, 72 colonnes après préparation
- **Conclusion** (bilan J1 du notebook) : les données viennent d'un seul site sur un an, sans valeur manquante, et sont déséquilibrées (15,5 % d'achats). Les acheteurs regardent plus de pages produits (29 contre 16 en médiane), y restent plus longtemps et quittent moins vite le site ; on achète surtout en fin d'année (25,4 % en novembre contre 1,6 % en février), et les nouveaux visiteurs achètent plus souvent (24,9 % contre 13,9 %). `PageValues` est très liée à l'achat mais c'est une fuite : elle est exclue de la préparation.

## 3. Résultats (J2 et J3)

À compléter aux jalons 2 et 3 : ce premier dépôt ne contient ni modèle ni score.

## 4. Limites et usages à éviter (J3)

À compléter au jalon 3.

## 5. Équipe

| Membre | Cadrage | J1 Données | J2 Modèles | J3 Évaluation et application |
| --- | --- | --- | --- | --- |
| Khaled Mnejja | Analyste données | Modélisateur | Évaluateur | Documentaliste |
| Omar Zouari | Documentaliste | Présentateur | Analyste données | Modélisateur |
| Omar Idriss | Modélisateur | Évaluateur | Documentaliste | Présentateur |
| Tawfik Zayen | Évaluateur | Documentaliste | Présentateur | Analyste données |
| Rayen Hsairi | Présentateur | Analyste données | Modélisateur | Évaluateur |

## Avant le rendu

- [ ] Section 1 remplie et validée en S2
- [ ] Les 3 notebooks s'exécutent de haut en bas sans erreur, sorties enregistrées (J1 : notebook 1 exécuté dans Colab, 0 erreur)
- [ ] Tous les liens s'ouvrent dans une fenêtre de navigation privée
- [ ] L'application s'ouvre, refuse les saisies absurdes et rappelle les limites du modèle
- [ ] Même version de scikit-learn dans `requirements.txt` et dans Colab
- [ ] `JOURNAL_IA.md` : au moins une erreur de l'IA détaillée et la critique d'un notebook public
- [x] Sources externes citées (notebooks Kaggle, dépôts GitHub, documentation)
- [ ] Lignes en italique et crochets supprimés
