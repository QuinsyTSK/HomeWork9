# Проект для обработки и фильтрации банковских операций

## Описание

Проект создан в рамках домашней работы по изучению написания кода на языке Python.
В проекте реализованы функции шифрования банковских карт и счетов, вывод их в кодированном виде, формирование даты в формате ДД.ММ.ГГГГ.
А так же функции принимающие списки словарей с данными счетов и карт и возвращающие их по задданым фильтрам (статус, дата).

## Установка

1. Клонируйте репозиторий:
```
https://github.com/QuinsyTSK/HomeWork9/tree/main
```

2. Установите зависимости:
```
poetry instal
```

3. Проверьте качество кода:
```
poetry run flake8
poetry run black --check
poetry run mypy src/
```

## Использование

Для корректного получения кодированного вида карты или счета нужно ввести правильный номер.
В случае, если цифр окажется меньше или больше, функционал выдаст ошибку.

## Документация

1. Функция get_mask_card_number:
- принимает на вход номер карты и возвращает ее маску;
- маска отображается в формате XXXX XX** **** XXXX, где X — это цифра номера;
- пример работы функции:
``` 7000792289606361     # входной аргумент ```
``` 7000 79** **** 6361  # выход функции ```

2. Функция get_mask_account:
- принимает на вход номер счета и возвращает его маску;
- маска отображается в формате **XXXX, где X — это цифра номера;
- пример работы функции:
``` 73654108430135874305  # входной аргумент ```
``` **4305  # выход функции ```

3. Функция mask_account_card:
- принимает один аргумент — строку, содержащую тип и номер карты или счета и возвращает строку с замаскированным номером;
- для карт и счетов используются разные типы маскировки - get_mask_card_number и get_mask_account соответственно;
- пример работы функции для карт:
``` Visa Platinum 7000792289606361  # входной аргумент ```
``` Visa Platinum 7000 79** **** 6361  # выход функции ```
- пример работы функции для счета:
``` Счет 73654108430135874305  # входной аргумент ```
``` Счет **4305  # выход функции ```

4. Функция get_date:
- принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

5. Функция filter_by_state:
- принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED') и возвращает новый список словарей с заданным ключом;
- пример работы функции:

``` [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] ```

Выход функции со статусом по умолчанию 'EXECUTED'
``` [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}] ```

6. Функция sort_by_date:
- принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание), и возвращать новый список, отсортированный по дате;
- пример работы функции (входные данные такие же как и filter_by_state):

Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
``` [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}] ```

## Лицензия

Лицензия к данному проекту не предусмотрена
