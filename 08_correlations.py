import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les rendements journaliers des actifs
df = pd.read_csv("rendements_winsorises.csv", index_col='Date', parse_dates=True)

# Sous-périodes
t1 = df.loc['2024-01-02':'2024-10-31']
t2 = df.loc['2024-11-01':'2025-01-31']
t3 = df.loc['2025-02-01':'2025-04-30']

# Fonction pour afficher une heatmap de corrélation
def heatmap_corr(data, title, filename):
    corr = data.corr()
    plt.figure(figsize=(9, 7))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt=".2f")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

# Générer les heatmaps par période
heatmap_corr(t1, "Corrélations croisées – Période T1", "heatmap_corr_T1.png")
heatmap_corr(t2, "Corrélations croisées – Période T2", "heatmap_corr_T2.png")
heatmap_corr(t3, "Corrélations croisées – Période T3", "heatmap_corr_T3.png")
