def filter_by_state(list_of_data_cards: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает список по заданному ключу 'state'"""
    filtered_list = []
    for data_item in list_of_data_cards:
        if data_item.get("state") == state:
            filtered_list.append(data_item)

    return filtered_list


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="CANCELED",
        )
    )
