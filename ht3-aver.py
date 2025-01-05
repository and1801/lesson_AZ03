import pandas as pd
import matplotlib.pyplot as plt

# Путь к файлу CSV
file_path = 'pricesd.csv'

# Чтение данных из CSV-файла
data = pd.read_csv(file_path)

# Удаление пробелов из строковых представлений чисел
data['Price'] = data['Price'].str.replace(' ', '')

# Преобразование столбца 'Price' в числовой формат
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Удаление NaN значений, если они есть
data = data.dropna(subset=['Price'])

# Вычисление среднего значения
average_price = data['Price'].mean()

# Вывод среднего значения
print(f'Средняя цена: {average_price}')