"""Étape 6 · Déploiement : estimer, pendant une visite, la probabilité d'achat d'une session.

Lancer en local :  streamlit run app.py
Le fichier model.joblib est produit par la partie 6 du notebook synora_projet_ml.ipynb.
"""
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

MONTH_ORDER = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

LABELS = {
    "Administrative": "Pages administratives vues",
    "Administrative_Duration": "Temps sur les pages administratives (s)",
    "Informational": "Pages d'information vues",
    "Informational_Duration": "Temps sur les pages d'information (s)",
    "ProductRelated": "Pages produits vues",
    "ProductRelated_Duration": "Temps sur les pages produits (s)",
    "BounceRates": "Taux de rebond moyen des pages vues",
    "ExitRates": "Taux de sortie moyen des pages vues",
    "SpecialDay": "Proximité d'un jour spécial (0 à 1)",
    "PageValues": "Valeur moyenne des pages vues",
    "Month": "Mois",
    "VisitorType": "Type de visiteur",
    "OperatingSystems": "Code du système d'exploitation",
    "Browser": "Code du navigateur",
    "Region": "Code de la région",
    "TrafficType": "Code de la source de trafic",
}

# (nombre de pages, durée) : une durée sans page vue est incohérente
PAGE_PAIRS = [
    ("Administrative", "Administrative_Duration"),
    ("Informational", "Informational_Duration"),
    ("ProductRelated", "ProductRelated_Duration"),
]
COUNT_COLS = {count for count, _ in PAGE_PAIRS}

LIMITS = (
    "**Limites du modèle.** Entraîné sur les sessions d'un seul site marchand pendant une année, "
    "sans janvier ni avril. Il détecte environ 7 acheteurs sur 10, mais une alerte sur trois "
    "seulement correspond à un vrai achat. C'est une aide pour cibler une offre ou une assistance, "
    "pas une décision automatique : ne l'utilisez ni pour fixer des prix différents selon la région "
    "ou le type de visiteur, ni sur un autre site sans le réentraîner."
)


@st.cache_resource
def load_bundle():
    # joblib = pickle : ne charger que le model.joblib produit par NOTRE notebook (partie 6, livrable imposé),
    # jamais un fichier .joblib reçu d'ailleurs, qui pourrait exécuter du code.
    return joblib.load(Path(__file__).parent / "model.joblib")


def validate(values):
    """Refuse les sessions impossibles avant toute prédiction."""
    errors = []
    if sum(values[count] for count in COUNT_COLS) == 0:
        errors.append("Une session doit contenir au moins une page vue.")
    for count, duration in PAGE_PAIRS:
        if values[count] == 0 and values[duration] > 0:
            errors.append(f"{LABELS[duration]} : impossible sans page vue de ce type.")
    return errors


st.set_page_config(page_title="Intention d'achat", page_icon="🛒", layout="centered")
bundle = load_bundle()
pipe, threshold, schema = bundle["pipeline"], bundle["threshold"], bundle["schema"]

st.title("🛒 Cette visite va-t-elle se terminer par un achat ?")
st.caption(
    f"Modèle : {bundle['metrics_test']['modele']} ({bundle['feature_set']}) · "
    f"sur le test : rappel {bundle['metrics_test']['rappel']:.2f}, "
    f"F1 {bundle['metrics_test']['f1']:.2f}, AUC {bundle['metrics_test']['auc']:.2f}"
)
st.info(LIMITS)

with st.form("session"):
    values = {}
    st.subheader("Navigation pendant la session")
    left, right = st.columns(2)
    for i, col in enumerate(bundle["num_cols"]):
        low, high = schema["num"][col]
        box = left if i % 2 == 0 else right
        if col in COUNT_COLS:
            values[col] = box.number_input(LABELS[col], min_value=0, max_value=int(high), value=0, step=1)
        else:
            values[col] = box.number_input(LABELS[col], min_value=0.0, max_value=float(high),
                                           value=0.0, format="%.4f" if high <= 1 else "%.1f")

    st.subheader("Contexte de la visite")
    left, right = st.columns(2)
    for i, col in enumerate(bundle["cat_cols"]):
        options = schema["cat"][col]
        if col == "Month":
            options = sorted(options, key=MONTH_ORDER.index)
        box = left if i % 2 == 0 else right
        values[col] = box.selectbox(LABELS[col], options)
    values["Weekend"] = int(st.checkbox("Visite pendant le week-end"))

    submitted = st.form_submit_button("Estimer la probabilité d'achat", type="primary")

if submitted:
    errors = validate(values)
    if errors:
        for message in errors:
            st.error(message)
        st.stop()

    X = pd.DataFrame([values])[bundle["features"]]
    proba = float(pipe.predict_proba(X)[0, 1])
    st.metric("Probabilité d'achat estimée", f"{proba:.0%}", help=f"Seuil d'alerte : {threshold:.0%}")
    st.progress(min(max(proba, 0.0), 1.0))
    if proba >= threshold:
        st.success("Session à fort potentiel : une offre ou une assistance peut être proposée.")
    else:
        st.warning("Achat peu probable d'après le modèle.")
    st.caption("Estimation statistique, à combiner avec le jugement de l'équipe marketing.")
