import pandas as pd

# Charger les résultats calculés
df_indicateurs = pd.read_csv("indicateurs_portefeuilles.csv", index_col=0)

# === H1 – BTC : corrélation manuelle extraite de T2 heatmap ===
btc_corr_T2 = 0.45  # corrélation BTC-S&P500 période T2, relevée sur la heatmap
sharpe_btc_T2 = df_indicateurs.loc["Bitcoin_10", "T2_Sharpe"]
sharpe_ref_T2 = df_indicateurs.loc["Ref_60_40", "T2_Sharpe"]

h1_corr_ok = btc_corr_T2 < 0.30
h1_sharpe_ok = sharpe_btc_T2 > sharpe_ref_T2
h1_verdict = "Validée" if (h1_corr_ok and h1_sharpe_ok) else \
             "Partiellement validée" if h1_sharpe_ok else "Non validée"

# === H2 – USDT : CVaR(USDT) < CVaR(Ref) sur T1, T2, T3 ===
usdt_cvar = df_indicateurs.loc["USDT_10", ["T1_CVaR", "T2_CVaR", "T3_CVaR"]]
ref_cvar = df_indicateurs.loc["Ref_60_40", ["T1_CVaR", "T2_CVaR", "T3_CVaR"]]
comparaison = usdt_cvar < ref_cvar

if comparaison.all():
    h2_verdict = "Validée"
elif comparaison.any():
    h2_verdict = "Partiellement validée"
else:
    h2_verdict = "Non validée"

# === H3 – UNI & BNB : Sharpe < Ref et CVaR > Ref en T2 ===
def evaluer_H3(actif):
    sharpe_bad = df_indicateurs.loc[f"{actif}_10", "T2_Sharpe"] < df_indicateurs.loc["Ref_60_40", "T2_Sharpe"]
    cvar_bad = df_indicateurs.loc[f"{actif}_10", "T2_CVaR"] > df_indicateurs.loc["Ref_60_40", "T2_CVaR"]
    return sharpe_bad and cvar_bad

h3_uni = evaluer_H3("UNI")
h3_bnb = evaluer_H3("BNB")

if h3_uni and h3_bnb:
    h3_verdict = "Validée"
elif h3_uni or h3_bnb:
    h3_verdict = "Partiellement validée"
else:
    h3_verdict = "Non validée"

# === Créer tableau récapitulatif ===
tableau = pd.DataFrame({
    "Hypothèse": ["H1 – BTC/ETH", "H2 – USDT", "H3 – UNI/BNB"],
    "Critère de validation": [
        "Corrélation < 0.30 et Sharpe T2 > Ref",
        "CVaR(USDT_10) < Ref sur T1, T2, T3",
        "Sharpe < Ref et CVaR > Ref en T2"
    ],
    "Résultat empirique": [
        f"Corrélation = {btc_corr_T2:.2f}; Sharpe BTC = {sharpe_btc_T2:.2f} > Ref = {sharpe_ref_T2:.2f}",
        f"CVaR(USDT_10) < Ref : {comparaison.tolist()}",
        f"UNI: {h3_uni}, BNB: {h3_bnb}"
    ],
    "Verdict": [h1_verdict, h2_verdict, h3_verdict]
})

# Afficher et sauvegarder
print("\nValidation synthétique des hypothèses :\n")
print(tableau)
tableau.to_csv("validation_hypotheses.csv", index=False)
