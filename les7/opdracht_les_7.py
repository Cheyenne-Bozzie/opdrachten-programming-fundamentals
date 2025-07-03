from config_les_7 import exchange_rates_API

import requests

url = 'https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR'
params = {'appid': exchange_rates_API }


def get_exchange_rates(api_key, base_currency, target_currency):
    full_url = f"{url}latest"
    params = {
        'access_key': api_key,
        'base': base_currency,
        'symbols': target_currency
 }
    try:
        response = requests.get(full_url, params=params)
        response.raise_for_status()

    if response.status_code == 200:
        data = response.json()

        if data.get('succes'):
            return data
        else
            error_info = data.get('error')

get_exchange_rates(exchange_rates_API)