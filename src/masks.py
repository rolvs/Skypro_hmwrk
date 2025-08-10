def get_mask_card_number(num: int) -> str:
    """принимает на вход номер карты и возвращает ее маску."""

    num_str = str(num)
    visible = num_str[:6] + "******" + num_str[-4:]

    blocks = [visible[i : i + 4] for i in range(0, len(visible), 4)]
    return " ".join(blocks)


def get_mask_account(account_num: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    account_num_str = str(account_num)
    visible_part = "**" + account_num_str[-4:]
    return visible_part


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
