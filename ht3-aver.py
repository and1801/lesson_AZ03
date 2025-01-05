import pandas as pd



file_path = 'pricesd.csv'
data = pd.read_csv(file_path)

data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

data = data.dropna(subset=['Price'])

ap = data['Price'].mean()

print(ap)