from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_info: str) -> str:
    """Принимаем тип и номер карты, возвращает тип и маску номера"""
    if account_info == "":  # проверяем строку данных на наличие символов
        raise ValueError("Неверный данные")

    type_list = []
    number_list = account_info.split()

    # Определяем тип данных
    for string in number_list:
        if string.isalpha():
            type_list.append(string)
    card_type = " ".join(type_list)

    # Определяем номер карты
    card_number = number_list[-1]
    for i in card_number:  # Проверяем номер на наличие не числовых символов
        if i.isalpha():
            raise ValueError("Неверный данные номера")

    # Применяем маскировки счета
    if card_type == "Счет":
        return f"{card_type} {get_mask_account(card_number)}"
    else:
        return f"{card_type} {get_mask_card_number(card_number)}"


def get_date(date_card: str) -> str:
    """Функция выводит дату в формате ДД.ММ.ГГГГ"""

    if date_card == "":  # проверяем строку с данными даты на наличие символов
        raise ValueError("Неверный ввод даты")

    date_list = date_card.split("-", 2)
    date_list[2] = date_list[2][:2]
    date_list_reverse = ".".join(date_list[::-1])
    return date_list_reverse


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
