# Белов Сергей, 44-я когорта — Финальный проект. Инженер по тестированию плюс
import data
from order_helpers import create_order, get_order_by_track

def test_create_and_get_order_by_track():
    # Создание заказа
    create_response = create_order(data.order_body)
    assert create_response.status_code == 201, (
        f"Create order failed with status {create_response.status_code}"
    )

    track = create_response.json().get("track")
    assert track is not None, "Response does not contain track"

    # Получение заказа по треку
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200, (
        f"Get order failed with status {get_response.status_code}"
    )