# Synora · 18. Intentions d'achat sur un site marchand

## Liens

| Livrable | Lien |
| --- | --- |
| Notebook Colab 1 · Données (J1, 25/11) | https://colab.research.google.com/drive/1yGfFigA1Fn-iRtjC4A7rh-N4dAzHyhJs?usp=sharing (notebook unique `synora_projet_ml.ipynb`, parties 1 et 2) |
| Notebook Colab 2 · Modèles (J2, fin S4) | https://colab.research.google.com/drive/1yGfFigA1Fn-iRtjC4A7rh-N4dAzHyhJs?usp=sharing (notebook unique `synora_projet_ml.ipynb`, parties 3 et 4) |
| Notebook Colab 3 · Évaluation (J3, fin S5) | https://colab.research.google.com/drive/1yGfFigA1Fn-iRtjC4A7rh-N4dAzHyhJs?usp=sharing (notebook unique `synora_projet_ml.ipynb`, parties 5 et 6) |
| Application Streamlit déployée | https://synora-achat.streamlit.app (Streamlit Community Cloud, Python 3.12, fichier `app/app.py`) |
| Dépôt GitHub de l'application (`app.py`, `requirements.txt`, `model.joblib`) | https://github.com/khaledmnejja/projet-achat-en-ligne (dossier `app/`) |
| Journal IA | `JOURNAL_IA.md` (rendu avec ce fichier) |
| Présentation (6 diapositives, PDF) | `presentation/synora_presentation.pdf` (source modifiable : `presentation/presentation.html`) |

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
| `Administrative`, `Administrative_Duration`, `Informational`, `Informational_Duration`, `ProductRelated`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `SpecialDay` (+ `PageValues` dans la variante « avec ») | `StandardScaler` | Échelles très différentes (secondes contre taux entre 0 et 0,2) |
| `Month`, `VisitorType`, `OperatingSystems`, `Browser`, `Region`, `TrafficType` ; `Weekend` | `OneHotEncoder(handle_unknown="ignore")` ; `Weekend` converti en 0 / 1 | Ce sont des catégories ; un code 8 n'est pas « plus grand » qu'un code 2 ; `Weekend` est déjà binaire |
| `PageValues` (variante « sans ») | retirée | Fuite possible : calculée à partir des transactions |

- **Découpage** : 20 % pour le test, `stratify` oui, `random_state` = 42

## 3. Résultats (J2 et J3)

| Modèle | F1 « achat » en validation croisée (moyenne ± écart-type) | F1 « achat » sur le test |
| --- | --- | --- |
| Référence naïve | sans `PageValues` : 0,000 ± 0,000 · avec : 0,000 ± 0,000 | 0,000 (ne prédit jamais « achat ») |
| Régression logistique | sans : 0,392 ± 0,011 · avec : 0,606 ± 0,024 | non mesuré : le test ne sert qu'une fois, aux modèles retenus |
| Forêt aléatoire | sans : 0,138 ± 0,032 (0,414 à son meilleur seuil) · avec : 0,614 ± 0,016 (0,690 à son meilleur seuil, retenue pour la variante « avec ») | avec `PageValues`, seuil 0,323 : 0,683 (rappel 0,736, AUC 0,925) |
| Gradient boosting, retenu après GridSearchCV | sans : 0,411 ± 0,009 (0,418 à son meilleur seuil ; 0,425 après réglage et choix du seuil) · avec : 0,669 ± 0,015 | sans `PageValues`, seuil 0,593 : **0,443** (rappel 0,599, précision 0,35, AUC 0,785) |

