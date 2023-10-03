import sender_stand_request

# 2 Сохранить номер трека заказа.
def save_number_from_track_order():
    t_track = sender_stand_request.post_create_order()
    return t_track.json()["track"]

# 4 Проверить, что код ответа равен 200.
def test_get_order_by_track():
    t_track = save_number_from_track_order()
    response_success = sender_stand_request.get_request_from_track_order(t_track)
    assert response_success.status_code == 200
