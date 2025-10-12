def get_mask_card_number(num: str) -> str:
    """Принимает на вход строку с картой или счётом и возвращает её маску."""

    if num.startswith("Счет"):
        # оставляем только последние 4 цифры
        return f"Счет **{num[-4:]}"
    else:
        # вытащим только цифры из строки
        digits = "".join(filter(str.isdigit, num))
        # первые 6 + ** + последние 4
        visible = digits[:6] + "******" + digits[-4:]
        # разобьём на блоки по 4 цифры
        blocks = [visible[i:i+4] for i in range(0, len(visible), 4)]
        # добавим название карты (например "Visa Platinum")
        prefix = " ".join(num.split()[:-1])
        return f"{prefix} {' '.join(blocks)}"


def get_mask_account(account_num: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    account_num_str = str(account_num)
    visible_part = "**" + account_num_str[-4:]
    return visible_part


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
