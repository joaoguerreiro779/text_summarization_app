import pytest
from services.summarizer import Summarizer
from services.language_identifier import LanguageIdentifier


data = pytest.env_var

@pytest.mark.parametrize("test_input,expected", [(data['ENGLISH_TEXT_1'], data['ENGLISH_RESULT_1'])])
def test_summarizer(test_input, expected):
    assert Summarizer().summarize(test_input) == expected

@pytest.mark.parametrize("test_input,expected",
[(data['ENGLISH_TEXT_1'], True),
(data['SPANISH_TEXT_1'], True),
(data['GERMAN_ENGLISH'], False)])
def test_language_prob(test_input, expected):
    assert (LanguageIdentifier().get_language(test_input)[1]>0.98) == expected

@pytest.mark.parametrize("test_input,expected",
[(data['ENGLISH_TEXT_1'], 'en'),
(data['SPANISH_TEXT_1'], 'es')])
def test_language_identifier(test_input, expected):
    assert LanguageIdentifier().get_language(test_input)[0] == expected