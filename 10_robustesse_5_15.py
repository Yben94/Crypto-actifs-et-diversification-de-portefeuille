import pandas as pd

# Charger les rendements winsorisés
rendements = pd.read_csv("rendements_winsorises.csv", index_col='Date', parse_dates=True)

# Définir les pondérations pour chaque scénario
scenarios = {
    "Ref_60_40": [("S&P500", 0.6), ("Obligations", 0.4)],
    "Crypto_5": [("S&P500", 0.57), ("Obligations", 0.38), ("Crypto", 0.05)],
    "Crypto_10": [("S&P500", 0.54), ("Obligations", 0.36), ("Crypto", 0.10)],
    "Crypto_15": [("S&P500", 0.51), ("Obligations", 0.34), ("Crypto", 0.15)]
}

# Liste des actifs crypto à tester
cryptos = ["Bitcoin", "Ethereum", "BNB", "UNI", "USDT"]

# Calculer les portefeuilles simulés
resultats = {}
for crypto in cryptos:
    for scenario, alloc in scenarios.items():
        nom_portefeuille = f"{crypto}_{scenario}"
        rend = (
            rendements[alloc[0][0]] * alloc[0][1] +
            rendements[alloc[1][0]] * alloc[1][1]
        )
        if "Crypto" in scenario:
            rend += rendements[crypto] * alloc[2][1]
        resultats[nom_portefeuille] = rend

# Mettre en DataFrame
df = pd.DataFrame(resultats)

# Calculer les Sharpe ratios (annualisés)
risk_free = 0.0002
sharpe = ((df.mean() - risk_free) / df.std()) * (252**0.5)
sharpe.name = "Sharpe"

# Sauvegarder
sharpe.to_csv("robustesse_sharpe_5_10_15.csv")
print(sharpe.sort_values(ascending=False))
