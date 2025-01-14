from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Импортируем модуль CSV
import csv

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Firefox()

# URL страницы
url = 'https://tehnotezis.ru/catalog/raskhodnye_materialy/kartridzhi_dlya_printerov/'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(20)


prices = driver.find_elements(By.CLASS_NAME, 'price_value')



# Открытие CSV файла для записи
with open('pricesd.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()