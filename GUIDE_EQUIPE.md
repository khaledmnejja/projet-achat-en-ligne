# Guide de l'équipe Synora · Sujet 18, intentions d'achat

Document de travail interne (non demandé par le cours). Il explique chaque partie du notebook unique `notebooks/synora_projet_ml.ipynb`, les étapes à suivre et qui fait quoi.
Rendu final sur Moodle : **samedi 28/11, 08h00**.

## L'équipe et les rôles (J1)

| Membre | Rôle | Domaine |
| --- | --- | --- |
| Khaled Mnejja | Modélisateur | Choix et entraînement des modèles (parties 3-4) |
| Rayen Hsairi | Analyste données | Exploration et préparation des données (parties 1-2) |
| Omar Idriss | Évaluateur | Mesure sur le test, seuil, erreurs, limites (partie 5) |
| Tawfik Zayen | Documentaliste | README, journal IA, vérification avant chaque dépôt |
| Omar Zouari | Présentateur | 6 diapositives, préparation de la soutenance |

**Règles du cours :**
- Chacun **code au moins une partie**. C'est vérifié par l'historique du notebook et par la question individuelle à la soutenance.
- Les rôles tournent à chaque jalon. Pensez à mettre à jour la section 5 du README.
- Chacun doit avoir au moins une ligne dans `JOURNAL_IA.md`.

## Le projet en une phrase

À partir de 12 330 visites passées d'un site marchand, on apprend à un modèle à deviner, **pendant une visite**, si elle va finir par un achat. L'équipe marketing peut ainsi proposer une offre au bon moment.

## Vue d'ensemble

| Fichier | Étapes du cours | Jalon | Responsable | État |
| --- | --- | --- | --- | --- |
| `synora_projet_ml.ipynb`, parties 1-2 | 1 Collecte, 2 Préparation | J1 · 25/11 | Rayen | ✅ Exécutées dans Colab, textes rédigés |
| `synora_projet_ml.ipynb`, parties 3-4 | 3 Modèle, 4 Entraînement | J2 · fin S4 | Khaled | ✅ Testées en local · ⏳ Colab, textes 4.2 et bilan |
| `synora_projet_ml.ipynb`, parties 5-6.1 | 5 Évaluation, export | J3 · fin S5 | Omar Idriss | ✅ Testées en local · ⏳ Colab, limites et bilan |
| `app/` (Streamlit) | 6 Déploiement | J3 · fin S5 | Khaled, avec Omar Idriss | ⏳ À déployer |
| `README.md`, `JOURNAL_IA.md` | Tous | Tous | Tawfik | ⏳ En cours |
| `presentation/` (6 diapositives, PDF) | Tous | Rendu final | Omar Zouari | ⏳ À faire |

