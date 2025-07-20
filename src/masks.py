def get_mask_card_number(number_card_1: str) -> str:
    """Функция возвращает маску номера карты в формате
    XXXX XX** **** XXXX"""
    number_card = ''
    for i in number_card_1:
        if i.isalpha():
            raise TypeError("Введен не верный номер карты")
        elif i.isdigit():
            number_card += number_card.join(i)

    if len(number_card) == 16:
        mask_number = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
        return mask_number
    raise ValueError("Введен не верный номер карты")


def get_mask_account(number_account_2: str) -> str:
    """Функция возвращает маску номера карты в формате
    **XXXX"""
    number_account = ''
    for i in number_account_2:
        if i.isalpha():
            raise TypeError("Введен не верный номер счета")
        elif i.isdigit():
            number_account += number_account.join(i)

    if len(number_account) == 20:
        mask_account = f"**{number_account[-4:]}"
        return mask_account
    else:
        raise ValueError("Введен не верный номер счета")


if __name__ == "__main__":
    print(get_mask_card_number("1212 12121212 1212"))
    print(get_mask_account("12345678 9098765 49345"))
