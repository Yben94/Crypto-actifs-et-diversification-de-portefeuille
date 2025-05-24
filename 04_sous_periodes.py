import pandas as pd

# Charger les rendements journaliers des portefeuilles
rendements = pd.read_csv("rendements_portefeuilles.csv", index_col='Date', parse_dates=True)

# Définir les dates des sous-périodes
t1_start, t1_end = '2024-01-02', '2024-10-31'
t2_start, t2_end = '2024-11-01', '2025-01-31'
t3_start, t3_end = '2025-02-01', '2025-04-30'

# Filtrer les sous-périodes
T1 = rendements.loc[t1_start:t1_end]
T2 = rendements.loc[t2_start:t2_end]
T3 = rendements.loc[t3_start:t3_end]

# Sauvegarder chaque sous-période
T1.to_csv("rendements_T1.csv")
T2.to_csv("rendements_T2.csv")
T3.to_csv("rendements_T3.csv")

# Vérification rapide
print("Période T1 :", T1.shape)
print("Période T2 :", T2.shape)
print("Période T3 :", T3.shape)