**Un seul notebook, une seule configuration.** Tout le code est dans `synora_projet_ml.ipynb` (choix de l'équipe) : une cellule `CONFIG` unique (graine 42, 20 % de test, colonnes), un découpage unique contrôlé par `EXPECTED_SPLIT`, et la partie 5 reprend automatiquement les réglages de la partie 4 (`BEST = best`) : plus rien à recopier à la main. Le même lien Colab sert pour les trois jalons du README.

---

## Parties 1-2 · Données (J1, 25/11) · responsable : Rayen

**But :** charger les données, vérifier leur qualité, les comprendre, puis les préparer pour les modèles.

| Section | Ce qu'elle fait | Résultat obtenu |
| --- | --- | --- |
| 0 Mise en place | Imports, `CONFIG`, fonctions communes | Colab : scikit-learn 1.6.1 |
| 1.1 Premier contact | Charge le CSV officiel de l'UCI | 12 330 lignes × 18 colonnes |
| 1.2 Qualité | Valeurs manquantes, doublons, statistiques | 0 manquante, 125 doublons |
| 1.2 bis Doublons | Profil des lignes en double | 201 lignes, toutes des rebonds sans achat : sans doute de vraies visites |
| 1.2 ter Valeurs aberrantes | Histogrammes log des durées, durées nulles | 867 sessions > 1 h, maximum 17,8 h ; 717 sessions avec des pages produits mais une durée nulle (limite de Google Analytics) |
| 1.3 La cible | Répartition achat / non-achat | 15,5 % d'achats : déséquilibre |
| 1.4 Catégories | Mois et types de visiteurs | Pas de janvier ni d'avril ; « June » mal écrit |
| 1.5 `PageValues` | Taux d'achat avec ou sans valeur de page | 56 % contre 4 % : variable suspecte |
| 1.5 bis Acheteurs | Boîtes à moustaches et corrélation de Spearman | Les acheteurs sortent moins vite (`ExitRates` −0,25) et voient 2 fois plus de pages produits ; `PageValues` 0,63 |
| 1.5 ter À surveiller | `SpecialDay` et codes rares | `SpecialDay` seulement en février et mai ; 12 codes avec moins de 30 sessions |
| 1.6 Constats | **À rédiger** | Brouillon disponible (voir le journal, ligne 4) |
| 2.1 Nettoyage | Corrige « June », retire les doublons | 12 205 lignes |
| 2.2 Découpage | 80 % entraînement / 20 % test, stratifié | 9 764 / 2 441 |
| 2.3 Encodage | `StandardScaler` sur les nombres, `OneHotEncoder` sur les codes | 72 colonnes (73 avec `PageValues`) |
| 2.4 Nouvelle session | Prépare une visite comme le fera l'application | Vecteur de 72 valeurs |
| Bilan J1 | **À rédiger** | Brouillon disponible |

**Idées à savoir expliquer :**
- Pourquoi on sépare les données **avant** de les préparer (sinon il y a une fuite).
- Pourquoi la région 8 n'est pas « plus grande » que la région 2.
- Pourquoi l'exactitude est trompeuse ici.

**Étapes restantes :**
1. ✅ Parties exécutées dans Colab, constats et bilan rédigés.
2. **Rayen :** relire les constats 1.6 et le bilan J1, et savoir les expliquer à l'oral.

---

## Parties 3-4 · Modèles (J2, fin S4) · responsable : Khaled

**But :** comparer plusieurs algorithmes et garder le meilleur, **sans jamais toucher au test**.

| Section | Ce qu'elle fait |
| --- | --- |
| 3 Modèle | 4 candidats : référence naïve, régression logistique, forêt aléatoire, gradient boosting, tous avec `class_weight="balanced"` |
| 4.1 Validation croisée | Chaque modèle est entraîné 5 fois sur 4/5 des données et testé sur le 1/5 restant, **avec et sans `PageValues`** : 8 résultats (F1, rappel, précision, AUC, sous forme moyenne ± écart-type), plus un graphique |
| 4.1 bis Meilleur seuil | Compare chaque modèle à son meilleur seuil (validation croisée sur l'entraînement) : au seuil 0,5, la forêt aléatoire paraît mauvaise (F1 0,14) alors qu'elle est au niveau des autres (0,41) |
| 4.2 Lecture | **À rédiger** : écart avec / sans `PageValues`, ce qu'il dit de la fuite, meilleur modèle par variante |
| 4.3 `GridSearchCV` | Règle le meilleur modèle (au meilleur seuil) de chaque variante, noté en précision moyenne |
| 4.4 Configuration | Affiche `best`, repris **automatiquement** en partie 5 |
| Bilan J2 | **À rédiger** : modèle retenu, hyperparamètres |

**Essai en local :** F1 au meilleur seuil d'environ 0,42 sans `PageValues` et 0,69 avec. Cet écart est le résultat central du sujet.

**Idées à savoir expliquer :**
- La validation croisée, et pourquoi on donne un écart-type.
- Ce que fait `class_weight="balanced"`.
- Pourquoi on compare au modèle naïf.

**Étapes :**
1. **Khaled :** importer la dernière version de `synora_projet_ml.ipynb` dans le notebook Colab du README (`1HTM…`, Gérer les versions → Importer une nouvelle version, pour garder le lien), **Exécution → Tout exécuter** (environ 15 min), enregistrer.
2. **Khaled :** rédiger 4.2 et le bilan J2.
3. **Tawfik :** reporter les scores dans la section 3 du README (une ligne par modèle et par variante), puis télécharger le `.ipynb`.

---

## Partie 5 et export (6.1) · Évaluation (J3, fin S5) · responsable : Omar Idriss

**But :** mesurer **une seule fois**, honnêtement, le modèle final sur le test, comprendre ses erreurs, puis l'exporter pour l'application.

| Section | Ce qu'elle fait |
| --- | --- |
| 5.0 Configuration | `BEST = best` : réglages repris de la partie 4 (corrige E2 : plus de valeurs écrites à l'avance) |
| 5.1 Choix du seuil | Cherche, en validation croisée sur l'entraînement, le seuil de probabilité qui maximise le F1 (pas forcément 50 %), avec une courbe précision-rappel |
| 5.2 Évaluation unique | Mesure sur le test : matrice de confusion, F1, rappel, AUC, courbes ROC |
| 5.3 Erreurs | Rappel par type de visiteur et par mois : quels acheteurs le modèle rate-t-il ? |
| 5.4 Limites | **À rédiger**, puis à reporter dans la section 4 du README |
| 6.1 Export | Crée `model.joblib` et `requirements.txt` avec les versions exactes de Colab, puis les télécharge |
| Bilan J3 | **À rédiger** |

**Idées à savoir expliquer :**
- Pourquoi le test ne sert qu'une fois.
- Ce qu'est un seuil de décision.
- Comment lire une matrice de confusion (faux positif : offre gaspillée ; faux négatif : acheteur raté).
- Pourquoi on déploie la version **sans** `PageValues`.

**Étapes :**
1. **Omar Idriss :** après l'exécution complète dans Colab, lire les résultats de la partie 5.
2. **Omar Idriss :** rédiger les limites (5.4) et le bilan J3, enregistrer.
3. **Omar Idriss :** récupérer `model.joblib` et `requirements.txt` (téléchargés automatiquement).
4. **Tawfik :** remplir les sections 3 (modèle retenu, seuil) et 4 (limites) du README, puis compléter les fiches E1 et E2 du journal.

---

## Application Streamlit · déploiement (J3) · responsables : Khaled, avec Omar Idriss

**But :** une page web où l'on saisit une visite pour obtenir la probabilité d'achat.

**Ce que fait `app.py` :**
- Il charge `model.joblib`.
- Il affiche un formulaire et refuse les saisies impossibles (aucune page vue, durée sans page).
- Il affiche la probabilité, le seuil et un rappel des limites.

**Étapes :**
1. ✅ **Khaled :** `app/model.joblib` **et** `app/requirements.txt` remplacés par ceux produits en partie 6.1 (corrige E1).
2. ✅ **Omar Idriss :** texte des limites de `app.py` réécrit avec les vrais chiffres du test (`limits_text`, corrige E2). À relire pour pouvoir l'expliquer à l'oral.
3. **Khaled :** créer un dépôt GitHub public contenant `app.py`, `requirements.txt` et `model.joblib`.
4. **Khaled :** sur **share.streamlit.io**, cliquer sur New app, choisir le dépôt et le fichier `app.py`, puis Deploy.
5. **Omar Idriss :** tester l'application (une saisie normale, une saisie absurde).
6. **Tawfik :** ajouter les liens de l'application et du dépôt dans le README.

**Après la mise en service (notebook, parties 6.2 et 6.3) :**

| Section | Ce qu'elle fait |
| --- | --- |
| 6.2 Surveiller | Rapport de suivi par lot (un lot par mois du test, en simulation) : dérive des entrées (PSI), catégories inconnues, part d'achats annoncés, rappel et F1 quand les achats sont connus, raison de chaque alerte |
| 6.3 Réentraîner | Quand réentraîner, comment (retour à l'étape 2 avec les nouvelles sessions), et règle de remplacement : le nouveau modèle doit battre l'ancien sur les sessions récentes |

**Idées à savoir expliquer :** ce qu'est une dérive des données ; pourquoi on ne connaît le rappel qu'après coup ; pourquoi `SpecialDay` est exclue du PSI ; pourquoi on ne remplace pas un modèle sans le comparer à l'ancien.

7. **Khaled :** après l'exécution dans Colab, rédiger la lecture du tableau de suivi (6.2).

---

## Documentation (tout au long du projet) · responsable : Tawfik

- **`README.md`** : liens, sections 3 (résultats) et 4 (limites), checklist « Avant le rendu », suppression des lignes en italique et des crochets.
- **`JOURNAL_IA.md`** (10 % de la note) :
  - une ligne par usage de l'IA ;
  - les fiches E1 et E2 à compléter ;
  - les sources externes ;
  - **la critique d'un notebook Kaggle (obligatoire)** ;
  - le bilan de l'équipe ;
  - la suppression des 2 lignes d'exemple.
- **Vérification avant chaque dépôt** : chaque membre a sa ligne, tous les liens s'ouvrent en navigation privée.

## Présentation et soutenance · responsable : Omar Zouari

**6 diapositives en PDF dans `presentation/` :**
1. Le problème et l'utilisateur
2. Les données et les pièges
3. La préparation
4. Les modèles, avec l'écart avec / sans `PageValues`
5. L'évaluation et les limites
6. La démonstration de l'application

**Préparer la question individuelle :** chaque membre doit pouvoir expliquer sa partie, et le débat sur `PageValues`.

## Calendrier

| Date | Objectif |
| --- | --- |
| Avant le 25/11 | Parties 1-2 finalisées et partagées (J1) |
| Fin S4 | Parties 3-4 exécutées et rédigées (J2) |
| Fin S5 | Parties 5-6, application déployée (J3) |
| Avant le 28/11, 08h00 | README, journal, présentation, checklist cochée, **un seul** dépôt sur Moodle |
