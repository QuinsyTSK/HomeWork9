from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_info: str) -> str:
    """Принимаем тип и номер карты, возвращает тип и маску номера"""
    type_list = []
    number_list = account_info.split()

    # Определяем тип данных
    for string in number_list:
        if string.isalpha():
            type_list.append(string)
    card_type = " ".join(type_list)

    # Определяем номер карты
    card_number = int(number_list[-1])

    # Применяем маскировки счета
    if card_type == "Счет":
        return f"{card_type} {get_mask_account(card_number)}"
    else:
        return f"{card_type} {get_mask_card_number(card_number)}"


def get_date(date_card: str) -> str:
    """Функция выводит дату в формате ДД.ММ.ГГГГ"""
    date_list = date_card.split("-", 2)
    date_list[2] = date_list[2][:2]
    date_list_reverse = ".".join(date_list[::-1])
    return date_list_reverse


if __name__ == "__main__":
    print(mask_account_card('Maestro 1596837868705199'))
    print(mask_account_card('Счет 64686473678894779589'))
    print(get_date('2024-03-11T02:26:18.671407'))
