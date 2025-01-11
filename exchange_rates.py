
import requests

def fetch_exchange_rates():

    url = "https://nbu.uz/uz/exchange-rates/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Valyuta kurslarini olishda xatolik yuz berdi: {e}")
        return None
