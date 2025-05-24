import pandas as pd
import matplotlib.pyplot as plt

# Charger les rendements winsorisés
df = pd.read_csv("rendements_winsorises.csv", index_col="Date", parse_dates=True)

# Paramètres
window = 60  # rolling window en jours
ref = "S&P500"
assets = ["Bitcoin", "Ethereum"]

# Calcul rolling corrélations
rolling_corr = pd.DataFrame(index=df.index)
for asset in assets:
    rolling_corr[f"{asset}_vs_{ref}"] = df[asset].rolling(window).corr(df[ref])

# Tracer
plt.figure(figsize=(12, 6))
for col in rolling_corr.columns:
    plt.plot(rolling_corr.index, rolling_corr[col], label=col.replace("_vs_", " / "))

plt.axhline(0.3, color='red', linestyle='--', linewidth=1, label="Seuil critique 0.3")
plt.title("Corrélations glissantes 60 jours – BTC & ETH vs S&P500")
plt.xlabel("Date")
plt.ylabel("Corrélation (ρ)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("rolling_correlation_crypto_sp500.png", dpi=300)
plt.show()
