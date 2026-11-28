"""Étape 6 · Déploiement : estimer, pendant une visite, la probabilité d'achat d'une session.

Lancer en local :  streamlit run app.py
Le fichier model.joblib est produit par la partie 6 du notebook synora_projet_ml.ipynb.
Interface : identité Synora (verre sur fond lumineux, logomark Convergence), sans dépendance en plus :
la jauge et les barres sont du SVG/HTML, tous les chiffres viennent de model.joblib.
"""
import math
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
VISITOR_NAMES = {"New_Visitor": "Nouveaux visiteurs", "Returning_Visitor": "Visiteurs réguliers", "Other": "Autres"}

# (nombre de pages, durée) : une durée sans page vue est incohérente
PAGE_PAIRS = [
    ("Administrative", "Administrative_Duration"),
    ("Informational", "Informational_Duration"),
    ("ProductRelated", "ProductRelated_Duration"),
]
COUNT_COLS = {count for count, _ in PAGE_PAIRS}


def precision_of(metrics):
    """Précision mesurée en partie 5.2 ; un ancien model.joblib ne l'a pas : on la déduit de F1 = 2PR / (P + R)."""
    recall, f1 = metrics["rappel"], metrics["f1"]
    return metrics.get("precision", f1 * recall / (2 * recall - f1))


