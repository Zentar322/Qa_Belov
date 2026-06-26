# order_helpers.py
import requests
import configuration

def create_order(order_data):
    url = f"{configuration.BASE_URL}{configuration.CREATE_ORDER_ENDPOINT}"
    response = requests.post(url, json=order_data)
    return response

def get_order_by_track(track_number):
    url = f"{configuration.BASE_URL}{configuration.GET_ORDER_BY_TRACK_ENDPOINT}"
    response = requests.get(url, params={"t": track_number})
    return response