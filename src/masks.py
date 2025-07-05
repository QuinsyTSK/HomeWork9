def get_mask_card_number(number_card_1: int) -> str:
    """Функция возвращает маску номера карты в формате
    XXXX XX** **** XXXX"""
    number_card = str(number_card_1)
    if len(number_card) == 16:
        mask_number = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
        return mask_number
    return "Введен не верный номер карты"


def get_mask_account(number_card_2: int) -> str:
    """Функция возвращает маску номера карты в формате
    **XXXX"""
    number_card = str(number_card_2)
    if len(number_card) == 16:
        mask_account = f"**{number_card[-4:]}"
        return mask_account
    return "Введен не верный номер карты"


if __name__ == "__main__":
    print(get_mask_card_number(1212121212121212))
    print(get_mask_account(1212121212121212))
