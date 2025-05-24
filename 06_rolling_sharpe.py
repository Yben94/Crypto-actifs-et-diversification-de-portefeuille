import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("rendements_portefeuilles.csv", index_col='Date', parse_dates=True)

window = 30
risk_free = 0.0002
rolling_sharpe = pd.DataFrame(index=df.index)

# Calcul Sharpe rolling
for col in df.columns:
    excess = df[col] - risk_free
    mean = excess.rolling(window).mean()
    std = df[col].rolling(window).std()
    rolling_sharpe[col] = (mean / std) * np.sqrt(252)

# Repères temporels (élection, investiture)
repere1 = pd.to_datetime("2024-11-05")  # élection US (mardi 5 novembre 2024)
repere2 = pd.to_datetime("2025-01-20")  # investiture (lundi 20 janvier 2025)

def tracer(courbes, titre, filename):
    plt.figure(figsize=(12, 6))
    for col in courbes:
        plt.plot(rolling_sharpe.index, rolling_sharpe[col], label=col, linewidth=2 if "Ref" in col else 1)

    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    plt.axvline(repere1, color='red', linestyle='--', label='Élection')
    plt.axvline(repere2, color='orange', linestyle='--', label='Investiture')

    plt.title(titre)
    plt.ylabel("Sharpe annualisé (rolling 30j)")
    plt.xlabel("Date")
    plt.legend(loc='upper right', fontsize=9)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

# Groupe 1
tracer(['Ref_60_40', 'Bitcoin_10', 'Ethereum_10', 'BTC_USDT_5_5'],
       "Rolling Sharpe – Groupe Bitcoin & Référence", "rolling_sharpe_groupe1.png")

# Groupe 2
tracer(['UNI_10', 'BNB_10', 'USDT_10'],
       "Rolling Sharpe – Groupe Spéculatif / Stablecoin", "rolling_sharpe_groupe2.png")
