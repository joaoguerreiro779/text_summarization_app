'''
Test the api endpoints

    Methods
        -------
            test_response_codes
                Test error status code.

            test_error_type
                Test error response.

            test_not_error
                Test absence of error when input is english text.

            test_summarizer
                Test summarization service end-to-end.
'''

import json
import time
import requests
import pytest


time.sleep(20)
env_data = pytest.env_var

@pytest.mark.parametrize("test_input,expected",
[({'text': 5}, 400),
({'text': '5'}, 400),
({'text': env_data['ENGLISH_TEXT_1']}, 200),
({'text': env_data['SPANISH_TEXT_1']}, 400),
({'text': env_data['GERMAN_ENGLISH']}, 400)])
def test_response_codes(test_input, expected):

    '''Test error status code.'''

    response = requests.post(env_data['URL'], json = test_input).json()
    assert int(response['status_code']) == expected

@pytest.mark.parametrize("test_input,expected",
[({'text': 5}, 'TypeError'),
({'text': '5'}, 'LanguageIdentificationError'),
({'text': env_data['SPANISH_TEXT_1']}, 'LanguageIdentificationError'),
({'text': env_data['GERMAN_ENGLISH']}, 'LanguageIdentificationError')])
def test_error_type(test_input, expected):

    '''Test error response.'''

    response = requests.post(env_data['URL'], json = test_input).text
    assert json.loads(response)['error']['type'] == expected

@pytest.mark.parametrize("test_input,expected",
[({'text': env_data['ENGLISH_TEXT_1']}, None)])
def test_not_error(test_input, expected):

    '''Test absence of error when input is english text.'''

    response = requests.post(env_data['URL'], json = test_input).text
    assert json.loads(response).get('error') == expected

@pytest.mark.parametrize("test_input,expected",
[({'text': env_data['ENGLISH_TEXT_1']}, env_data['ENGLISH_RESULT_1']),
({'text': env_data['ENGLISH_TEXT_2']}, env_data['ENGLISH_RESULT_2'])])
def test_summarizer(test_input, expected):

    '''Test summarization service end-to-end.'''

    response = requests.post(env_data['URL'], json = test_input).json()
    assert response['summary'] == expected
