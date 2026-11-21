# Guide de l'équipe Synora · Sujet 18, intentions d'achat

Document de travail interne (non demandé par le cours). Il explique chaque notebook, les étapes à suivre et qui fait quoi.
Rendu final sur Moodle : **samedi 28/11, 08h00**.

## L'équipe et les rôles (J1)

| Membre | Rôle | Domaine |
| --- | --- | --- |
| Khaled Mnejja | Modélisateur | Choix et entraînement des modèles (notebook 2) |
| Rayen Hsairi | Analyste données | Exploration et préparation des données (notebook 1) |
| Omar Idriss | Évaluateur | Mesure sur le test, seuil, erreurs, limites (notebook 3) |
| Tawfik Zayen | Documentaliste | README, journal IA, vérification avant chaque dépôt |
| Omar Zouari | Présentateur | 6 diapositives, préparation de la soutenance |

**Règles du cours :**
- Chacun **code au moins une partie**. C'est vérifié par l'historique des notebooks et par la question individuelle à la soutenance.
- Les rôles tournent à chaque jalon. Pensez à mettre à jour la section 5 du README.
- Chacun doit avoir au moins une ligne dans `JOURNAL_IA.md`.

## Le projet en une phrase

À partir de 12 330 visites passées d'un site marchand, on apprend à un modèle à deviner, **pendant une visite**, si elle va finir par un achat. L'équipe marketing peut ainsi proposer une offre au bon moment.

## Vue d'ensemble

| Fichier | Étapes du cours | Jalon | Responsable | État |
| --- | --- | --- | --- | --- |
| `notebooks/01_donnees.ipynb` | 1 Collecte, 2 Préparation | J1 · 25/11 | Rayen | ✅ Exécuté · ⏳ textes à rédiger |
| `notebooks/02_modeles.ipynb` | 3 Modèle, 4 Entraînement | J2 · fin S4 | Khaled | ⏳ À exécuter |
| `notebooks/03_evaluation.ipynb` | 5 Évaluation | J3 · fin S5 | Omar Idriss | ⏳ À exécuter |
| `app/` (Streamlit) | 6 Déploiement | J3 · fin S5 | Khaled, avec Omar Idriss | ⏳ À déployer |
| `README.md`, `JOURNAL_IA.md` | Tous | Tous | Tawfik | ⏳ En cours |
| `presentation/` (6 diapositives, PDF) | Tous | Rendu final | Omar Zouari | ⏳ À faire |

**Règle d'or partagée par les 3 notebooks.** La cellule `CONFIG` est identique partout : graine 42, 20 % de test, mêmes colonnes. Ne la modifiez jamais dans un seul notebook. Un contrôle (`EXPECTED_SPLIT`) arrête le notebook si le découpage diffère.

---

## Notebook 1 · Données (J1, 25/11) · responsable : Rayen

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
1. **Rayen :** coller les constats 1.6 et le bilan J1 relus dans Colab, puis **Fichier → Enregistrer**.
2. **Rayen :** vérifier que le lien de partage s'ouvre dans une fenêtre privée (il est déjà dans le README).
3. **Tawfik :** télécharger le `.ipynb` final et remplacer `notebooks/01_donnees.ipynb`.

---

## Notebook 2 · Modèles (J2, fin S4) · responsable : Khaled

**But :** comparer plusieurs algorithmes et garder le meilleur, **sans jamais toucher au test**.

| Section | Ce qu'elle fait |
| --- | --- |
| 0 Mise en place | Mêmes `CONFIG` et découpage que le notebook 1 |
| 1 Modèle | 4 candidats : référence naïve, régression logistique, forêt aléatoire, gradient boosting, tous avec `class_weight="balanced"` |
| 2.1 Validation croisée | Chaque modèle est entraîné 5 fois sur 4/5 des données et testé sur le 1/5 restant, **avec et sans `PageValues`** : 8 résultats (F1, rappel, précision, AUC, sous forme moyenne ± écart-type), plus un graphique |
| 2.2 Lecture | **À rédiger** : écart avec / sans `PageValues`, ce qu'il dit de la fuite, meilleur modèle par variante |
| 2.3 `GridSearchCV` | Essaie plusieurs réglages du meilleur modèle de chaque variante |
| 2.4 Configuration | Affiche `BEST = {...}`, **à recopier dans le notebook 3** |
| Bilan J2 | **À rédiger** : modèle retenu, hyperparamètres |

