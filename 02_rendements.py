import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize

# Charger les prix journaliers depuis le CSV
df_prix = pd.read_csv("prix_journaliers.csv", parse_dates=['Date'], index_col='Date')

# Calculer les rendements arithmétiques
rendements = df_prix.pct_change().dropna()

# Winsorisation à 1 % - 99 %
rendements_winsor = rendements.copy()
for col in rendements.columns:
    rendements_winsor[col] = winsorize(rendements[col], limits=[0.01, 0.01])

# Afficher un aperçu
print(rendements_winsor.head())

# Sauvegarder les rendements winsorisés dans un nouveau fichier
rendements_winsor.to_csv("rendements_winsorises.csv")
