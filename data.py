from datetime import datetime, timedelta

tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

order_body = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "Москва, ул. Ленина, д.1",
    "metroStation": "4",
    "phone": "+79998887766",
    "rentTime": 3,
    "deliveryDate": tomorrow,
    "comment": "Позвоните за час",
    "color": ["BLACK", "GREY"]
}