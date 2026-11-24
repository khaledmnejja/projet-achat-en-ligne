# Synora · 18. Intentions d'achat sur un site marchand

> Modèle de README du projet Machine Learning, L3 GLSI, IIT Sfax, 2026-2027.
> Remplacez tout ce qui est entre crochets et supprimez les lignes en italique avant le rendu.
> Rendu final sur Moodle : **samedi 28/11, 08h00**, une seule fois par équipe.

*L'organisation des fichiers et le lien entre les six étapes et les parties du notebook unique sont décrits dans `ARCHITECTURE.md`.*

## Liens

*Choix de l'équipe : tout le code est dans **un seul notebook Colab** (`synora_projet_ml.ipynb`), une partie par étape ; les trois lignes ci-dessous pointent vers ce même notebook. Pour garder ce lien, remplacer le contenu de `lucia.ipynb` dans Drive (clic droit → Gérer les versions → Importer une nouvelle version).*

*Le notebook Colab est partagé en lecture : « Partager » → « Tous les utilisateurs disposant du lien » → Lecteur. Vérifiez chaque lien dans une fenêtre de navigation privée : un lien qui ne s'ouvre pas compte comme un livrable manquant.*

| Livrable | Lien |
| --- | --- |
| Notebook Colab · parties 1-2, Données (J1, 25/11) | https://colab.research.google.com/drive/1LiB1IPa35JmYHIGbi2EDKlJWYfQkG3AR?usp=sharing |
| Notebook Colab · parties 3-4, Modèles (J2, fin S4) | https://colab.research.google.com/drive/1LiB1IPa35JmYHIGbi2EDKlJWYfQkG3AR?usp=sharing (même notebook, parties 3 et 4) |
| Notebook Colab · parties 5-6, Évaluation et export (J3, fin S5) | https://colab.research.google.com/drive/1LiB1IPa35JmYHIGbi2EDKlJWYfQkG3AR?usp=sharing (même notebook, parties 5 et 6) |
| Application Streamlit déployée | [lien Streamlit Community Cloud] |
| Dépôt GitHub de l'application (`app.py`, `requirements.txt`, `model.joblib`) | [lien] |
| Journal IA | `JOURNAL_IA.md` (rendu avec ce fichier) |
| Présentation (6 diapositives, PDF) | [nom du fichier] |

## 1. Problème · cadrage (fin S2, validé en séance)

*Proposition de cadrage à relire et valider en équipe.*

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
| `Month`, `VisitorType`, `OperatingSystems`, `Browser`, `Region`, `TrafficType` | `OneHotEncoder(handle_unknown="ignore")` | Ce sont des catégories ; un code 8 n'est pas « plus grand » qu'un code 2 |
| `Weekend` | converti en 0 / 1 | Déjà binaire |
| `PageValues` (variante « sans ») | retirée | Fuite possible : calculée à partir des transactions |

- **Découpage** : 20 % pour le test, `stratify` oui, `random_state` = 42

*Les données ne sont pas rendues : le notebook les charge depuis leur page officielle ou un fichier téléversé.*

## 3. Résultats (J2 et J3)

| Modèle | F1 « achat » en validation croisée (moyenne ± écart-type) | F1 « achat » sur le test |
| --- | --- | --- |
| Référence naïve | | |
| Régression logistique | | |
| Forêt aléatoire | | |
| [Modèle retenu, après GridSearchCV] | | |

*Ajouter une ligne par variante (avec / sans `PageValues`) pour montrer l'écart.*

**Modèle retenu** : [nom], parce que [raison liée à la métrique et à l'utilisateur].

**Principaux hyperparamètres** : [valeurs trouvées par GridSearchCV]

**Seuil de décision** : [valeur], choisi en validation croisée sur l'entraînement (pas sur le test).

## 4. Limites et usages à éviter (J3)

- **Où le modèle se trompe le plus** (matrice de confusion ou résidus) :
- **Situations peu représentées dans les données** : janvier et avril absents, visiteurs de type `Other` (85 sessions)
- **Usages à éviter** :
- **Données personnelles et variables sensibles** : [présentes ? comment traitées ?]

### Suivi et réentraînement après la mise en service (étape 6)

*Détail et code : notebook, parties 6.2 et 6.3.*

| Quoi | Comment | Alerte si |
| --- | --- | --- |
| Entrées | PSI de chaque variable numérique (sauf `SpecialDay`, qui dépend du mois), catégories jamais vues, valeurs hors bornes, par lot mensuel | PSI > 0,25 ou plus de 5 % de sessions avec une catégorie inconnue (lots d'au moins 100 sessions) |
| Sorties | Part de sessions annoncées « achat » | Pas d'alerte automatique : comparée à la part d'achats réels dès qu'elle est connue |
| Qualité | Rappel et F1 du lot, dès que les achats sont connus | Rappel inférieur de plus de 10 points à celui du test (lots d'au moins 20 achats) |

**Réentraînement** : après deux alertes de suite, et au moins une fois par saison. On ajoute les nouvelles sessions et on repart de l'étape 2, avec la même configuration et un seuil rechoisi en validation croisée. Le nouveau modèle ne remplace l'ancien que s'il obtient un meilleur F1 sur les sessions les plus récentes ; l'ancien `model.joblib` est gardé pour revenir en arrière.

## 5. Équipe

*Équipes de 4 à 5. Les rôles tournent à chaque jalon ; chacun code au moins une partie (vérifié par l'historique des notebooks et la question individuelle de la soutenance).*

| Membre | Cadrage | J1 Données | J2 Modèles | J3 Évaluation et application |
| --- | --- | --- | --- | --- |
| Khaled Mnejja | [rôle] | Modélisateur | [rôle] | [rôle] |
| Omar Zouari | [rôle] | Présentateur | [rôle] | [rôle] |
| Omar Idriss | [rôle] | Évaluateur | [rôle] | [rôle] |
| Tawfik Zayen | [rôle] | Documentaliste | [rôle] | [rôle] |
| Rayen Hsairi | [rôle] | Analyste données | [rôle] | [rôle] |

## Avant le rendu

- [ ] Section 1 remplie et validée en S2
- [ ] Le notebook s'exécute de haut en bas sans erreur, sorties enregistrées
- [ ] Tous les liens s'ouvrent dans une fenêtre de navigation privée
- [ ] L'application s'ouvre, refuse les saisies absurdes et rappelle les limites du modèle
- [ ] Même version de scikit-learn dans `requirements.txt` et dans Colab
- [ ] `JOURNAL_IA.md` : au moins une erreur de l'IA détaillée et la critique d'un notebook public
- [ ] Sources externes citées (notebooks Kaggle, dépôts GitHub, documentation)
- [ ] Lignes en italique et crochets supprimés
