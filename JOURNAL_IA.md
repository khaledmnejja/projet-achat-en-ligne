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
| Groupe | G1 / G2 |
| Nom de l'équipe | Synora |
| Sujet (n° et titre) | 18 · Intentions d'achat sur un site marchand |
| Membres | Khaled Mnejja (modélisateur), Omar Zouari (présentateur), Omar Idriss (évaluateur), Tawfik Zayen (documentaliste), Rayen Hsairi (analyste données) |
| Outils IA utilisés (nom et version si connue) | Claude Code (modèle Claude Opus 5.5) |
| Liens des notebooks Colab | https://colab.research.google.com/drive/1HTMnvKr9NkoFk7ZmI2E4jtd99rfjie32?usp=sharing (notebook unique : parties 1-2 pour J1, 3-4 pour J2, 5-6 pour J3) |

## 2. Journal

Une ligne par usage. Le prompt peut être résumé ; s'il est long, mettez le texte complet en annexe et indiquez son numéro. La colonne « Vérification » dit comment vous avez contrôlé le résultat (exécution, comparaison avec le cours, test sur un exemple).

| N° | Date | Membre | Jalon | Outil | Prompt (résumé) | Ce qui a été gardé | Vérification | Erreur détectée / correction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 20/11 | Exemple : Amira | J1 Données | Assistant de code Colab | « Écris un pipeline qui encode les colonnes catégorielles et normalise les numériques » | Structure du `ColumnTransformer` | Exécuté sur le train, dimensions vérifiées | Le `fit` était fait sur tout le jeu avant le découpage (fuite) : découpage déplacé avant le pipeline (voir E1) |
| 2 | 22/11 | Exemple : Youssef | J1 Données | Chatbot | « Explique la différence entre OneHotEncoder et OrdinalEncoder » | Explication reformulée dans le notebook | Comparée au support de S2 | Aucune |
| 3 | 21/11 | Khaled Mnejja | Cadrage | Claude (Claude Code) | « À partir du schéma des six étapes, génère une structure de projet conforme et fiable » | Arborescence, `ARCHITECTURE.md`, squelettes des 3 notebooks et de `app.py` | Notebook 1 exécuté de haut en bas dans Colab, découpage (9 764 / 2 441) et dimensions vérifiés ; notebooks 2 et 3 pas encore vérifiés | Fichiers et chiffres fournis sans provenir de notre exécution (voir E1 et E2) ; à corriger en J2 et J3 |
| 4 | 21/11 | Rayen Hsairi | J1 Données | Claude (Claude Code) | « Aide-nous à exécuter le notebook 1 et à rédiger les constats et le bilan J1 » | Brouillon des constats 1.6 et du bilan J1, chiffres sur les durées extrêmes, phrase de la section 2 du README | Chiffres recalculés et comparés aux sorties de notre exécution Colab (identiques) ; textes relus et reformulés en équipe | [À compléter : ce que l'équipe a modifié dans le brouillon] |
| 5 | 21/11 | Tawfik Zayen | Cadrage | Claude (Claude Code) | « Reprends le dépôt de notre coéquipier comme un nouveau projet pour l'équipe Synora, sans confusion avec un autre projet » | Copie des fichiers sans l'historique git, nom de l'équipe dans le README et le journal, `CLAUDE.md` qui délimite le projet, `.gitignore` (supports de cours exclus) | Liste des fichiers et historique git relus ; contenu comparé au dépôt GitHub d'origine et aux modèles du cours (`template_README.md`, `template_JOURNAL_IA.md`) | Aucune |
| 6 | 21/11 | Omar Idriss | Cadrage | Claude (Claude Code) | « Donne-nous tout ce que tu sais du projet, avec des critiques », puis « vérifie le projet par rapport à l'énoncé » | Liste des limites à discuter (écart avec / sans `PageValues`, découpage aléatoire et non temporel, modèles comparés au seuil 0,5, durées extrêmes, usage de `Region` et `VisitorType`) ; tableau de conformité à l'énoncé | Relecture du code des notebooks 2 et 3 ; versions lues dans `app/model.joblib` sans le charger ; versions de Colab lues dans la sortie de notre notebook 1 | Deux erreurs repérées dans la structure générée en ligne 3 (E1, E2) |
| 7 | 21/11 | Tawfik Zayen | Organisation | Claude (Claude Code) | « Donne-nous tous les notebooks avec leurs explications, les étapes et le rôle de chaque membre » | `GUIDE_EQUIPE.md` : explication de chaque notebook et de l'application, étapes restantes, répartition des tâches par rôle, calendrier | Contenu comparé au code des 3 notebooks et aux sorties de notre notebook 1 ; répartition relue en équipe [à faire] | Aucune ; les scores attendus du notebook 2 (F1 ≈ 0,4 / 0,65-0,7) sont des estimations à confirmer par notre exécution |
| 8 | 21/11 | Rayen Hsairi | J1 Données | Claude (Claude Code) | « Relis et critique le notebook 1 : est-il bien fait ? » | Critique : points forts (pas de fuite, pipeline) et manques (aucun graphique des valeurs aberrantes, doublons qui sont de vrais rebonds, durées nulles pour une page vue, modalités rares, `SpecialDay` limité à février et mai) | Chaque constat recalculé sur le CSV officiel (201 lignes en double, toutes des rebonds sans achat ; 717 sessions avec des pages produits mais une durée nulle) | La décision de retirer les doublons, prise dans la structure générée (ligne 3), est discutable : ce sont probablement de vraies visites distinctes. Décision gardée, mais à justifier dans le notebook |
| 9 | 21/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Ajoute au notebook 1 les cellules d'amélioration proposées dans la critique » | Sections 1.2 bis (profil des doublons), 1.2 ter (histogrammes log des durées, durées nulles), 1.5 bis (boîtes à moustaches acheteurs / non-acheteurs, corrélation de Spearman), 1.5 ter (`SpecialDay`, codes rares) ; justification du retrait des doublons en 2.1 | Copie du notebook exécutée de haut en bas sans erreur ; découpage inchangé (9 764 / 2 441) ; chiffres identiques à ceux de la critique (ligne 8) | Aucune ; le notebook doit être réimporté et réexécuté dans Colab pour que les sorties soient les nôtres |
| 10 | 21/11 | Tawfik Zayen | J1 Données | Claude (Claude Code) | « Vérifie le lien Colab du projet » | Constat : le lien est bien public, mais il ouvre un notebook de 2 cellules (chargement des données et `df.head()`), pas notre `01_donnees.ipynb` ; lien retiré du README et du journal en attendant le bon | Notebook téléchargé sans compte Google (comme un correcteur), cellules et sorties relues | Le lien avait été reporté dans le README (ligne du journal non numérotée, 21/11) sans en vérifier le contenu : corrigé |
| 11 | 21/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Fais toi-même les étapes Colab du notebook 1 » | Textes des cases 1.6 Constats et Bilan J1 rédigés dans le notebook à partir des sorties (doublons, durées, `PageValues`, profil des acheteurs, mois, codes rares) | Chaque chiffre repris des sorties de notre exécution du notebook ; [à faire : relecture et reformulation par Rayen, exécution dans Colab] | Aucune ; l'import dans Colab par Claude a échoué (navigateur non connecté), à faire par l'équipe |
| 12 | 21/11 | Tawfik Zayen | J1 Données | Claude (Claude Code) | « Vérifie le nouveau lien Colab du notebook 1 » | Lien vérifié puis reporté dans le README et le journal ; version exécutée dans Colab enregistrée dans `notebooks/01_donnees.ipynb` | Notebook téléchargé sans compte Google : 35 cellules, 18 cases exécutées dans l'ordre (1 à 18), 0 erreur, 5 graphiques ; chiffres de contrôle identiques (125 doublons, 12 205 lignes, 9 764 / 2 441, 72 / 73 colonnes) | Aucune |
| 13 | 21/11 | Rayen Hsairi | J1 Données (étapes 1-2) | Claude (Claude Code) | « Relis et reformule les constats et le bilan J1 avec des mots simples » | Nouvelle version plus simple des cases 1.6 et Bilan J1 | Chaque chiffre comparé aux sorties de notre exécution Colab : tous présents, sauf les taux d'achat par mois et par type de visiteur, visibles seulement sur les graphiques | La première version (ligne 11) citait des taux (1,6 %, 25,4 %, 24,9 %, 13,9 %) qu'aucune cellule n'affiche : remplacés par une lecture des graphiques. [Rayen doit encore relire la version finale et pouvoir l'expliquer à l'oral] |
| 14 | 21/11 | Khaled Mnejja | J2 Modèles (étapes 3-4) | Claude (Claude Code) | « Quelle est la suite ? » : exécution d'essai du notebook 2 en local avant Colab | Lecture des résultats de validation croisée (8 modèles) et du `BEST` obtenu | Exécuté de haut en bas sans erreur (6 min, scikit-learn 1.5.1 en local) ; découpage 9 764 / 2 441 identique ; [à refaire dans Colab pour les résultats officiels] | Confirme E2 : notre `BEST` avec `PageValues` est un gradient boosting (F1 CV 0,669), pas la forêt aléatoire (0,685) écrite à l'avance dans le notebook 3. Limite repérée : la forêt aléatoire sans `PageValues` a le F1 le plus bas (0,138) mais la meilleure AUC (0,769), car elle est jugée au seuil 0,5 |
| 15 | 21/11 | Khaled Mnejja | J2 Modèles (étapes 3-4) | Claude (Claude Code) | « Ajoute au notebook 2 une comparaison des modèles à leur meilleur seuil » | Section 2.1 bis (F1 de chaque modèle à son meilleur seuil, choisi en validation croisée sur l'entraînement, et précision moyenne) ; en 2.3, sélection sur ce F1 et réglage `GridSearchCV` noté en `average_precision` ; question ajoutée en 2.2 | Notebook exécuté en entier en local sans erreur (environ 10 min) ; test jamais utilisé ; forêt aléatoire sans `PageValues` : F1 de 0,138 au seuil 0,5 contre 0,414 au meilleur seuil | Corrige un défaut de la structure générée (ligne 3) : les modèles étaient comparés au seuil 0,5 alors que le seuil final est choisi au notebook 3, ce qui désavantageait la forêt aléatoire. Avec `PageValues`, le modèle retenu passe du gradient boosting à la forêt aléatoire |
| 16 | 21/11 | Khaled Mnejja | J2-J3 (étapes 1 à 6) | Claude (Claude Code) | « Tout le code doit être dans un seul projet Colab » (option : un seul notebook) | Fusion des 3 notebooks en `notebooks/synora_projet_ml.ipynb` : une seule cellule `CONFIG`, parties 1 à 6 numérotées comme les étapes du cours, `BEST = best` (la partie 5 reprend automatiquement les réglages de la partie 4) ; anciens notebooks retirés du dépôt (gardés dans l'historique git) | Notebook fusionné exécuté en entier en local : 30 cellules de code sur 30, 0 erreur, 10 graphiques, export de `model.joblib` réussi ; découpage 9 764 / 2 441 identique. Les scores sur le test de cet essai local ne servent à aucun choix : modèles, réglages et seuil restent fixés en validation croisée | Corrige E2 : plus aucune valeur de `BEST` écrite à la main. Écart au format du cours (3 notebooks attendus) : choix de l'équipe, à confirmer auprès de l'enseignant |
| 17 | 21/11 | Tawfik Zayen | Organisation | Claude (Claude Code) | « Mets à jour la documentation pour le notebook unique » | README (liens : un même notebook pour les 3 jalons, avec les parties), `ARCHITECTURE.md`, `GUIDE_EQUIPE.md`, `app/README.md` et commentaires de `app.py` | Plus aucune mention des anciens notebooks (recherche dans tous les fichiers) | Aucune |
| 18 | 21/11 | Tawfik Zayen | Organisation | Claude (Claude Code) | « Je ne veux aucune confusion avec un autre dépôt GitHub présent sur ce PC » | Dépôt distant `origin` = notre dépôt du projet (compte précisé dans l'URL) ; identifiants GitHub séparés par dépôt ; garde-fou local (hook `pre-push`) qui refuse tout push vers un autre dépôt | Garde-fou testé : refus pour un autre dépôt, accord pour le nôtre ; `git remote -v` vérifié | Aucune |
| 19 | 24/11 | Khaled Mnejja | J3 Déploiement (étape 6) | Claude (Claude Code) | « Continue le projet ML » (étape 6 : surveiller et réentraîner) | Parties 6.2 (rapport de suivi par lot : PSI des variables numériques, catégories inconnues, valeurs hors bornes, part d'achats annoncés, rappel et F1 quand les achats sont connus ; simulation par mois sur le test) et 6.3 (`retrain` : même configuration `BEST`, seuil rechoisi en validation croisée ; `should_replace` : ancien contre nouveau modèle sur des sessions récentes) | Notebook exécuté en entier en local, 0 erreur ; `retrain` sur les mêmes données redonne exactement le seuil de la partie 5 (0,593, contrôle `assert`). Le test n'a servi à aucun choix : la simulation par mois est seulement descriptive | Oui, voir E3 : la première version mettait les 10 mois en alerte (PSI de `SpecialDay`, lots trop petits). Corrigé avant le commit |
| 20 | 24/11 | Tawfik Zayen | Organisation | Claude (Claude Code) | « La documentation doit toujours suivre le modèle que je t'ai donné » | README remis à la structure exacte de `template_README.md` : lignes en italique ajoutées retirées, libellés « Notebook Colab 1, 2, 3 » rétablis (avec les parties du notebook unique dans la colonne des liens), seuil de décision déplacé dans la ligne des hyperparamètres, `Weekend` regroupé avec les catégorielles, case de la checklist rétablie ; champ des liens Colab du journal mis à jour | Comparaison ligne à ligne avec le modèle (`diff`) : il ne reste que des champs remplis, aucune section ni ligne ajoutée. Journal : 9 colonnes et 6 rubriques par fiche, conformes | L'IA avait ajouté au README une sous-section absente du modèle (ligne 19) : retirée. La checklist parle de 3 notebooks alors que nous en avons un seul : à faire valider par l'enseignant |
| 21 | 24/11 | Tawfik Zayen | Organisation | Claude (Claude Code) | « Voici le lien Colab » (nouveau notebook `1HTM…`) | Lien reporté dans le README (3 lignes des notebooks) et dans la section 1 du journal, à la place de l'ancien (`1LiB…`) | Notebook téléchargé sans compte (lien public) et comparé au notebook du dépôt : c'est bien `synora_projet_ml.ipynb`, mais la version d'avant les parties 6.2-6.3 (61 cellules contre 66). Exécution enregistrée : parties 1-2 complètes (scikit-learn 1.6.1, découpage 9 764 / 2 441, 0 erreur), arrêt en 4.1 (validation croisée interrompue après 2 modèles) | Aucune erreur de l'IA. Reste à faire : importer la version à jour et tout exécuter |
| 22 | 24/11 | Omar Idriss | J2-J3 (étapes 3 à 6) | Claude (Claude Code) | « C'est exécuté » : vérifier l'exécution complète du notebook dans Colab | Relevé des chiffres officiels (Colab, scikit-learn 1.6.1) pour 4.2, 5.4, 6.2 et le README : sans `PageValues`, gradient boosting (`learning_rate=0.05`, `max_depth=6`), seuil 0,593, test F1 0,443, rappel 0,599, AUC 0,785 ; avec `PageValues`, forêt aléatoire, seuil 0,323, test F1 0,683, rappel 0,736, AUC 0,925 | Notebook téléchargé sans compte : 66 cellules identiques au dépôt, 32 cellules de code sur 32 exécutées dans l'ordre, 0 erreur. Tous les chiffres sont identiques à l'essai local (scikit-learn 1.5.1). `model.joblib` téléchargé depuis Colab : 3 exports identiques octet pour octet, mais différent de celui de `app/` | Aucune nouvelle erreur. Confirme E1 : `app/model.joblib` et `app/requirements.txt` (1.9.1) ne viennent pas de notre exécution ; les fichiers de Colab (1.6.1) sont prêts pour la correction |
| 23 | | | | | | | | |

Supprimez les deux lignes d'exemple avant le rendu.

## 3. Erreurs de l'IA détectées

Une fiche par erreur importante (au moins une). Numérotez-les E1, E2… et renvoyez-y depuis le tableau du journal.

### E1 — Modèle et `requirements.txt` incompatibles avec notre Colab

| Rubrique | À remplir |
| --- | --- |
| Ligne du journal | 3 (repérée en ligne 6) |
| Ce que l'IA a proposé | Un `app/model.joblib` déjà fourni et un `requirements.txt` avec `scikit-learn==1.9.1`, `pandas==3.1.1`, `numpy==2.4.6` |
| Pourquoi c'est faux | Le modèle n'a pas été produit par notre notebook 3 : ce n'est pas notre modèle, et ses scores ne correspondent pas à notre exécution. Notre Colab utilise `scikit-learn 1.6.1` et `pandas 2.2.3` (sortie de la cellule d'imports du notebook 1). Un modèle enregistré avec scikit-learn 1.9.1 risque de ne pas se charger, ou de mal se comporter, avec une autre version : c'est la règle 8 d'`ARCHITECTURE.md` (« mêmes versions en Colab et en production »). |
| Comment vous l'avez repéré | Relecture : versions de la cellule d'imports dans Colab comparées à `requirements.txt` ; chaînes `1.9.1` et `3.1.1` lues dans `model.joblib` sans le charger |
| Correction apportée | [À faire en J3] Exécuter notre notebook 3 dans Colab ; remplacer `app/model.joblib` **et** `app/requirements.txt` par les deux fichiers qu'il télécharge (la section 4 écrit les versions exactes de Colab) |
| Effet mesuré | [À compléter en J3] Versions avant : 1.9.1 / 3.1.1 ; après : celles de notre Colab ; l'application se charge sans erreur sur Streamlit Cloud (oui / non) |

### E2 — Résultats et texte de limites écrits à l'avance

| Rubrique | À remplir |
| --- | --- |
| Ligne du journal | 3 (repérée en ligne 6) |
| Ce que l'IA a proposé | Dans le notebook 3, une cellule `BEST` déjà remplie (`Gradient_boosting` sans `PageValues`, F1 CV = 0,431 ; `Foret_aleatoire` avec `PageValues`, F1 CV = 0,685) ; dans `app.py`, un texte fixe « Il détecte environ 7 acheteurs sur 10, mais une alerte sur trois seulement correspond à un vrai achat » |
| Pourquoi c'est faux | Ces chiffres n'ont pas été obtenus par notre notebook 2 ni sur notre test. Les reprendre reviendrait à rendre des résultats non vérifiés, et à montrer aux utilisateurs de l'application des limites qui ne décrivent peut-être pas notre modèle. |
| Comment vous l'avez repéré | Relecture du notebook 3 et de `app.py` avant leur exécution (notebook 2 pas encore exécuté) |
| Correction apportée | `BEST` : notebook unique, la partie 5 reprend `best` de la partie 4 (`BEST = best`), plus aucune valeur écrite à la main (ligne 16). [À faire en J3] réécrire `LIMITS` dans `app.py` avec le rappel et la précision de notre test |
| Effet mesuré | [À compléter] Valeurs de `BEST` et du texte avant et après |

### E3 — Suivi en production qui déclenche une alerte tous les mois

| Rubrique | À remplir |
| --- | --- |
| Ligne du journal | 19 |
| Ce que l'IA a proposé | En partie 6.2, une alerte de dérive dès que le PSI d'une variable numérique dépasse 0,25, sur toutes les variables, et une alerte de baisse du rappel sur tous les lots mensuels |
| Pourquoi c'est faux | `SpecialDay` n'est non nulle qu'en février et mai : pour les autres mois, son PSI vaut 0,727 par construction, sans aucune dérive réelle. Février (37 sessions, aucun achat) donnait un rappel de 0. Une alerte qui sonne tout le temps ne sert à rien : personne ne la regarderait plus |
| Comment vous l'avez repéré | Lecture du tableau de suivi après l'exécution complète du notebook en local : 10 mois en alerte sur 10, avec `SpecialDay` comme variable la plus en dérive dans 8 mois |
| Correction apportée | `SpecialDay` exclue du PSI (variable de calendrier) ; pas d'alerte sur les lots de moins de 100 sessions, ni sur le rappel avec moins de 20 achats ; la raison de chaque alerte est affichée |
| Effet mesuré | Essai local (à confirmer dans Colab) : de 10 mois en alerte à 3 (mars et mai : baisse du rappel ; octobre : dérive de `Administrative`), 5 lots signalés trop petits, novembre et décembre sans alerte |

## 4. Sources externes

Tout notebook, dépôt ou article dont vous avez repris une idée ou du code.

| N° | Source (lien) | Type | Ce qui a été repris | Où dans notre projet |
| --- | --- | --- | --- | --- |
| S1 | | Notebook Kaggle / dépôt GitHub / documentation / forum | | Notebook, cellule ou fichier |

### Critique d'un notebook public (obligatoire)

Une demi-page. Choisissez l'un des notebooks les plus votés sur votre jeu de données.

- **Notebook choisi** : lien, auteur, nombre de votes.
- **Ce qu'il fait bien** : deux ou trois phrases.
- **Erreur ou limite trouvée** : fuite de données, métrique inadaptée, évaluation sur le train, rééquilibrage avant le découpage, variable connue trop tard…
- **Preuve** : la cellule concernée et, si possible, le score obtenu une fois l'erreur corrigée.
- **Ce que nous avons fait différemment** : une ou deux phrases.

## 5. Bilan de l'équipe

Cinq lignes au maximum, à rédiger pour le rendu final.

- Où l'IA nous a fait gagner du temps :
- Où elle nous a fait perdre du temps ou induits en erreur :
- Ce que nous ferions autrement :

### Avant chaque dépôt

- [ ] Chaque membre a au moins une ligne dans le journal
- [ ] Au moins une erreur de l'IA est décrite en détail (section 3)
- [ ] Toutes les sources externes sont listées (section 4)
- [ ] La critique d'un notebook public est rédigée (rendu final)
- [ ] Aucune donnée personnelle n'a été envoyée à un assistant
- [ ] Chaque membre peut expliquer chaque ligne de code reprise d'une IA
- [ ] Les lignes d'exemple du modèle sont supprimées
