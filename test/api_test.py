import json
import requests
import pytest

data = pytest.env_var

@pytest.mark.parametrize("test_input,expected",
[({'text': 5}, 400),
({'text': '5'}, 400),
({'text': data['ENGLISH_TEXT_1']}, 200),
({'text': data['SPANISH_TEXT_1']}, 400),
({'text': data['GERMAN_ENGLISH']}, 400)])
def test_response_codes(test_input, expected):
    response = requests.post(data['URL'], json = test_input).text
    assert int(json.loads(response)['status_code']) == expected

@pytest.mark.parametrize("test_input,expected",
[({'text': 5}, 'TypeError'),
({'text': '5'}, 'LanguageIdentificationError'),
({'text': data['SPANISH_TEXT_1']}, 'LanguageIdentificationError'),
({'text': data['GERMAN_ENGLISH']}, 'LanguageIdentificationError')])
def test_error_type(test_input, expected):
    response = requests.post(data['URL'], json = test_input).text
    assert json.loads(response)['error']['type'] == expected

@pytest.mark.parametrize("test_input,expected",
[({'text': data['ENGLISH_TEXT_1']}, None)])
def test_not_error(test_input, expected):
    response = requests.post(data['URL'], json = test_input).text
    assert json.loads(response).get('error') == expected
