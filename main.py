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

str_search = "https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?reff=menu_main"
try:
    driver.get(str_search)

    time.sleep(2)

    try:
        print("Ща")
        button = driver.find_element(By.CLASS_NAME, 'location.ng-tns-c110-1')

        #button = driver.find_element(By.CLASS_NAME, "location ng-tns-c110-1")
        print("Нажимаем кнопку выбора регионов")
        # Нажатие на кнопку
        button.click()

        time.sleep(0.3)
        cities = driver.find_elements(By.CLASS_NAME, "location-select__location")
        for select_sity in cities:
            if select_sity.text == "Саратов":
                button = select_sity
                print("Был выбран Саратов")

        button.click()
    except:
        pass
    time.sleep(0.3)
    n = 1

    try:
        pagesNumbers = driver.find_elements(By.CLASS_NAME, "page-item")
        pagesCount = int(pagesNumbers[-2].find_element(By.TAG_NAME, 'a').text)
        print("Количество страниц " + str(pagesCount))
    except:
        pagesCount = 1
        pass

    dict_prods = {}

    while n <= pagesCount:
        flag_next_iteration = 1
        if(pagesCount > 1):
            driver.get(str_search + "&page=" + str(n))
        else:
            driver.get(str_search)

        time.sleep(0.5)

        last_page_stopper = 0

        items = 0
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

            if len(items) == 0:
                items = driver.find_elements(By.CLASS_NAME, 'product-card__notification-preorder.ng-star-inserted')
                # print("Вычисляем иначе")

            if len(items) == 24:
                break



            last_page_stopper = last_page_stopper + 1
            if n == pagesCount and last_page_stopper == 50:
                break

            if last_page_stopper == 51:
                flag_next_iteration = 0
                print("Сработало превышение")
                print(len(items))
                break


        #items = driver.find_elements(By.TAG_NAME, 'mvid-plp-product-card')
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

        for i in range(len(name_array)):
            if(pagesCount > 1):
                notification_element = items[i].find_elements(By.CLASS_NAME, 'product-notification_black')
                if notification_element:
                    print("Элемент с классом 'product-notification_black' найден")
                    price_array.insert(i, 'Нет в наличии')


            dict_prods[name_array[i]] = price_array[i]

        print('Цикл выполнился', n, 'раз(а)')

        if flag_next_iteration == 1:
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