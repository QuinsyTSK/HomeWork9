import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number_card, mask_card", [('1212121212121212', '1212 12** **** 1212'),
                                                    ('12 345678909 87654', '1234 56** **** 7654'),
                                                    ('22876-54321098-765', '2287 65** **** 8765')])
def test_get_mask_card_number(number_card, mask_card):
    assert get_mask_card_number(number_card) == mask_card


def test_get_mask_invalid_card_number():
    with pytest.raises(TypeError):
        get_mask_card_number('f1212121212121aa21212')


@pytest.mark.parametrize("number_card", ['',
                                       '1234 4557',
                                       '1234 1234 1234 1234 1234'])
def test_get_mask_card_number_wrong(number_card):
    with pytest.raises(ValueError):
        get_mask_card_number(number_card)


@pytest.fixture
def number_account():
    return '12121212121212121212'


def test_get_mask_account(number_account):
    assert get_mask_account(number_account) == '**1212'


@pytest.mark.parametrize("number_account, mask_account", [('1212-1212-1212-1212-1212', '**1212'),
                                                          ('12345678 9098765 48345', '**8345')])
def test_get_mask_account(number_account, mask_account):
    assert get_mask_account(number_account) == mask_account


def test_get_mask_invalid_account():
    with pytest.raises(TypeError):
        get_mask_account('f1212121212121aa212112342')


def test_get_mask_account_less():
    with pytest.raises(ValueError):
        get_mask_account('1234 2386')


def test_get_mask_account_0():
    with pytest.raises(ValueError):
        get_mask_account('')


def test_get_mask_account_big():
    with pytest.raises(ValueError):
        get_mask_account('1234 2386373738837645455251543678')
