from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимает на вход тип и номер карты или счета и возвращает маску"""
    mask_card = ""
    if data.startswith('Счет'):
        # для счетов: берем все после слова счет.
        number = data.split()[-1]
        return f"Счет {get_mask_account(number)}"
    else:
        # для карт: берем все, что после типа карты и названия
        *name_parts, number = data.split()
        name = " ".join(name_parts)
        return f"{name} {get_mask_card_number(number)}"


print(mask_account_card("Visa Platinum 8990922113665229"))

print(mask_account_card("Счет 35383033474447895560"))


