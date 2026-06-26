# Белов Сергей, 44-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def test_create_and_get_order_by_track():
    # Создание заказа
    create_response = requests.post(
        f"{configuration.BASE_URL}{configuration.CREATE_ORDER_ENDPOINT}",
        json=data.order_body
    )
    assert create_response.status_code == 201, (
        f"Create order failed with status {create_response.status_code}"
    )
    
    track = create_response.json().get("track")
    assert track is not None, "Response does not contain track"
    
    # Получение заказа по треку
    get_response = requests.get(
        f"{configuration.BASE_URL}{configuration.GET_ORDER_BY_TRACK_ENDPOINT}",
        params={"t": track}
    )
    assert get_response.status_code == 200, (
        f"Get order failed with status {get_response.status_code}"
    )