def limits_text(metrics, recall_by_visitor):
    """Limites affichées à l'utilisateur. Les chiffres viennent de l'évaluation unique sur le test
    (parties 5.2 et 5.3, enregistrés dans model.joblib) : rien n'est écrit à la main (correction E2)."""
    recall, precision = metrics["rappel"], precision_of(metrics)
    returning = recall_by_visitor["Returning_Visitor"]
    new = recall_by_visitor["New_Visitor"]
    return (
        "**Limites du modèle.** Entraîné sur les sessions complètes d'un seul site marchand pendant une année, "
        f"sans janvier ni avril. Sur notre jeu de test, il détecte {recall * 100:.0f} % des acheteurs, "
        f"mais seules {precision * 100:.0f} % de ses alertes correspondent à un vrai achat. "
        f"Il rate surtout les visiteurs réguliers (rappel de {returning * 100:.0f} %, "
        f"contre {new * 100:.0f} % pour les nouveaux visiteurs). "
        "En cours de visite, les pages vues et les durées ne sont pas encore définitives : "
        "l'estimation est plus fiable en fin de visite. "
        "C'est une aide pour cibler une offre ou une assistance, pas une décision automatique : "
        "ne l'utilisez ni pour fixer des prix différents selon la région ou le type de visiteur, "
        "ni sur un autre site sans le réentraîner."
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


def pct(x):
    """38 % au format français (espace insécable avant %)."""
    return f"{x * 100:.0f} %"


def fr(x, digits=2):
    return f"{x:.{digits}f}".replace(".", ",")


# ------------------------------------------------------------------ identité Synora (HTML + SVG)
MARK = ('<svg viewBox="0 0 64 64" width="{s}" height="{s}" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-width="6">'
        '<path d="M8 50C26 50 30 32 46 32" stroke="#5a6384"/><path d="M8 32H46" stroke="#c39dbc"/>'
        '<path d="M8 14C26 14 30 32 46 32" stroke="#4d97ff"/></g><circle cx="50" cy="32" r="7" fill="#f5c04a"/></svg>')

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@200;300;400;600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root{--night:#121624;--glass:rgba(24,29,48,.52);--glass-strong:rgba(20,24,40,.74);--edge:rgba(255,255,255,.16);--hi:rgba(255,255,255,.14);
 --line-strong:#5a6384;--ink:#eef0f6;--muted:#a7acc1;--faint:#8a90a8;--signal:#4d97ff;--signal-strong:#7fb2ff;--on-signal:#08101f;
 --glow:rgba(77,151,255,.32);--dusk:#c39dbc;--amber:#f5c04a;--rose:#ff7a8a;--teal:#43d9b5}
.stApp{background:radial-gradient(34% 46% at 6% 8%,rgba(77,151,255,.5),transparent 70%),radial-gradient(36% 50% at 98% 30%,rgba(195,157,188,.38),transparent 70%),
 radial-gradient(26% 30% at 55% 102%,rgba(245,192,74,.22),transparent 70%),var(--night) !important;background-attachment:fixed !important;color:var(--ink)}
.stApp, .stApp p, .stApp label, .stApp input, .stApp li{font-family:'IBM Plex Sans',system-ui,sans-serif}
[data-testid="stHeader"]{background:transparent}
.block-container{max-width:1280px;padding-top:2.2rem}
h1,h2,h3{font-family:'Sora',system-ui,sans-serif !important;letter-spacing:-.02em}
/* panneaux en verre : formulaire et conteneurs à bordure */
[data-testid="stForm"], [data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"]){
 background:var(--glass) !important;backdrop-filter:blur(24px) saturate(150%);-webkit-backdrop-filter:blur(24px) saturate(150%);
 border:1px solid var(--edge) !important;border-radius:22px !important;box-shadow:inset 0 1px 0 var(--hi),0 30px 80px rgba(0,0,0,.4)}
[data-testid="stForm"]{background:var(--glass-strong) !important;padding:1.4rem 1.4rem 1.2rem}
/* champs */
[data-testid="stNumberInput"] input, [data-baseweb="select"] > div{background:rgba(8,10,20,.45) !important;border-color:var(--line-strong) !important;
 border-radius:10px !important;color:var(--ink) !important;font-variant-numeric:tabular-nums}
[data-testid="stNumberInput"] > div > div, [data-baseweb="input"]{background:transparent !important;border-radius:10px !important}
[data-testid="stNumberInput"] button{background:rgba(255,255,255,.06) !important;border-radius:8px !important;color:var(--muted) !important}
[data-testid="stWidgetLabel"] p{color:var(--muted) !important;font-size:.82rem !important;font-weight:500}
/* bouton principal */
[data-testid="stFormSubmitButton"], [data-testid="stFormSubmitButton"] > div{width:100% !important}
[data-testid="stFormSubmitButton"] button{width:100%;height:3rem;border-radius:12px;background:var(--signal) !important;border:0 !important;
 color:var(--on-signal) !important;font-weight:600;box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 12px 32px var(--glow)}
[data-testid="stFormSubmitButton"] button:hover{background:var(--signal-strong) !important}
[data-testid="stFormSubmitButton"] button p{color:var(--on-signal) !important;font-weight:600}
/* résultat */
[data-testid="stMetric"]{text-align:center}
[data-testid="stMetricLabel"]{justify-content:center}
[data-testid="stMetricLabel"] p{color:var(--muted) !important}
[data-testid="stMetricValue"]{font-family:'Sora',sans-serif !important;font-weight:200 !important;font-size:4.2rem !important;letter-spacing:-.06em;justify-content:center}
/* alertes : limites (info) et refus (error) */
[data-testid="stAlertContainer"]{background:var(--glass-strong) !important;border:1px solid var(--edge) !important;border-radius:16px !important;color:var(--muted) !important}
[data-testid="stAlertContainer"] p{color:var(--muted) !important;font-size:.86rem;line-height:1.6}
[data-testid="stAlertContainer"] strong{color:var(--ink)}
.stAlert:has([data-testid="stAlertContentError"]) [data-testid="stAlertContainer"]{border-color:var(--rose) !important}
.stAlert:has([data-testid="stAlertContentError"]) p{color:#ffd0d6 !important}
/* composants Synora */
.sy-head{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:12px 18px;margin-bottom:1.2rem;border-radius:18px;
 background:var(--glass);backdrop-filter:blur(24px) saturate(150%);border:1px solid var(--edge);box-shadow:inset 0 1px 0 var(--hi)}
.sy-lock{display:flex;align-items:center;gap:10px;font:600 22px 'Sora',sans-serif;letter-spacing:-.8px;color:var(--ink)}
.sy-pill{display:flex;align-items:center;gap:8px;font:500 12px 'IBM Plex Sans',sans-serif;color:var(--muted);border:1px solid var(--edge);border-radius:999px;padding:6px 12px}
.sy-pill b{color:var(--ink);font-weight:500}.sy-pill i{width:7px;height:7px;border-radius:50%;background:var(--teal);box-shadow:0 0 8px var(--teal)}
.stApp p.sy-title{font:600 2.3rem/1.08 'Sora',sans-serif !important;letter-spacing:-.045em;color:var(--ink);margin:.2rem 0 .4rem}
.stApp p.sy-title span{font-weight:300}
.stApp p.sy-lead{color:var(--muted);font-size:.95rem !important;margin-bottom:1rem}
.stApp p.sy-eb{font-size:11px !important}.stApp .sy-ann{font-size:10px !important}
[data-testid="stForm"] h3{font:600 .95rem 'IBM Plex Sans',sans-serif !important;letter-spacing:.02em;color:var(--ink) !important;padding:.3rem 0 .2rem !important}
.sy-eb{font:500 11px 'IBM Plex Sans',sans-serif;letter-spacing:1.6px;color:var(--muted);text-transform:uppercase}
.sy-ann{font:500 10px 'IBM Plex Mono',monospace;letter-spacing:.5px;color:var(--faint);text-transform:uppercase}
.sy-badge{display:inline-flex;align-items:center;gap:7px;font:500 12px 'IBM Plex Sans',sans-serif;padding:5px 12px;border-radius:999px;border:1px solid var(--c);color:var(--c)}
.sy-badge::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--c);box-shadow:0 0 8px var(--c)}
.sy-center{display:flex;justify-content:center}
.sy-scale{position:relative;height:8px;border-radius:999px;background:linear-gradient(90deg,rgba(255,255,255,.07),var(--signal));margin:14px 0 8px}
.sy-scale i{position:absolute;top:-7px;width:3px;height:22px;border-radius:2px}
.sy-row{display:flex;justify-content:space-between}
.sy-kpis{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:.4rem 0}
.sy-k{background:rgba(255,255,255,.05);border:1px solid var(--edge);box-shadow:inset 0 1px 0 var(--hi);border-radius:12px;padding:12px}
.sy-k b{display:block;font:300 1.7rem 'Sora',sans-serif;letter-spacing:-.04em;color:var(--ink)}
.sy-k span{font:500 .8rem 'IBM Plex Sans',sans-serif;color:var(--muted)}
.sy-bar{margin:.6rem 0}.sy-bar .t{position:relative;height:10px;border-radius:999px;background:rgba(255,255,255,.06);margin-top:6px}
.sy-bar .t i{position:absolute;left:0;top:0;bottom:0;border-radius:999px}.sy-bar .t em{position:absolute;top:-5px;width:2px;height:20px;background:var(--amber)}
.sy-bar .l{display:flex;justify-content:space-between;font:400 .88rem 'IBM Plex Sans',sans-serif;color:var(--ink)}
.sy-bar .l b{font:300 1.1rem 'Sora',sans-serif}
.sy-empty{text-align:center;padding:1.4rem .5rem;color:var(--muted)}
.sy-foot{margin-top:1.4rem;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
</style>
"""


def gauge_svg(p, thr, width=360):
    """Demi-jauge : arc de progression (signal) et repère du seuil d'alerte (ambre)."""
    r, cx, cy = 118, 160, 140

    def at(frac, rad=r):
        a = math.radians(180 + 180 * frac)
        return round(cx + rad * math.cos(a), 1), round(cy + rad * math.sin(a), 1)

    sx, sy = at(0)
    ex, ey = at(1)
    vx, vy = at(min(max(p, 0.001), 1))
    t1, t2, tl = at(thr, 100), at(thr, 138), at(thr, 150)
    ticks = "".join(
        f'<line x1="{at(i / 50, 134)[0]}" y1="{at(i / 50, 134)[1]}" x2="{at(i / 50, 141 if i % 5 == 0 else 137)[0]}" '
        f'y2="{at(i / 50, 141 if i % 5 == 0 else 137)[1]}" stroke="#5a6384" stroke-width="{1.4 if i % 5 == 0 else .7}"/>'
        for i in range(51))
    return (f'<svg viewBox="0 0 320 150" width="{width}" role="img" aria-label="Probabilité {pct(p)}, seuil {pct(thr)}">'
            '<defs><filter id="sy-gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter></defs>'
            f'{ticks}<path d="M{sx} {sy}A{r} {r} 0 0 1 {ex} {ey}" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="18" stroke-linecap="round"/>'
            f'<path d="M{sx} {sy}A{r} {r} 0 0 1 {vx} {vy}" fill="none" stroke="rgba(77,151,255,.32)" stroke-width="28" stroke-linecap="round" filter="url(#sy-gl)"/>'
            f'<path d="M{sx} {sy}A{r} {r} 0 0 1 {vx} {vy}" fill="none" stroke="#4d97ff" stroke-width="18" stroke-linecap="round"/>'
            f'<circle cx="{vx}" cy="{vy}" r="5" fill="#eef0f6"/>'
            f'<line x1="{t1[0]}" y1="{t1[1]}" x2="{t2[0]}" y2="{t2[1]}" stroke="#f5c04a" stroke-width="3.5" stroke-linecap="round"/>'
            f'<text x="{tl[0] + 4}" y="{tl[1]}" style="font:500 10px \'IBM Plex Mono\',monospace;fill:#f5c04a">seuil {pct(thr)}</text></svg>')


def html(markup):
    st.markdown(markup, unsafe_allow_html=True)


# ------------------------------------------------------------------ page
st.set_page_config(page_title="Synora · Intention d'achat", page_icon="◐", layout="wide")
html(CSS)
bundle = load_bundle()
pipe, threshold, schema = bundle["pipeline"], bundle["threshold"], bundle["schema"]
metrics = bundle["metrics_test"]
recall_visitors = bundle["rappel_par_groupe"]["VisitorType"]

html(f'<div class="sy-head"><div class="sy-lock">{MARK.format(s=30)}synora</div>'
     f'<span class="sy-pill"><i></i>Modèle : <b>{metrics["modele"].replace("_", " ")}</b> · {bundle["feature_set"].replace("_", " ")} · '
     f'seuil d\'alerte <b>{pct(threshold)}</b></span></div>')

form_col, report_col = st.columns([1.05, 1.2], gap="large")

with form_col:
    html('<p class="sy-eb">Session à estimer</p>'
         '<p class="sy-title">Cette visite va-t-elle se terminer <span>par un achat ?</span></p>'
         '<p class="sy-lead">Décrivez la visite en cours : le modèle estime la probabilité d\'achat.</p>')
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

with report_col:
    html('<p class="sy-eb">Rapport de session</p>')
    with st.container(border=True):
        errors = validate(values) if submitted else []
        if submitted and errors:
            for message in errors:
                st.error(message)
        elif submitted:
            X = pd.DataFrame([values])[bundle["features"]]
            proba = float(pipe.predict_proba(X)[0, 1])
            high_potential = proba >= threshold
            badge = ('<span class="sy-badge" style="--c:#43d9b5">Fort potentiel</span>' if high_potential
                     else '<span class="sy-badge" style="--c:#ff7a8a">Peu probable</span>')
            html(f'<div class="sy-row" style="align-items:center">{badge}<span class="sy-ann">test unique · partie 5.2</span></div>'
                 f'<div class="sy-center">{gauge_svg(proba, threshold)}</div>')
            st.metric("Probabilité d'achat estimée", f"{proba:.0%}", help=f"Seuil d'alerte : {threshold:.0%}")
            verdict = ("Session à fort potentiel : une offre ou une assistance peut être proposée." if high_potential
                       else "Achat peu probable d'après le modèle : aucune offre n'est déclenchée.")
            html(f'<div class="sy-scale"><i style="left:{min(proba, 1) * 100:.1f}%;background:#eef0f6;box-shadow:0 0 10px rgba(77,151,255,.5)"></i>'
                 f'<i style="left:{threshold * 100:.1f}%;background:#f5c04a"></i></div>'
                 f'<div class="sy-row sy-ann"><span>Faible</span><span>seuil {pct(threshold)}</span><span>Forte</span></div>'
                 f'<p style="margin-top:.8rem;color:var(--ink)">{verdict}</p>')
        else:
            html(f'<div class="sy-empty">{MARK.format(s=44)}<p style="margin-top:.6rem">Renseignez la session à gauche, '
                 'puis cliquez sur <b style="color:var(--ink)">Estimer la probabilité d\'achat</b>.</p>'
                 '<p class="sy-ann" style="margin-top:.4rem">Une session sans page vue est refusée.</p></div>')

    html(f'<p class="sy-eb" style="margin-top:1.2rem">Qualité du modèle · jeu de test</p>'
         f'<div class="sy-kpis"><div class="sy-k"><b>{pct(metrics["rappel"])}</b><span>Rappel</span></div>'
         f'<div class="sy-k"><b>{pct(precision_of(metrics))}</b><span>Précision</span></div>'
         f'<div class="sy-k"><b>{fr(metrics["f1"])}</b><span>F1</span></div>'
         f'<div class="sy-k"><b>{fr(metrics["auc"])}</b><span>AUC</span></div></div>')
    bars = "".join(
        f'<div class="sy-bar"><div class="l"><span>{VISITOR_NAMES.get(k, k)}</span><b>{pct(v)}</b></div>'
        f'<div class="t"><i style="width:{v * 100:.1f}%;background:{"#43d9b5" if v >= metrics["rappel"] else "#4d97ff"}"></i>'
        f'<em style="left:{metrics["rappel"] * 100:.1f}%"></em></div></div>'
        for k, v in sorted(recall_visitors.items(), key=lambda kv: -kv[1]) if k in VISITOR_NAMES)
    html(f'<p class="sy-eb" style="margin-top:1rem">Rappel par type de visiteur</p>{bars}'
         f'<p class="sy-ann">Trait doré : rappel global {pct(metrics["rappel"])} · partie 5.3</p>')
    st.info(limits_text(metrics, recall_visitors))

html('<div class="sy-foot"><span class="sy-ann">Synora · projet ML L3 GLSI · IIT Sfax</span>'
     '<span class="sy-ann">Estimation statistique, à combiner avec le jugement de l\'équipe marketing</span></div>')
