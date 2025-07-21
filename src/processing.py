def filter_by_state(list_of_data_cards_1: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей с данными счета.карты и заданный ключ 'state' (по умолчанию EXECUTED)
    и возвращает список по заданному этому ключу"""
    filtered_list = []
    for state_item in list_of_data_cards_1:
        if not state_item.get("state"):
            raise KeyError("В данных отсутствует статус")

    for data_item in list_of_data_cards_1:
        if data_item.get("state") == state:
            filtered_list.append(data_item)

    return filtered_list


def sort_by_date(list_of_data_cards_2: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей с данными счета/карты и параметр сортировки (по умолчанию True)
    и возвращает отсортированный список по дате согласно параметру"""
    if list_of_data_cards_2 == []:
        raise ValueError("Отсутствуют данные")

    for data_item in list_of_data_cards_2:
        if not data_item.get("date"):
            raise KeyError("В данных отсутствует дата")
    return sorted(list_of_data_cards_2, key=lambda x: x["date"], reverse=reverse)


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
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            reverse=False,
        )
    )
