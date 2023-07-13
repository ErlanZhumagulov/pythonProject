import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()


options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")  # Опционально: запуск в безголовом режиме

s = Service(executable_path="/path/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get("https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search")

    time.sleep(2)

    pagesNumbers = driver.find_elements(By.CLASS_NAME, "page-item")
    pagesCount = int(pagesNumbers[-2].find_element(By.TAG_NAME, 'a').text)
    print("Количество страниц " + str(pagesCount))

    dict_prods = {}

    n = 1
    while n <= pagesCount:
        driver.get("https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65/f/tolko-v-nalichii=da?from=under_search&page=" + str(n))

        time.sleep(2)

        page_height = driver.execute_script("return document.body.scrollHeight")
        print(page_height)

        item_count_buf = 0
        # Получение высоты страницы

        last_page_stopper = 0
        while True:
            try:
                button = driver.find_element(By.CLASS_NAME, "mobile-notification__button")
                # Нажатие на кнопку
                button.click()
            except:
                pass

            # Прокрутка на 100 пикселей вверх
            driver.execute_script("window.scrollBy(0, +300);")

            # Пауза для прогрузки элементов
            time.sleep(0.2)



            items = driver.find_elements(By.TAG_NAME, 'mvid-plp-product-card')
            if len(items) == 24:
                break

            last_page_stopper = last_page_stopper + 1
            if n == pagesCount and last_page_stopper == 24:
                break

        items = driver.find_elements(By.TAG_NAME, 'mvid-plp-product-card')
        prices = driver.find_elements(By.CLASS_NAME, 'price__main-value')
        names = driver.find_elements(By.CLASS_NAME, 'product-title__text')
        price_array = [price.text for price in prices]
        name_array = [name.text for name in names]
        for i in range(len(name_array)):
            name_array[i] = name_array[i].replace('"', '').replace("'", '')
        print("Ниже цены")
        print(name_array)
        print(price_array)
        print(len(items))
        print(len(price_array))
        print(len(name_array))

        for i in range(len(items)):
            notification_element = items[i].find_elements(By.CLASS_NAME, 'product-notification_black')
            if notification_element:
                print("Элемент с классом 'product-notification_black' найден")
                price_array.insert(i, 'Нет в наличии')


            dict_prods[name_array[i]] = price_array[i]

        # Вывод массива значений содержимого



        #print(items)

        print('Цикл выполнился', n, 'раз(а)')
        n = n + 1

    filename = 'parse_result.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Наименование', 'Цена'])

        for item, price in dict_prods.items():
            writer.writerow([item, price])


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()