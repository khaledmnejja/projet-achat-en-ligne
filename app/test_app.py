"""Tests de l'application (étape 6). Lancer depuis le dossier app/ :  python -m pytest test_app.py

Ils vérifient que le modèle se charge, que les saisies impossibles sont refusées
et qu'une saisie normale donne une probabilité accompagnée du seuil.
"""
from pathlib import Path

import joblib
import pytest
from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).parent / "app.py")
BUNDLE = joblib.load(Path(__file__).parent / "model.joblib")


def run_app():
    at = AppTest.from_file(APP, default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    return at


def set_number(at, label, value):
    next(w for w in at.number_input if w.label == label).set_value(value)


def submit(at):
    next(b for b in at.button if b.label.startswith("Estimer")).click()
    at.run()
    assert not at.exception, at.exception
    return at


def test_bundle_coherent():
    assert BUNDLE["feature_set"] == "sans_PageValues"
    assert "PageValues" not in BUNDLE["features"]
    assert 0 < BUNDLE["threshold"] < 1
    assert set(BUNDLE["rappel_par_groupe"]["VisitorType"]) >= {"New_Visitor", "Returning_Visitor"}


def test_limits_come_from_the_model():
    at = run_app()
    text = at.info[0].value
    recall = BUNDLE["metrics_test"]["rappel"]
    assert f"{recall * 100:.0f} % des acheteurs" in text
    returning = BUNDLE["rappel_par_groupe"]["VisitorType"]["Returning_Visitor"]
    assert f"rappel de {returning * 100:.0f} %" in text
    if "precision" in BUNDLE["metrics_test"]:   # export de S5 : précision mesurée en 5.2
        assert f"seules {BUNDLE['metrics_test']['precision'] * 100:.0f} %" in text


def test_session_without_page_is_refused():
    at = submit(run_app())
    assert any("au moins une page" in e.value for e in at.error)
    assert not at.metric


def test_duration_without_page_is_refused():
    at = run_app()
    set_number(at, "Pages produits vues", 3)
    set_number(at, "Temps sur les pages administratives (s)", 120.0)
    at = submit(at)
    assert any("impossible sans page vue" in e.value for e in at.error)
    assert not at.metric


@pytest.mark.parametrize("pages, seconds", [(12, 482.5), (60, 3600.0)])
def test_normal_session_gets_a_probability(pages, seconds):
    at = run_app()
    set_number(at, "Pages produits vues", pages)
    set_number(at, "Temps sur les pages produits (s)", seconds)
    at = submit(at)
    assert not at.error
    value = at.metric[0].value
    assert value.endswith("%") and 0 <= int(value.rstrip("%")) <= 100
