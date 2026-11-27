# Journal IA

Machine Learning, L3 GLSI, IIT Sfax, 2026-2027. Un des cinq éléments à rendre, sous le nom `JOURNAL_IA.md`.

## Mode d'emploi

Le journal IA prouve que l'équipe sait ce qu'elle a demandé à l'IA, ce qu'elle a gardé et ce qu'elle a corrigé. Il compte pour 10 % de la note de projet (« Usage critique de l'IA »).

- **Où** : un fichier `JOURNAL_IA.md` rendu sur Moodle avec le README, les liens des notebooks Colab, le lien de l'application Streamlit et la présentation.
- **Qui** : chaque membre ajoute ses propres lignes et indique son nom ; le documentaliste vérifie le journal avant chaque jalon.
- **Quand** : au fil de l'eau, pas la veille du rendu. Une ligne par usage significatif (générer une fonction, expliquer une erreur, rédiger une partie du README), pas pour chaque autocomplétion.
- **Quoi** : tout assistant IA (chatbot, assistant de code de Colab ou de l'éditeur) et toute source externe reprise (notebook Kaggle, dépôt GitHub, forum).
- **Attendu minimum** : au moins une erreur de l'IA détectée et corrigée, décrite en détail, et la critique d'un notebook public.
- **Interdit** : envoyer des données personnelles à un assistant en ligne (loi organique 2004-63). Ne collez que des extraits de données publiques ou anonymisées.

## 1. Identification

| Champ | À remplir |
| --- | --- |
| Groupe | G1 |
| Nom de l'équipe | Synora |
| Sujet (n° et titre) | 18 · Intentions d'achat sur un site marchand |
| Membres | Khaled Mnejja (modélisateur), Omar Zouari (présentateur), Omar Idriss (évaluateur), Tawfik Zayen (documentaliste), Rayen Hsairi (analyste données) |
| Outils IA utilisés (nom et version si connue) | Claude Code (modèle Claude Opus 5.5). Toutes les sessions ont été menées par Khaled Mnejja, depuis le poste et le compte Google de Tawfik Zayen : les versions Colab enregistrées au nom de Tawfik par Claude ont été faites dans ces sessions. La colonne « Membre » du journal indique le membre responsable de l'étape (son rôle au jalon), qui a relu et validé la ligne et doit pouvoir l'expliquer. |
| Liens des notebooks Colab | J1 : https://colab.research.google.com/drive/1WDsyqDsZlHAFGgUwjHlLMjeveNjFrwqY?usp=sharing · J2 et J3 : à venir |

## 2. Journal

Une ligne par usage. Le prompt peut être résumé ; s'il est long, mettez le texte complet en annexe et indiquez son numéro. La colonne « Vérification » dit comment vous avez contrôlé le résultat (exécution, comparaison avec le cours, test sur un exemple).

| N° | Date | Membre | Jalon | Outil | Prompt (résumé) | Ce qui a été gardé | Vérification | Erreur détectée / correction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 21/11 | Khaled Mnejja | Cadrage | Claude (Claude Code) | « À partir du schéma des six étapes, génère une structure de projet conforme et fiable » | Arborescence, `ARCHITECTURE.md`, squelettes des 3 notebooks et de `app.py` | Notebook 1 exécuté de haut en bas dans Colab, découpage (9 764 / 2 441) et dimensions vérifiés ; notebooks 2 et 3 pas encore vérifiés | Fichiers des jalons suivants fournis sans provenir de notre exécution : à vérifier en J2 et J3 |
| 2 | 21/11 | Rayen Hsairi | J1 Données | Claude (Claude Code) | « Aide-nous à exécuter le notebook 1 et à rédiger les constats et le bilan J1 » | Brouillon des constats 1.6 et du bilan J1, chiffres sur les durées extrêmes, phrase de la section 2 du README | Chiffres recalculés et comparés aux sorties de notre exécution Colab (identiques) ; textes relus et reformulés en équipe | Brouillon reformulé en ligne 10, puis vérifié chiffre par chiffre en ligne 13 |
| 3 | 21/11 | Tawfik Zayen | Cadrage | Claude (Claude Code) | « Reprends le dépôt de notre coéquipier comme un nouveau projet pour l'équipe Synora, sans confusion avec un autre projet » | Copie des fichiers sans l'historique git, nom de l'équipe dans le README et le journal, `CLAUDE.md` qui délimite le projet, `.gitignore` (supports de cours exclus) | Liste des fichiers et historique git relus ; contenu comparé au dépôt GitHub d'origine et aux modèles du cours (`template_README.md`, `template_JOURNAL_IA.md`) | Aucune |
| 4 | 21/11 | Omar Idriss | Cadrage | Claude (Claude Code) | « Donne-nous tout ce que tu sais du projet, avec des critiques », puis « vérifie le projet par rapport à l'énoncé » | Liste des limites à discuter (`PageValues` connue trop tard, découpage aléatoire et non temporel, durées extrêmes, usage de `Region` et `VisitorType`) ; tableau de conformité à l'énoncé | Relecture de tout le code du projet ; versions de Colab lues dans la sortie de notre notebook 1 | Deux fichiers des jalons suivants, fournis par la structure générée en ligne 1, ne viennent pas de notre exécution : à refaire en J2 et J3 |
| 5 | 21/11 | Rayen Hsairi | J1 Données | Claude (Claude Code) | « Relis et critique le notebook 1 : est-il bien fait ? » | Critique : points forts (pas de fuite, pipeline) et manques (aucun graphique des valeurs aberrantes, doublons qui sont de vrais rebonds, durées nulles pour une page vue, modalités rares, `SpecialDay` limité à février et mai) | Chaque constat recalculé sur le CSV officiel (201 lignes en double, toutes des rebonds sans achat ; 717 sessions avec des pages produits mais une durée nulle) | La décision de retirer les doublons, prise dans la structure générée (ligne 1), est discutable : ce sont probablement de vraies visites distinctes. Décision gardée, mais à justifier dans le notebook |
| 6 | 21/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Ajoute au notebook 1 les cellules d'amélioration proposées dans la critique » | Sections 1.2 bis (profil des doublons), 1.2 ter (histogrammes log des durées, durées nulles), 1.5 bis (boîtes à moustaches acheteurs / non-acheteurs, corrélation de Spearman), 1.5 ter (`SpecialDay`, codes rares) ; justification du retrait des doublons en 2.1 | Copie du notebook exécutée de haut en bas sans erreur ; découpage inchangé (9 764 / 2 441) ; chiffres identiques à ceux de la critique (ligne 5) | Aucune ; le notebook doit être réimporté et réexécuté dans Colab pour que les sorties soient les nôtres |
| 7 | 21/11 | Tawfik Zayen | J1 Données | Claude (Claude Code) | « Vérifie le lien Colab du projet » | Constat : le lien est bien public, mais il ouvre un notebook de 2 cellules (chargement des données et `df.head()`), pas notre `01_donnees.ipynb` ; lien retiré du README et du journal en attendant le bon | Notebook téléchargé sans compte Google (comme un correcteur), cellules et sorties relues | Le lien avait été reporté dans le README (ligne du journal non numérotée, 21/11) sans en vérifier le contenu : corrigé |
| 8 | 21/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Fais toi-même les étapes Colab du notebook 1 » | Textes des cases 1.6 Constats et Bilan J1 rédigés dans le notebook à partir des sorties (doublons, durées, `PageValues`, profil des acheteurs, mois, codes rares) | Chaque chiffre repris des sorties de notre exécution du notebook ; relecture et reformulation : lignes 10 et 13 ; exécution dans Colab : ligne 9 | Aucune ; l'import dans Colab par Claude a échoué (navigateur non connecté), à faire par l'équipe |
| 9 | 21/11 | Tawfik Zayen | J1 Données | Claude (Claude Code) | « Vérifie le nouveau lien Colab du notebook 1 » | Lien vérifié puis reporté dans le README et le journal ; version exécutée dans Colab enregistrée dans `notebooks/01_donnees.ipynb` | Notebook téléchargé sans compte Google : 35 cellules, 18 cases exécutées dans l'ordre (1 à 18), 0 erreur, 5 graphiques ; chiffres de contrôle identiques (125 doublons, 12 205 lignes, 9 764 / 2 441, 72 / 73 colonnes) | Aucune |
| 10 | 21/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Relis et reformule les constats et le bilan J1 avec des mots simples » | Nouvelle version plus simple des cases 1.6 et Bilan J1 | Chaque chiffre comparé aux sorties de notre exécution Colab : tous présents, sauf les taux d'achat par mois et par type de visiteur, visibles seulement sur les graphiques | La première version (ligne 8) citait des taux (1,6 %, 25,4 %, 24,9 %, 13,9 %) qu'aucune cellule n'affiche : remplacés par une lecture des graphiques. version finale vérifiée en ligne 13 |
| 11 | 21/11 | Tawfik Zayen | Organisation | Claude (Claude Code) | « Je ne veux aucune confusion avec un autre dépôt GitHub présent sur ce PC » | Dépôt distant `origin` = notre dépôt du projet (compte précisé dans l'URL) ; identifiants GitHub séparés par dépôt ; garde-fou local (hook `pre-push`) qui refuse tout push vers un autre dépôt | Garde-fou testé : refus pour un autre dépôt, accord pour le nôtre ; `git remote -v` vérifié | Aucune |
| 12 | 25/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Corrige le projet par rapport aux séances S1 à S3 » | `notebooks/01_donnees.ipynb` : notebook Colab 1 du jalon 1 (parties 1 et 2 seulement), rôles de chaque jalon en tête des deux notebooks | Exécuté de haut en bas sans erreur (18 cellules de code) avec les versions de Colab ; recherche automatique : aucune cellule de code n'entraîne de modèle ni ne calcule de score | Le notebook unique déposé pour J1 contenait déjà modèles et scores, contraire à la consigne de S3 (« ni modèle, ni score ») : J1 a maintenant son propre notebook |
| 13 | 25/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Relis les constats 1.6 et le bilan J1 à notre place et corrige-les » | Constats 1.6 corrigés dans les deux notebooks : doublons décrits avec leur vraie médiane, sessions sans page vue ajoutées, explication des durées nulles présentée comme une hypothèse | Chaque chiffre de 1.6 et du bilan J1 comparé aux sorties de l'exécution Colab (1.2 bis, 1.2 ter, 1.3, 1.4, 1.5, 1.5 bis, 1.5 ter, 2.1, 2.2) : tous identiques | Deux affirmations allaient plus loin que les sorties : « une seule page vue, 0 seconde » pour tous les doublons (c'est la médiane, pas toutes les lignes) et l'explication des durées nulles par Google Analytics donnée comme un fait : corrigées. Rayen doit pouvoir expliquer ces constats à l'oral |
| 14 | 25/11 | Tawfik Zayen | J1 Données | Claude (Claude Code) | « Assure-toi que toutes les modifications sont faites dans Colab » | `notebooks/01_donnees.ipynb` importé dans Colab par Khaled avec le compte de Tawfik, exécuté en entier, enregistré avec ses sorties et partagé en lecture ; lien reporté dans le README et ci-dessus | Lien ouvert sans compte : 18 cellules de code sur 18 exécutées, 0 erreur, scikit-learn 1.6.1 | Aucune |
| 15 | 25/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Vérifie le notebook 1 point par point avec la consigne du jalon 1 » | Une phrase de lecture sous chacun des 5 graphiques, avec les chiffres affichés par la cellule (taux d'achat par mois et par type de visiteur, corrélations) ; tableau de description des 18 variables ; tableau des colonnes exclues (pas d'identifiant, `PageValues` exclue comme fuite, `Revenue` = cible) ; préparation sans `PageValues` ; conclusion reprise dans la section 2 du README | Notebook exécuté de haut en bas sans erreur avec les versions de Colab, puis dans Colab (Redémarrer la session et tout exécuter) ; chaque chiffre des phrases de lecture retrouvé dans une sortie ; recherche automatique : aucun modèle, aucun score | Trois écarts avec la consigne : les graphiques n'avaient pas chacun leur phrase, 1.6 citait la part de bonnes réponses d'une règle « jamais d'achat » (une exactitude, interdite au J1), et `PageValues` était préparée « avec et sans » alors que les colonnes de fuite doivent être exclues : corrigés |
| 16 | | | | | | | | |

## 3. Erreurs de l'IA détectées

Une fiche par erreur importante (au moins une). Numérotez-les E1, E2… et renvoyez-y depuis le tableau du journal.

### E1 — Constats J1 citant des chiffres qu'aucune sortie n'affiche

| Rubrique | À remplir |
| --- | --- |
| Ligne du journal | 8 (repérée en ligne 10, puis en ligne 13) |
| Ce que l'IA a proposé | Dans les constats 1.6 : des taux d'achat par mois et par type de visiteur (1,6 %, 25,4 %, 24,9 %, 13,9 %), « les doublons sont tous des rebonds : une seule page vue, 0 seconde », et « c'est normal, car Google Analytics… » pour les durées nulles |
| Pourquoi c'est faux | Un constat doit venir d'une sortie de notre notebook. Les quatre taux ne sont affichés par aucune cellule (ils ne se lisent que sur les graphiques) ; « 1 page, 0 s » est la médiane des 201 doublons, pas la valeur de chacun ; l'explication par Google Analytics est une hypothèse que les données ne prouvent pas |
| Comment vous l'avez repéré | Relecture : chaque chiffre de 1.6 et du bilan J1 comparé aux sorties des cellules 1.2 bis, 1.2 ter, 1.3, 1.4, 1.5, 1.5 bis, 1.5 ter, 2.1 et 2.2 |
| Correction apportée | Taux remplacés par une lecture des graphiques ; « le plus souvent des rebonds (médiane : 1 page, 0 s) » ; « sans doute une limite de Google Analytics » ; ajout des 6 sessions sans aucune page vue |
| Effet mesuré | Avant : 4 chiffres sans sortie correspondante et 2 affirmations trop fortes ; après : chaque chiffre de 1.6 et du bilan J1 se retrouve dans une sortie de l'exécution Colab |

## 4. Sources externes

Tout notebook, dépôt ou article dont vous avez repris une idée ou du code.

| N° | Source (lien) | Type | Ce qui a été repris | Où dans notre projet |
| --- | --- | --- | --- | --- |
| S1 | https://www.kaggle.com/code/annettecatherinepaul/online-shoppers-behavior-prediction | Notebook Kaggle | Aucun code repris : notebook lu et critiqué (ci-dessous) | `JOURNAL_IA.md`, critique d'un notebook public |
| S2 | https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset | Documentation (jeu de données, CC BY 4.0) | Le fichier CSV et la définition des variables, dont celle de `PageValues` | `01_donnees.ipynb`, partie 1 ; README, section 2 |
| S3 | https://scikit-learn.org/stable/user_guide.html | Documentation | Utilisation de `train_test_split`, `ColumnTransformer`, `Pipeline` | `01_donnees.ipynb`, partie 2 |

### Critique d'un notebook public (obligatoire)

- **Notebook choisi** : « Online Shoppers Behavior Prediction », https://www.kaggle.com/code/annettecatherinepaul/online-shoppers-behavior-prediction, auteur `annettecatherinepaul`, 312 votes (le plus voté du jeu sur Kaggle, consulté le 25/11/2026, écrit en R).
- **Ce qu'il fait bien** : l'exploration est complète et les codes (`Browser`, `Region`, `TrafficType`…) sont traités comme des catégories. Il reconnaît le déséquilibre des classes et regarde le rappel et le F1 plutôt que l'exactitude. Il découpe en 80 / 20 avant d'entraîner.
- **Erreur ou limite trouvée** : (1) métriques fausses : l'exactitude est divisée par la taille de l'entraînement, et le rappel et la précision sont inversés ; (2) le test n'est pas standardisé alors que l'entraînement l'est ; (3) `PageValues`, variable connue trop tard, est gardée sans discussion alors qu'elle domine l'arbre (importance 1 018, contre 103 pour la suivante) ; (4) l'auteur compare l'exactitude (87 %) au F1 (67 %) du même test et parle de « surapprentissage ».
- **Preuve** : cellule `In [14]` : `Accuracy <- (x[4] + x[1]) / (nrow(train))` et `TPR_Recall <- x[4] / (x[2] + x[4])`, où `x[2]` est un faux positif ; cellule `In [12]` : `scale` appliqué à `sample_train` seulement. À partir de la matrice de `In [15]` (1 838 / 67 / 246 / 314), le rappel est 314 / 381 = **0,824** (affiché 0,561), la précision 314 / 560 = **0,561** (affichée 0,824) et l'exactitude 0,873 (affichée 0,218).
- **Ce que nous avons fait différemment** : la préparation est dans un `Pipeline` appris sur l'entraînement seulement, puis appliqué tel quel au test. `PageValues` est signalée dès la partie 1.5 comme variable connue trop tard : elle sera testée avec et sans aux jalons suivants.

## 5. Bilan de l'équipe

À rédiger pour le rendu final.

### Avant chaque dépôt

- [ ] Chaque membre a au moins une ligne dans le journal
- [x] Au moins une erreur de l'IA est décrite en détail (section 3)
- [x] Toutes les sources externes sont listées (section 4)
- [x] La critique d'un notebook public est rédigée (rendu final)
- [x] Aucune donnée personnelle n'a été envoyée à un assistant
- [ ] Chaque membre peut expliquer chaque ligne de code reprise d'une IA
- [x] Les lignes d'exemple du modèle sont supprimées
