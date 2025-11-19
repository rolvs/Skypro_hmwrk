from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимает на вход тип и номер карты или счета и возвращает маску"""
    if data.startswith("Счет"):
        # для счетов: берем все после слова счет.
        number = data.split()[-1]
        return f"Счет {get_mask_account(number)}"
    else:
        # для карт: берем все, что после типа карты и названия
        *name_parts, number = data.split()
        name = " ".join(name_parts)
        return get_mask_card_number(f"{name} {number}")


# print(mask_account_card("Visa Platinum 8990922113665229"))

# print(mask_account_card("Счет 35383033474447895560"))


def get_date(data: str) -> str:
    """принимает на вход строку с датой и возвращает в формате "ДД.ММ.ГГГГ"""
    date_part = data.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


# print(get_date("2024-03-11T02:26:18.671407"))
