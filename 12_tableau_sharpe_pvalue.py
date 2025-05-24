import pandas as pd
from scipy.stats import ttest_ind

# Charger indicateurs et rendements
ind = pd.read_csv("indicateurs_portefeuilles.csv", index_col=0)
rendements = pd.read_csv("rendements_portefeuilles.csv", index_col='Date', parse_dates=True)

# Préparer tableau
colonnes = ["Portefeuille",
            "T1 Sharpe", "T1 σ", "T2 Sharpe", "T2 σ", "T3 Sharpe", "T3 σ",
            "Δ T1", "Δ T2", "Δ T3",
            "p-val T1", "p-val T2", "p-val T3"]

lignes = []
ref = "Ref_60_40"
portfolios = ind.index.tolist()

for pf in portfolios:
    row = [pf]

    # Sharpe et σ
    for period in ["T1", "T2", "T3"]:
        row.append(ind.loc[pf, f"{period}_Sharpe"])
        row.append(ind.loc[pf, f"{period}_Volatilité"])

    # Δ vs 60/40
    for period in ["T1", "T2", "T3"]:
        delta = ind.loc[pf, f"{period}_Sharpe"] - ind.loc[ref, f"{period}_Sharpe"]
        row.append(delta)

    # p-values Welch
    for period, df_slice in zip(
        ["T1", "T2", "T3"],
        [rendements.loc["2024-01-02":"2024-10-31"],
         rendements.loc["2024-11-01":"2025-01-31"],
         rendements.loc["2025-02-01":"2025-04-30"]]):
        stat, p = ttest_ind(df_slice[pf], df_slice[ref], equal_var=False, nan_policy="omit")
        row.append(p)

    lignes.append(row)

tableau = pd.DataFrame(lignes, columns=colonnes)
tableau.to_csv("tableau_sharpe.csv", index=False)
print(tableau.round(3))
