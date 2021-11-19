import json
import requests
import pytest

data = pytest.env_var

@pytest.mark.parametrize("test_input,expected",
[({'wrong_key': 5}, 400),
({'text': 5}, 400),({'text': '5'}, 400),
({'text': data['ENGLISH_TEXT_1']}, 200),
({'text': data['SPANISH_TEXT_1']}, 400),
({'text': data['GERMAN_ENGLISH']}, 400)])
def test_response_codes(test_input, expected):
    response = requests.post(data['URL'], json = json.dumps(test_input))
    assert response.status_code == expected

@pytest.mark.parametrize("test_input,expected",
[({'wrong_key': 5}, 'TypeError'),
({'text': 5}, 'TypeError'),
({'text': '5'}, 'LanguageIdentificationError'),
({'text': data['SPANISH_TEXT_1']}, 'LanguageIdentificationError'),
({'text': data['GERMAN_ENGLISH']}, 'LanguageIdentificationError')])
def test_error_type(test_input, expected):
    response = requests.post(data['URL'], json = json.dumps(test_input)).json()
    assert response['error']['name'] == expected

@pytest.mark.parametrize("test_input,expected",
[({'text': data['ENGLISH_TEXT_1']}, None)])
def test_not_error(test_input, expected):
    response = requests.post(data['URL'], json = json.dumps(test_input)).json()
    assert json.loads(response.text).get('error') == expected
