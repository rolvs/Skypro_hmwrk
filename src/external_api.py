import os
from typing import Any

import requests

API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Convert amount from currency (USD/EUR) to RUB using APILayer Exchange Rates Data API.
    Requires env var EXCHANGE_RATES_API_KEY.
    """
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise RuntimeError("EXCHANGE_RATES_API_KEY is not set")

    params = {"from": currency, "to": "RUB", "amount": amount}
    headers = {"apikey": api_key}

    resp = requests.get(API_URL, params=params, headers=headers, timeout=10)
    resp.raise_for_status()

    data: dict[str, Any] = resp.json()
    result = data.get("result")
    if result is None:
        raise RuntimeError("API response does not contain 'result'")

    return float(result)
