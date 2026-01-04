import os
from unittest.mock import Mock, patch

import external_api


@patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_key"})
@patch("external_api.requests.get")
def test_convert_to_rub_success(mock_get):
    fake_response = Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = {"result": 123.45}
    mock_get.return_value = fake_response

    result = external_api.convert_to_rub(10.0, "USD")
    assert result == 123.45

    mock_get.assert_called_once()
    _, kwargs = mock_get.call_args
    assert kwargs["headers"] == {"apikey": "test_key"}
    assert kwargs["params"] == {"from": "USD", "to": "RUB", "amount": 10.0}
    assert kwargs["timeout"] == 10


@patch.dict(os.environ, {}, clear=True)
def test_convert_to_rub_no_api_key_raises():
    # если ключа нет — ожидаем ошибку
    try:
        external_api.convert_to_rub(10.0, "USD")
        assert False, "Expected RuntimeError"
    except RuntimeError:
        assert True
