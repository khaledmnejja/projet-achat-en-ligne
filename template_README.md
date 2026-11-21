# [Nom de l'équipe] · [N° et titre du sujet]

> Modèle de README du projet Machine Learning, L3 GLSI, IIT Sfax, 2026-2027.
> Remplacez tout ce qui est entre crochets et supprimez les lignes en italique avant le rendu.
> Rendu final sur Moodle : **samedi 28/11, 08h00**, une seule fois par équipe.

## Liens

*Chaque notebook Colab est partagé en lecture : « Partager » → « Tous les utilisateurs disposant du lien » → Lecteur. Vérifiez chaque lien dans une fenêtre de navigation privée : un lien qui ne s'ouvre pas compte comme un livrable manquant.*

| Livrable | Lien |
| --- | --- |
| Notebook Colab 1 · Données (J1, 25/11) | [lien] |
| Notebook Colab 2 · Modèles (J2, fin S4) | [lien] |
| Notebook Colab 3 · Évaluation (J3, fin S5) | [lien] |
| Application Streamlit déployée | [lien Streamlit Community Cloud] |
| Dépôt GitHub de l'application (`app.py`, `requirements.txt`, `model.joblib`) | [lien] |
| Journal IA | `JOURNAL_IA.md` (rendu avec ce fichier) |
| Présentation (6 diapositives, PDF) | [nom du fichier] |

## 1. Problème · cadrage (fin S2, validé en séance)

| Rubrique | Notre réponse |
| --- | --- |
| Utilisateur et décision | *Qui utilise le modèle, pour décider quoi ?* |
| Type de tâche | *Classification, régression ou segmentation : c'est la forme de la cible qui décide.* |
| Variable cible | *Nom exact de la colonne, définition, répartition des classes ou des valeurs.* |
| Variables exclues | *Identifiants et variables connues trop tard (fuite de données), avec la raison pour chacune.* |
| Métrique principale | *Laquelle, et quelle erreur coûte le plus cher ?* |
| Référence à battre | *Score d'un modèle naïf : classe majoritaire (classification) ou moyenne (régression).* |
| Risques | *Biais possibles, données personnelles, usages à éviter.* |

## 2. Données (J1)

- **Source** : [nom du jeu de données et lien vers sa page officielle], [licence]
- **Taille** : [lignes] × [colonnes] ; cible : `[nom]`
- **Qualité** : [valeurs manquantes, valeurs aberrantes, doublons repérés]
- **Préparation** (Pipeline ajusté sur l'entraînement seulement) :

| Colonnes | Traitement | Pourquoi |
| --- | --- | --- |
| [numériques] | [ex. imputation par la médiane + StandardScaler] | |
| [catégorielles] | [ex. valeur la plus fréquente + OneHotEncoder] | |
| [exclues] | retirées | [identifiant / fuite] |

- **Découpage** : [part du test], `stratify` [oui / non], `random_state` = [valeur]

*Les données ne sont pas rendues : le notebook 1 les charge depuis leur page officielle ou un fichier téléversé.*

## 3. Résultats (J2 et J3)

| Modèle | [Métrique] en validation croisée (moyenne ± écart-type) | [Métrique] sur le test |
| --- | --- | --- |
| Référence naïve | | |
| [Modèle 1] | | |
| [Modèle 2] | | |
| [Modèle retenu, après GridSearchCV] | | |

**Modèle retenu** : [nom], parce que [raison liée à la métrique et à l'utilisateur].

**Principaux hyperparamètres** : [valeurs trouvées par GridSearchCV]

## 4. Limites et usages à éviter (J3)

- **Où le modèle se trompe le plus** (matrice de confusion ou résidus) :
- **Situations peu représentées dans les données** :
- **Usages à éviter** :
- **Données personnelles et variables sensibles** : [présentes ? comment traitées ?]

## 5. Équipe

*Équipes de 4 à 5. Les rôles tournent à chaque jalon ; chacun code au moins une partie (vérifié par l'historique des notebooks et la question individuelle de la soutenance).*

| Membre | Cadrage | J1 Données | J2 Modèles | J3 Évaluation et application |
| --- | --- | --- | --- | --- |
| [Nom] | [rôle] | [rôle] | [rôle] | [rôle] |
| | | | | |
| | | | | |
| | | | | |

## Avant le rendu

- [ ] Section 1 remplie et validée en S2
- [ ] Les 3 notebooks s'exécutent de haut en bas sans erreur, sorties enregistrées
- [ ] Tous les liens s'ouvrent dans une fenêtre de navigation privée
- [ ] L'application s'ouvre, refuse les saisies absurdes et rappelle les limites du modèle
- [ ] Même version de scikit-learn dans `requirements.txt` et dans Colab
- [ ] `JOURNAL_IA.md` : au moins une erreur de l'IA détaillée et la critique d'un notebook public
- [ ] Sources externes citées (notebooks Kaggle, dépôts GitHub, documentation)
- [ ] Lignes en italique et crochets supprimés
