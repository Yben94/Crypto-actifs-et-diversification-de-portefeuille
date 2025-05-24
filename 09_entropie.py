import numpy as np
import pandas as pd

# Définir les pondérations des portefeuilles (de manière explicite)
portefeuilles = {
    "Ref_60_40": [0.6, 0.4],
    "Bitcoin_10": [0.54, 0.36, 0.10],
    "Ethereum_10": [0.54, 0.36, 0.10],
    "BNB_10": [0.54, 0.36, 0.10],
    "UNI_10": [0.54, 0.36, 0.10],
    "USDT_10": [0.54, 0.36, 0.10],
    "BTC_USDT_5_5": [0.54, 0.36, 0.05, 0.05]
}

# Fonction entropie de Shannon
def shannon_entropy(weights):
    weights = np.array(weights)
    return -np.sum(weights * np.log(weights))

# Calculer l'entropie de chaque portefeuille
entropie = {nom: shannon_entropy(poids) for nom, poids in portefeuilles.items()}

# Sauvegarder les résultats
df_entropie = pd.DataFrame.from_dict(entropie, orient='index', columns=["Entropie"])
df_entropie.index.name = "Portefeuille"
df_entropie = df_entropie.sort_values(by="Entropie", ascending=False)
print(df_entropie)

df_entropie.to_csv("entropie_portefeuilles.csv")
