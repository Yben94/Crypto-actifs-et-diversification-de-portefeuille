import pandas as pd

# Charger les rendements nettoyés
rendements = pd.read_csv("rendements_winsorises.csv", index_col='Date', parse_dates=True)

# Définir les portefeuilles
portefeuilles = {}

# Portefeuille référence 60/40
portefeuilles['Ref_60_40'] = 0.60 * rendements['S&P500'] + 0.40 * rendements['Obligations']

# Portefeuilles avec crypto (10 % crypto, 54 % actions, 36 % obligations)
crypto_actifs = ['Bitcoin', 'Ethereum', 'BNB', 'UNI', 'USDT']
for actif in crypto_actifs:
    nom = f"{actif}_10"
    portefeuilles[nom] = (
        0.54 * rendements['S&P500']
        + 0.36 * rendements['Obligations']
        + 0.10 * rendements[actif]
    )

# Portefeuille mixte BTC + USDT (5 % chacun)
portefeuilles['BTC_USDT_5_5'] = (
    0.54 * rendements['S&P500']
    + 0.36 * rendements['Obligations']
    + 0.05 * rendements['Bitcoin']
    + 0.05 * rendements['USDT']
)

# Fusionner tous les portefeuilles dans un DataFrame
df_portefeuilles = pd.DataFrame(portefeuilles)

# Afficher un aperçu
print(df_portefeuilles.head())

# Sauvegarder
df_portefeuilles.to_csv("rendements_portefeuilles.csv")
