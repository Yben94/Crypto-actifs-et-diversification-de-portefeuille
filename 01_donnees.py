import yfinance as yf
import pandas as pd

# Liste des actifs et leurs symboles
tickers = {
    'S&P500': '^GSPC',
    'Obligations': 'IEF',
    'Bitcoin': 'BTC-USD',
    'Ethereum': 'ETH-USD',
    'BNB': 'BNB-USD',
    'UNI': 'UNI-USD',
    'USDT': 'USDT-USD'
}

# Dates de début et fin de la période d'étude
start_date = '2024-01-01'
end_date = '2025-04-30'

# Télécharger les données de clôture
data = {}
for name, ticker in tickers.items():
    print(f"Téléchargement de {name}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    if 'Adj Close' in df.columns:
        data[name] = df['Adj Close']
    else:
        data[name] = df['Close']


# Fusionner dans une seule table
prix = pd.concat(data.values(), axis=1)
prix.columns = data.keys()

# Afficher un aperçu
print(prix.head())

# Sauvegarder dans un fichier CSV
prix.to_csv("prix_journaliers.csv")
