import requests


def get_size(address_ll):
    org_point = address_ll

    print("Введите размеры в формате: 0.005, 0.005")
    delta1, delta2 = '0.002, 0.002'.split(", ")

    params = {
        "ll": address_ll,
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": "{},pm2dgl".format(org_point),
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    return response
