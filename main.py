from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import Parser2
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()


options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-features=SameSiteByDefaultCookies")
options.add_argument("--disable-features=CrossSiteDocumentBlockingIfIsolating")
options.add_argument("--disable-features=CrossSiteDocumentBlockingAlways")
options.add_argument("--disable-features=SameSiteDefaultChecksMethodRigorously")
options.add_argument("--headless")  # Опционально: запуск в безголовом режиме
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("cookie=domain=.mvideo.ru; SameSite=None; Secure")  # Установка куки с доменом .mvideo.ru



s = Service(executable_path="/path/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get("https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search")

    time.sleep(2)

    pagesNumbers = driver.find_elements(By.CLASS_NAME, "page-item")
    pagesCount = int(pagesNumbers[-2].find_element(By.TAG_NAME, 'a').text)
    print("Количество страниц " + str(pagesCount))
    n = 1
    while n <= pagesCount:
        #driver.get("https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65/f/tolko-v-nalichii=da?from=under_search&page=" + str(n))
        cookies = driver.get_cookies()
        #print(cookies)
        cookies_to_extract = [
            '__hash_',
            '__lhash_',
            'MVID_ALFA_PODELI_NEW',
            'MVID_BLACK_FRIDAY_ENABLED',
            'MVID_CASCADE_CMN',
            'MVID_CATALOG_STATE',
            'MVID_CHECKOUT_STORE_SORTING',
            'MVID_CITY_ID',
            'MVID_CREDIT_SERVICES',
            'MVID_CRITICAL_GTM_INIT_DELAY',
            'MVID_FILTER_CODES',
            'MVID_FILTER_TOOLTIP',
            'MVID_FLOCKTORY_ON',
            'MVID_GEOLOCATION_NEEDED',
            'MVID_GIFT_KIT',
            'MVID_GTM_ENABLED',
            'MVID_INTERVAL_DELIVERY',
            'MVID_IS_NEW_BR_WIDGET',
            'MVID_KLADR_ID',
            'MVID_LAYOUT_TYPE',
            'MVID_LP_SOLD_VARIANTS',
            'MVID_MCLICK',
            'MVID_MINDBOX_DYNAMICALLY',
            'MVID_MINI_PDP',
            'MVID_NEW_ACCESSORY',
            'MVID_NEW_LK_CHECK_CAPTCHA',
            'MVID_NEW_LK_OTP_TIMER',
            'MVID_NEW_MBONUS_BLOCK',
            'MVID_PODELI_PDP',
            'MVID_PROMO_CATALOG_ON',
            'MVID_REGION_ID',
            'MVID_REGION_SHOP',
            'MVID_SERVICES',
            'MVID_SP',
            'MVID_TIMEZONE_OFFSET',
            'MVID_TYP_CHAT',
            'MVID_WEB_SBP',
            'SENTRY_ERRORS_RATE',
            'SENTRY_TRANSACTIONS_RATE',
            'MVID_ENVCLOUD',
            'gsscgib-w-mvideo',
            'gsscgib-w-mvideo',
            '_ga_CFMZTSS5FM',
            '_sp_ses.d61c',
            '_sp_id.d61c',
            '_ga_BNX5WPP3YK',
            '_ym_uid',
            '_ym_d',
            '_ga',
            '_gid',
            '_dc_gtm_UA-1873769-1',
            '_ym_isad',
            '_dc_gtm_UA-1873769-37',
            'tmr_lvid',
            'tmr_lvidTS',
            'tmr_detect',
            'uxs_uid',
            'advcake_track_id',
            'advcake_session_id',
            'flocktory-uuid',
            'flacktory',
            'BIGipServeratg-ps-prod_tcp80',
            'bIPs',
            'afUserId',
            'AF_SYNC',
            'fgsscgib-w-mvideo',
            'fgsscgib-w-mvideo',
            'gssc218',
            'cfidsgib-w-mvideo'
        ]
        cookies_dict = {}

        for cookie_name in cookies_to_extract:
            found_cookie = next((cookie for cookie in cookies if cookie['name'] == cookie_name), None)
            if found_cookie:
                cookies_dict[cookie_name] = found_cookie['value']
        #     else:
        #          print(f"Куки по имени '{cookie_name}' не найден")
        #
        # print(cookies_dict)


        time.sleep(2)
        Parser2.get_data(n, cookies_dict)

        print('Цикл выполнился', n, 'раз(а)')
        n = n + 1


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()