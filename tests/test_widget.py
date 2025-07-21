import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card , expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_good(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_mask_account_card_0():
    with pytest.raises(ValueError):
        mask_account_card("")


def test_mask_account_card_alpha():
    with pytest.raises(ValueError):
        mask_account_card("Visa Gold 599941a228426g53")


@pytest.mark.parametrize("date_card, data_list", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date_good(date_card, data_list):
    assert get_date(date_card) == data_list


def test_get_date_0():
    with pytest.raises(ValueError):
        get_date("")
