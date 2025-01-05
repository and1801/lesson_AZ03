from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Импортируем модуль CSV
import csv

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Firefox()

# URL страницы
url = 'https://www.divan.ru/irkutsk/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'ui-LD-ZU') and contains(@class, 'ui-SVNym') and contains(@class, 'bSEDs')]/span[@data-testid='price']")

#<span class="ui-LD-ZU ui-SVNym bSEDs" data-testid="price">55 990<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span>

# Открытие CSV файла для записи
with open('pricesd.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()