**Ce qu'on attend :** un F1 d'environ 0,4 sans `PageValues` et d'environ 0,65 à 0,7 avec. Cet écart est le résultat central du sujet.

**Idées à savoir expliquer :**
- La validation croisée, et pourquoi on donne un écart-type.
- Ce que fait `class_weight="balanced"`.
- Pourquoi on compare au modèle naïf.

**Étapes :**
1. **Khaled :** importer `02_modeles.ipynb` dans Colab, **Exécution → Tout exécuter** (5 à 10 min), enregistrer.
2. **Khaled :** rédiger 2.2 et le bilan J2.
3. **Tawfik :** reporter les scores dans la section 3 du README (une ligne par modèle et par variante), puis télécharger le `.ipynb`.
4. **Khaled :** partager le lien Colab, que Tawfik ajoute au README.

---

## Notebook 3 · Évaluation (J3, fin S5) · responsable : Omar Idriss

**But :** mesurer **une seule fois**, honnêtement, le modèle final sur le test, comprendre ses erreurs, puis l'exporter pour l'application.

| Section | Ce qu'elle fait |
| --- | --- |
| Configuration J2 | ⚠️ **Remplacer `BEST`** par la sortie du notebook 2 : les valeurs actuelles ne sont pas les nôtres (journal, E2) |
| 1 Choix du seuil | Cherche, en validation croisée sur l'entraînement, le seuil de probabilité qui maximise le F1 (pas forcément 50 %), avec une courbe précision-rappel |
| 2 Évaluation unique | Mesure sur le test : matrice de confusion, F1, rappel, AUC, courbes ROC |
| 3 Erreurs | Rappel par type de visiteur et par mois : quels acheteurs le modèle rate-t-il ? |
| Limites | **À rédiger**, puis à reporter dans la section 4 du README |
| 4 Export | Crée `model.joblib` et `requirements.txt` avec les versions exactes de Colab, puis les télécharge |
| Bilan J3 | **À rédiger** |

**Idées à savoir expliquer :**
- Pourquoi le test ne sert qu'une fois.
- Ce qu'est un seuil de décision.
- Comment lire une matrice de confusion (faux positif : offre gaspillée ; faux négatif : acheteur raté).
- Pourquoi on déploie la version **sans** `PageValues`.

**Étapes :**
1. **Omar Idriss :** importer le notebook dans Colab et **coller le `BEST` du notebook 2** dans la cellule prévue.
2. **Omar Idriss :** tout exécuter, enregistrer, rédiger les limites et le bilan J3.
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
1. **Khaled :** remplacer `app/model.joblib` **et** `app/requirements.txt` par ceux du notebook 3 (corrige E1).
2. **Omar Idriss :** réécrire le texte `LIMITS` dans `app.py` avec les vrais chiffres du test (corrige E2).
3. **Khaled :** créer un dépôt GitHub public contenant `app.py`, `requirements.txt` et `model.joblib`.
4. **Khaled :** sur **share.streamlit.io**, cliquer sur New app, choisir le dépôt et le fichier `app.py`, puis Deploy.
5. **Omar Idriss :** tester l'application (une saisie normale, une saisie absurde).
6. **Tawfik :** ajouter les liens de l'application et du dépôt dans le README.

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
| Avant le 25/11 | Notebook 1 finalisé et partagé (J1) |
| Fin S4 | Notebook 2 exécuté et rédigé (J2) |
| Fin S5 | Notebook 3, application déployée (J3) |
| Avant le 28/11, 08h00 | README, journal, présentation, checklist cochée, **un seul** dépôt sur Moodle |
