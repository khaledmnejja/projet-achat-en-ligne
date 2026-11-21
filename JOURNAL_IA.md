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
| Nom de l'équipe | |
| Sujet (n° et titre) | |
| Membres | |
| Outils IA utilisés (nom et version si connue) | |
| Liens des notebooks Colab | |

## 2. Journal

Une ligne par usage. Le prompt peut être résumé ; s'il est long, mettez le texte complet en annexe et indiquez son numéro. La colonne « Vérification » dit comment vous avez contrôlé le résultat (exécution, comparaison avec le cours, test sur un exemple).

| N° | Date | Membre | Jalon | Outil | Prompt (résumé) | Ce qui a été gardé | Vérification | Erreur détectée / correction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 20/11 | Exemple : Amira | J1 Données | Assistant de code Colab | « Écris un pipeline qui encode les colonnes catégorielles et normalise les numériques » | Structure du `ColumnTransformer` | Exécuté sur le train, dimensions vérifiées | Le `fit` était fait sur tout le jeu avant le découpage (fuite) : découpage déplacé avant le pipeline (voir E1) |
| 2 | 22/11 | Exemple : Youssef | J1 Données | Chatbot | « Explique la différence entre OneHotEncoder et OrdinalEncoder » | Explication reformulée dans le notebook | Comparée au support de S2 | Aucune |
| 3 | 21/11 | [Nom] | Cadrage | Claude (Claude Code) | « À partir du schéma des six étapes, génère une structure de projet conforme et fiable » | Arborescence, `ARCHITECTURE.md`, squelettes des 3 notebooks et de `app.py` | Notebooks exécutés de haut en bas, découpage et dimensions vérifiés | [À compléter après relecture en équipe] |
| 4 | | | | | | | | |

Supprimez les deux lignes d'exemple avant le rendu.

## 3. Erreurs de l'IA détectées

Une fiche par erreur importante (au moins une). Numérotez-les E1, E2… et renvoyez-y depuis le tableau du journal.

### E1 — [titre court de l'erreur]

| Rubrique | À remplir |
| --- | --- |
| Ligne du journal | N° |
| Ce que l'IA a proposé | Extrait de code ou de texte |
| Pourquoi c'est faux | Explication avec le vocabulaire du cours (fuite de données, évaluation sur le train, mauvaise métrique, mauvais encodage…) |
| Comment vous l'avez repéré | Score trop beau, erreur à l'exécution, comparaison avec le cours, relecture… |
| Correction apportée | Extrait du code corrigé |
| Effet mesuré | Résultat avant et après (score, dimensions, graphique) |

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
