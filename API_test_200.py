import Post_Get_Requests

# 2 Сохранить номер трека заказа.
def save_number_from_track_order():
    t_track = Post_Get_Requests.post_create_order()
    return t_track.json()["track"]

# 4 Проверить, что код ответа равен 200.
def test_positive_assert_200():
    t_track = save_number_from_track_order()
    response_success = Post_Get_Requests.get_request_from_track_order(t_track)
    assert response_success.status_code == 200