**Modèle retenu** : gradient boosting (`HistGradientBoostingClassifier`) sans `PageValues`, parce que c'est le meilleur F1 « achat » parmi les modèles qui n'utilisent que des informations connues pendant la visite : sur le test, il détecte 60 % des acheteurs (la référence n'en trouve aucun), ce qui répond au besoin de l'équipe marketing de ne pas rater les futurs acheteurs. La variante avec `PageValues` fait mieux (F1 0,683), mais grâce à une variable calculée à partir des achats. Quand tous les modèles sont réglés (contrôle 4.3 bis), la forêt aléatoire sans `PageValues` fait jeu égal (précision moyenne 0,393 contre 0,388, écart plus petit que l'écart-type entre plis) : le choix tient.

**Principaux hyperparamètres** : `learning_rate = 0.05`, `max_depth = 6`, `class_weight = "balanced"` ; seuil de décision 0,593, choisi en validation croisée sur l'entraînement (pas sur le test) pour maximiser le F1 : un seuil plus bas trouverait plus d'acheteurs, mais avec encore plus d'offres envoyées pour rien

## 4. Limites et usages à éviter (J3)

- **Où le modèle se trompe le plus** (matrice de confusion ou résidus) : sur 382 acheteurs du test, il en rate 153 (rappel 0,599) et donne 422 fausses alertes (précision 0,352), d'après la matrice de confusion (notebook, 5.2). Il rate surtout les visiteurs réguliers (rappel 0,540, contre 0,773 pour les nouveaux visiteurs) et les acheteurs des mois creux (août 0,357, mai 0,443, contre 0,752 en novembre). Sur un mois jamais vu à l'entraînement (notebook, 5.3 bis), le F1 tombe à 0,334 : le score du test est optimiste pour une nouvelle période.
- **Situations peu représentées dans les données** : janvier et avril absents, visiteurs de type `Other` (85 sessions) ; dans le test, juin, juillet, août, septembre et octobre ont chacun moins de 20 acheteurs, donc leurs scores sont fragiles. Le modèle apprend sur des sessions terminées, alors qu'il est utilisé pendant la visite, quand les pages vues et les durées sont encore incomplètes.
- **Usages à éviter** : décider automatiquement à la place d'une personne (le modèle aide à cibler une offre, il ne refuse rien à un client) ; fixer des prix différents selon la région ou le type de visiteur ; l'utiliser sur un autre site ou une autre période sans le réentraîner ; utiliser en direct la version avec `PageValues`.
- **Données personnelles et variables sensibles** : aucune donnée personnelle directe (ni nom, ni identifiant, ni adresse) ; `Region`, `Browser`, `OperatingSystems` et `TrafficType` sont des codes anonymes. `Region` et `VisitorType` restent des entrées du modèle mais ne doivent pas servir à traiter les clients différemment. Rappel par région vérifié (notebook, 5.3) : de 0,548 à 0,635 pour les régions d'au moins 30 acheteurs, sans écart net. Données publiques (licence CC BY 4.0).

## 5. Équipe

| Membre | Cadrage | J1 Données | J2 Modèles | J3 Évaluation et application |
| --- | --- | --- | --- | --- |
| Khaled Mnejja | Analyste données | Modélisateur | Évaluateur | Documentaliste |
| Omar Zouari | Documentaliste | Présentateur | Analyste données | Modélisateur |
| Omar Idriss | Modélisateur | Évaluateur | Documentaliste | Présentateur |
| Tawfik Zayen | Évaluateur | Documentaliste | Présentateur | Analyste données |
| Rayen Hsairi | Présentateur | Analyste données | Modélisateur | Évaluateur |

## Avant le rendu

- [x] Section 1 remplie et validée en S2
- [x] Les 3 notebooks s'exécutent de haut en bas sans erreur, sorties enregistrées
- [x] Tous les liens s'ouvrent dans une fenêtre de navigation privée
- [x] L'application s'ouvre, refuse les saisies absurdes et rappelle les limites du modèle
- [x] Même version de scikit-learn dans `requirements.txt` et dans Colab
- [x] `JOURNAL_IA.md` : au moins une erreur de l'IA détaillée et la critique d'un notebook public
- [x] Sources externes citées (notebooks Kaggle, dépôts GitHub, documentation)
- [x] Lignes en italique et crochets supprimés
