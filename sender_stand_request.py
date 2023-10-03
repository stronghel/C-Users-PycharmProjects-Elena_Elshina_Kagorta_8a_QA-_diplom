import configuration
import data
import requests


# 1 Выполнить запрос на создание заказа.
def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.body)


# 3 Выполнить запрос на получения заказа по треку заказа.
def get_request_from_track_order(t_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_REQUEST_FROM_TRACK_ORDER_PATH,
                        params={"t": t_track})
