import pandas as pd
import matplotlib.pyplot as plt

# Charger les rendements journaliers
rendements = pd.read_csv("rendements_portefeuilles.csv", index_col='Date', parse_dates=True)

# Charger les CVaR calculées
indicateurs = pd.read_csv("indicateurs_portefeuilles.csv", index_col=0)

# Calcul des rendements annuels moyens
rendement_annuel = rendements.mean() * 252

# On prend les CVaR de T2 comme période critique
cvar_t2 = indicateurs["T2_CVaR"]

# Création du scatterplot
plt.figure(figsize=(10, 6))
for portefeuille in rendement_annuel.index:
    x = rendement_annuel[portefeuille]
    y = cvar_t2[portefeuille]
    plt.scatter(x, y, label=portefeuille)
    plt.text(x, y, portefeuille, fontsize=8, ha='right')

plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.title("Rendement annuel moyen vs CVaR 95 % (T2)")
plt.xlabel("Rendement annuel moyen")
plt.ylabel("CVaR 95 % (pire 5 % des jours)")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_cvar_rendement.png", dpi=300)
plt.show()
