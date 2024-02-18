import sys
from io import BytesIO
import requests
from PIL import Image
from get_size import get_size
'''
python big_search.py Москва, ул. Ак. Королева, 12
0.002, 0.002
'''


def big_search():
    toponym_to_find = " ".join(sys.argv[1:])

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]

    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    address_ll = ",".join([toponym_longitude, toponym_lattitude])
    response = get_size(address_ll)

    Image.open(BytesIO(
        response.content)).show()


big_search()
