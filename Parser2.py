import requests

import csv


def get_data(page, cookies_dict):
    import requests

    cookies = {
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_6267',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2300000700000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '55',
        'MVID_REGION_SHOP': 'S928',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_ym_uid': '1688477596533287953',
        '_ym_d': '1688477596',
        'tmr_lvid': 'c876c8a3aa647a5f5fcbcb24fb92e212',
        'tmr_lvidTS': '1688477599829',
        'advcake_session_id': '34db6fb8-ea77-4b20-d6a6-833ca571a69b',
        'afUserId': 'de9c9f90-be7d-40de-a42e-05ae9d85baf9-p',
        'uxs_uid': '582006d0-1a6f-11ee-b68f-e1fd943ddd42',
        'flocktory-uuid': 'b464727d-352a-47a6-a302-004920f95f09-0',
        '__lhash_': 'c82abc25c08bb5139495a2bbc4d46ce8',
        'MVID_PODELI_PDP': 'true',
        'MVID_SERVICES': '111',
        '_gid': 'GA1.2.1062719037.1689100065',
        'AF_SYNC': '1689100070895',
        'partnerSrc': 'yandex',
        '__cpatrack': 'yandex_organic',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'advcake_track_id': '6f209995-efaa-eb09-2726-ccf433e8b76f',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex',
        'advcake_utm_partner': 'yandex',
        'advcake_utm_webmaster': '',
        'advcake_click_id': '',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        '_ym_isad': '2',
        'MVID_SP': 'true',
        'MVID_ENVCLOUD': 'prod1',
        'SMSError': '',
        'authError': '',
        '__js_p_': '172,1800,0,1,0',
        '_sp_id.d61c': '141bcadc-d675-4b25-8bd9-1c9dcbecb117.1688477596.17.1689242985.1689189411.6ae3044e-b670-4645-bcf1-78c9fe258fd3.4710dc12-99db-4012-a828-4df1da75632a.8d26692d-0b29-45c1-9faf-9af219eb5178.1689235871533.97',
        '_ga_CFMZTSS5FM': 'GS1.1.1689235871.17.1.1689242985.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1689235871.17.1.1689242985.60.0.0',
        'mindboxDeviceUUID': 'dac89675-e94a-4a4a-bf07-7765e74f9ea9',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22dac89675-e94a-4a4a-bf07-7765e74f9ea9%22%7D',
        '_ga': 'GA1.2.1703219727.1688477596',
        'tmr_detect': '0%7C1689242989778',
        'gsscgib-w-mvideo': 'WW0rGCZAoJTKjhmle5hYGKamg9IJIycNSMEqDFfdYzoFDGJyylo46mIw+zXC/upqmhYeoplkllNvtkuRDNLMiFEdKqAmy3HSC9rUUzN4FjVIjbINdndwe0ZlcU8J/6GeIKLGZ50+F4DiwPyQqUsPoQ9CTZaggkibAiT3IAAZm1aS/gbi0bDVkwpitXZbvlEN24F0umHPp9OnahChktfc2a9SS+HJtmBRe/xPOpjkFUlWlRmPFfKKh+aQUCMvhFr/EuywSP33iNIlFXg9lFYM',
        'gsscgib-w-mvideo': 'WW0rGCZAoJTKjhmle5hYGKamg9IJIycNSMEqDFfdYzoFDGJyylo46mIw+zXC/upqmhYeoplkllNvtkuRDNLMiFEdKqAmy3HSC9rUUzN4FjVIjbINdndwe0ZlcU8J/6GeIKLGZ50+F4DiwPyQqUsPoQ9CTZaggkibAiT3IAAZm1aS/gbi0bDVkwpitXZbvlEN24F0umHPp9OnahChktfc2a9SS+HJtmBRe/xPOpjkFUlWlRmPFfKKh+aQUCMvhFr/EuywSP33iNIlFXg9lFYM',
        'fgsscgib-w-mvideo': 'iZlt8bf4a9d7f879652aec973f6abf83361e45fb',
        'fgsscgib-w-mvideo': 'iZlt8bf4a9d7f879652aec973f6abf83361e45fb',
        '__hash_': '6371f609cf7ac13b175705878ee8d595',
        'gssc218': '',
        'cfidsgib-w-mvideo': '/81q8DGj8MasZB+dq+bfhO05/wChnWB2XJSn8MAn7h0guuU6/fp5ZiCHBga7mCb334kDOz0/zRN3IhRwD1fKPEfPisue0Av1EINz2t4SHvBYTC74lzQD7oADtLjt0xaRbndeY9epeM6vAfPB8+IH3WfDhTEOvolPBYEAm5Zp',
    }



    #cookies.update(cookies_dict)
    #print(cookies)
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=1be3bf8d45484f37aadb4ae8c34841df,sentry-sample_rate=0.5',
        # 'cookie': 'MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_6267; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000700000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=55; MVID_REGION_SHOP=S928; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _ym_uid=1688477596533287953; _ym_d=1688477596; tmr_lvid=c876c8a3aa647a5f5fcbcb24fb92e212; tmr_lvidTS=1688477599829; advcake_session_id=34db6fb8-ea77-4b20-d6a6-833ca571a69b; afUserId=de9c9f90-be7d-40de-a42e-05ae9d85baf9-p; uxs_uid=582006d0-1a6f-11ee-b68f-e1fd943ddd42; flocktory-uuid=b464727d-352a-47a6-a302-004920f95f09-0; __lhash_=c82abc25c08bb5139495a2bbc4d46ce8; MVID_PODELI_PDP=true; MVID_SERVICES=111; _gid=GA1.2.1062719037.1689100065; AF_SYNC=1689100070895; partnerSrc=yandex; __cpatrack=yandex_organic; __sourceid=yandex; __allsource=yandex; advcake_track_id=6f209995-efaa-eb09-2726-ccf433e8b76f; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex; advcake_utm_partner=yandex; advcake_utm_webmaster=; advcake_click_id=; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; _ym_isad=2; MVID_SP=true; MVID_ENVCLOUD=prod1; _sp_ses.d61c=*; SMSError=; authError=; __js_p_=534,1800,0,1,0; __jhash_=433; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20YaBrowser%2F23.5.4.674%20Yowser%2F2.5%20Safari%2F537.36; __hash_=9abbf6ec5856213a77517d50b085e4d4; mindboxDeviceUUID=dac89675-e94a-4a4a-bf07-7765e74f9ea9; directCrm-session=%7B%22deviceGuid%22%3A%22dac89675-e94a-4a4a-bf07-7765e74f9ea9%22%7D; tmr_detect=0%7C1689240467131; gssc218=; _dc_gtm_UA-1873769-1=1; _ga_BNX5WPP3YK=GS1.1.1689235871.17.1.1689241081.60.0.0; _ga=GA1.1.1703219727.1688477596; _ga_CFMZTSS5FM=GS1.1.1689235871.17.1.1689241081.0.0.0; _sp_id.d61c=141bcadc-d675-4b25-8bd9-1c9dcbecb117.1688477596.17.1689241082.1689189411.6ae3044e-b670-4645-bcf1-78c9fe258fd3.4710dc12-99db-4012-a828-4df1da75632a.8d26692d-0b29-45c1-9faf-9af219eb5178.1689235871533.55; cfidsgib-w-mvideo=JvuXvZg15nrJ5FET3iuW3kPH62xqhS2UqIYOaCVGsoWLgsLVP6ax4aeEY6I6Pi0Nd0YufjsnreHXmIyRUPs11NiEWbvi6Rrmf3vc0NponQ0s5XwBxZjUbKar8hznRCdTxVw0l70ow7lGkxrvdwafDiimFcUFlsQs1WDLt/A=; fgsscgib-w-mvideo=4wqTd77bc4ee406374fa58d4aed454ea97f41132; fgsscgib-w-mvideo=4wqTd77bc4ee406374fa58d4aed454ea97f41132; gsscgib-w-mvideo=Vjlq9ockyxwJyHPeeWpciCqeYQY+eu749g1Yk+2fuvLgR533JHLC+QMMmCdt2smAPiFW7FbUK6qdZrYBGPZI75eMo2vzTVHRePpQtjrDeiBaCdu33xDQOv8tQwmiw98oiDnc9K8IX+zd/ryADKlmr9iRy2TE4HMUQXQ4e8Bu56WwbW9RXRfKv5eS9Dm4dL5uPzkxgK5wXHeP0ctml073l8WuyXuHoh1lHZ4pC+YjU9AybOz4zeZJiS0ENk/wx0CZCqvGrKR12KaaIo4=; gsscgib-w-mvideo=Vjlq9ockyxwJyHPeeWpciCqeYQY+eu749g1Yk+2fuvLgR533JHLC+QMMmCdt2smAPiFW7FbUK6qdZrYBGPZI75eMo2vzTVHRePpQtjrDeiBaCdu33xDQOv8tQwmiw98oiDnc9K8IX+zd/ryADKlmr9iRy2TE4HMUQXQ4e8Bu56WwbW9RXRfKv5eS9Dm4dL5uPzkxgK5wXHeP0ctml073l8WuyXuHoh1lHZ4pC+YjU9AybOz4zeZJiS0ENk/wx0CZCqvGrKR12KaaIo4=',
        'referer': 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search',
        'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '1be3bf8d45484f37aadb4ae8c34841df-8b7f1fb14bf89500-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': '00ebd2b1-414b-45b0-ade2-df27074eb1b5',
    }

    params = {
        'categoryId': '65',
        'offset': (page - 1) * 24,
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }
    try:
        response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
        products_ids = response.get('body').get('products')

        print(products_ids)

        json_data = {
            'productIds': products_ids,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }

        response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                                 json=json_data).json()

        products = response.get('body').get('products')

        print(products)

        products_ids_str = ','.join(products_ids)
        print(products_ids_str)
        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }

        response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                                headers=headers).json()
        material_prices = response.get('body').get('materialPrices')

        items_prices = {}

        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_price = item.get('price').get('salePrice')
            items_prices[item_id] = item_price

        print(items_prices)

        data = []

        for item in products:
            product_id = item.get('productId')

            if (product_id in items_prices):
                prices = items_prices[product_id]
                data.append([item.get('name'), prices])

        #print(data)

        with open('output.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)

            # Записываем данные в файл
            writer.writerows(data)
            print("Данные успешно записаны в файл CSV.")

    except requests.exceptions.ReadTimeout:
        #print("Произошла ошибка чтения тайм-аута (Read timed out).")
        get_data(page, cookies_dict)

# def main():
#     get_data()
#     print("Начало")
#
#
# if __name__ == '__main__':
#     main()