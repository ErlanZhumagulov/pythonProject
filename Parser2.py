import requests

import csv


def get_data(page, cookies_dict):
    import requests

    cookies = {
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
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
        'MVID_SP': 'true',
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
        'MVID_ENVCLOUD': 'prod2',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'SMSError': '',
        'authError': '',
        'BIGipServericerock-prod': '3187989514.20480.0000',
        'bIPs': '-957002303',
        '_ym_isad': '2',
        'mindboxDeviceUUID': 'dac89675-e94a-4a4a-bf07-7765e74f9ea9',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22dac89675-e94a-4a4a-bf07-7765e74f9ea9%22%7D',
        '__js_p_': '590,1800,0,1,0',
        '__jhash_': '1103',
        '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20YaBrowser%2F23.5.4.674%20Yowser%2F2.5%20Safari%2F537.36',
        '_sp_ses.d61c': '*',
        '_sp_id.d61c': '141bcadc-d675-4b25-8bd9-1c9dcbecb117.1688477596.14.1689177591.1689174758.05824003-2bc4-422b-be28-b1e5f98fd2d5.ca6b15eb-0dff-4797-80ec-35ed64d7e532.d4ebcc54-a5b6-4b4f-8b49-34bd45006fd4.1689177590722.5',
        '_ga': 'GA1.2.1703219727.1688477596',
        'tmr_detect': '1%7C1689177594271',
        'gsscgib-w-mvideo': 'gCI5VNFzc7PfJ+K3imd6WbVK7tjjAuS07/8hu9KX1vdGLKCVjztgrN41zAaXmpFsB12WfXdTvPZXsPGD1vLS9D2Ux2GkuwtLplxobhgavTNJvY9FQOqmSUwkJLCsYy5YF4pssDZC15JrRfrodTvdFC0GLRuq5RZZ3gcMvqecEnXvjuM0+gSc5ZtgXqG4ls1TX7ZVxBP/ckvzGlkRH/Xqq9LtqY5W9z+m5eYANoqqAGl1PwW9uKfH0oCVeXxK3D8GM8S5OAFs3vXqPG2IEtM/',
        'gsscgib-w-mvideo': 'gCI5VNFzc7PfJ+K3imd6WbVK7tjjAuS07/8hu9KX1vdGLKCVjztgrN41zAaXmpFsB12WfXdTvPZXsPGD1vLS9D2Ux2GkuwtLplxobhgavTNJvY9FQOqmSUwkJLCsYy5YF4pssDZC15JrRfrodTvdFC0GLRuq5RZZ3gcMvqecEnXvjuM0+gSc5ZtgXqG4ls1TX7ZVxBP/ckvzGlkRH/Xqq9LtqY5W9z+m5eYANoqqAGl1PwW9uKfH0oCVeXxK3D8GM8S5OAFs3vXqPG2IEtM/',
        'fgsscgib-w-mvideo': 'eefIa1b2c790b5bed591fab9a36a656d0d243b7e',
        'fgsscgib-w-mvideo': 'eefIa1b2c790b5bed591fab9a36a656d0d243b7e',
        '__hash_': '79a78a1bccd1612aa75be8188dd84f73',
        'gssc218': '',
        'cfidsgib-w-mvideo': 'rUn0z78pGrp4hvmUcdSwjsQnE5Lqcax86Xt08PnCABX7sC+GEoX0mhaX5+2WLJ3eZzyiYvYKtFefU9kQmOc77TL0uDOgGBfzHjH5UClDooz1EHiWw1cbxdPhJZbGnPIXNsIwFZ1OuenUhhL6T5IiZEcj3Vj8QBrxaqLkq7o=',
        '_ga_BNX5WPP3YK': 'GS1.1.1689177590.13.0.1689177656.60.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1689177590.13.0.1689177656.0.0.0',
    }

    cookies.update(cookies_dict)
    #print(cookies)
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=d6c39d945253414084b4b90e0cab8a14,sentry-sample_rate=0.5',
        # 'cookie': 'MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_6267; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000700000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=55; MVID_REGION_SHOP=S928; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _ym_uid=1688477596533287953; _ym_d=1688477596; tmr_lvid=c876c8a3aa647a5f5fcbcb24fb92e212; tmr_lvidTS=1688477599829; advcake_session_id=34db6fb8-ea77-4b20-d6a6-833ca571a69b; afUserId=de9c9f90-be7d-40de-a42e-05ae9d85baf9-p; uxs_uid=582006d0-1a6f-11ee-b68f-e1fd943ddd42; flocktory-uuid=b464727d-352a-47a6-a302-004920f95f09-0; __lhash_=c82abc25c08bb5139495a2bbc4d46ce8; MVID_PODELI_PDP=true; MVID_SERVICES=111; _gid=GA1.2.1062719037.1689100065; _ym_isad=2; AF_SYNC=1689100070895; partnerSrc=yandex; __cpatrack=yandex_organic; __sourceid=yandex; __allsource=yandex; advcake_track_id=6f209995-efaa-eb09-2726-ccf433e8b76f; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dorganic%26utm_campaign%3Dyandex%26utm_referrer%3Dyandex; advcake_utm_partner=yandex; advcake_utm_webmaster=; advcake_click_id=; MVID_ENVCLOUD=prod2; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; SMSError=; authError=; __js_p_=73,1800,0,1,0; BIGipServericerock-prod=3187989514.20480.0000; bIPs=-957002303; mindboxDeviceUUID=dac89675-e94a-4a4a-bf07-7765e74f9ea9; directCrm-session=%7B%22deviceGuid%22%3A%22dac89675-e94a-4a4a-bf07-7765e74f9ea9%22%7D; __hash_=6371f609cf72d12e875705878ee8d595; _dc_gtm_UA-1873769-1=1; _ga_CFMZTSS5FM=GS1.1.1689160782.9.1.1689160788.0.0.0; _sp_ses.d61c=*; _sp_id.d61c=141bcadc-d675-4b25-8bd9-1c9dcbecb117.1688477596.9.1689160789.1689158594.17289e29-3d8a-47af-8e80-376d999ea667.0ae988bb-8a1f-4ae7-9df6-fc78028038c5.d605a590-0511-495b-9810-b9c8d0edb595.1689160788788.5; _ga_BNX5WPP3YK=GS1.1.1689160782.9.1.1689160788.54.0.0; _ga=GA1.2.1703219727.1688477596; _dc_gtm_UA-1873769-37=1; gsscgib-w-mvideo=2F7h8bu/LWlAzMIPU8W/iDs/LoHaMacgYGIbalDwLpV23NBktXGk0aJZtPn6eaaGWusimVnPoXFZZ2ybhrC6X/72fsNricdLIbVji/9Hx0QvxQOTz3Ysk9+O2rIqWgL0ibeVQ2ucamubl/3dBcygfltpW44G6pdk4olVrXw/jKe+6YmbdleR9mo3ui5SS591+mXdKb4wt57Q1SdNwwx2VJs7T6T4xtahS9sMrKck0nRjWO2niDUBFmOMt4l+VD6gVA==; gsscgib-w-mvideo=2F7h8bu/LWlAzMIPU8W/iDs/LoHaMacgYGIbalDwLpV23NBktXGk0aJZtPn6eaaGWusimVnPoXFZZ2ybhrC6X/72fsNricdLIbVji/9Hx0QvxQOTz3Ysk9+O2rIqWgL0ibeVQ2ucamubl/3dBcygfltpW44G6pdk4olVrXw/jKe+6YmbdleR9mo3ui5SS591+mXdKb4wt57Q1SdNwwx2VJs7T6T4xtahS9sMrKck0nRjWO2niDUBFmOMt4l+VD6gVA==; tmr_detect=1%7C1689160790631; fgsscgib-w-mvideo=Ukuaa60b67d1beeb9808144ed5e312702bb925a0; fgsscgib-w-mvideo=Ukuaa60b67d1beeb9808144ed5e312702bb925a0; cfidsgib-w-mvideo=PGcEcK7abW7HmY7BoBMc4sxIikuFRq3OIyvkKEQO5cq85Rn4RmO2Y+wVv7LuFGSgNxE5yjqh2u3D5xpauGnk5aEQ31FO3t2M/mCcx0K5CsLIbgJYUqvP19JgtYgmGe5Dj+RR4RWxKmheUfiYgg0zYWeRNDLZDygPXx+ejHk=; gssc218=',
        'referer': 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search',
        'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'd6c39d945253414084b4b90e0cab8a14-a8aeb91dbf11b430-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': '10668dcb-0fbc-43c4-9c3c-8d5da33096e0',
    }

    params = {
        'categoryId': '65',
        'offset': (page - 1) * 24,
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }
    try:
        response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                                headers=headers).json()
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
