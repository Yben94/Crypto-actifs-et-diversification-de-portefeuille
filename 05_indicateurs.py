import pandas as pd
import numpy as np

# === Fonctions de calcul ===

def sharpe_ratio(rendements, risk_free=0.0002):
    excess = rendements.mean() - risk_free
    volatility = rendements.std()
    return (excess / volatility) * np.sqrt(252)

def cvar_95(rendements):
    return rendements[rendements <= rendements.quantile(0.05)].mean()

# === Charger les sous-périodes ===

T1 = pd.read_csv("rendements_T1.csv", index_col='Date', parse_dates=True)
T2 = pd.read_csv("rendements_T2.csv", index_col='Date', parse_dates=True)
T3 = pd.read_csv("rendements_T3.csv", index_col='Date', parse_dates=True)

# === Fonction d'analyse ===

def analyser_periode(df, nom_periode):
    sharpe = sharpe_ratio(df)
    cvar = df.apply(cvar_95)
    vol = df.std() * np.sqrt(252)  # Écart-type annualisé
    resultat = pd.DataFrame({
        f"{nom_periode}_Sharpe": sharpe,
        f"{nom_periode}_CVaR": cvar,
        f"{nom_periode}_Volatilité": vol
    })
    return resultat

# === Exécution sur les 3 périodes ===

result_T1 = analyser_periode(T1, 'T1')
result_T2 = analyser_periode(T2, 'T2')
result_T3 = analyser_periode(T3, 'T3')

# === Fusionner et sauvegarder ===

indicateurs = pd.concat([result_T1, result_T2, result_T3], axis=1)
indicateurs.to_csv("indicateurs_portefeuilles.csv")

# Affichage pour vérification
print("\n=== Résumé des indicateurs calculés ===\n")
print(indicateurs.round(4))
