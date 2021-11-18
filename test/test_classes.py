from unittest import mock
import os
import pytest
from exceptions import ModelConfigLoadError, TokenizerConfigLoadError, InvalidModelError
from services.summarizer import Summarizer
from services.language_identifier import LanguageIdentifier


def test_summarizer():

    with open('resources/english_text_1.txt') as _:
        example_text_1 = _.readlines()
    with open('resources/english_result_1.txt') as _:
        result_1 = _.readlines()

    # fail if unable to retrieve the model
    with mock.patch.dict(os.environ, {"MODEL_NAME": ""}):
        with pytest.raises(ModelConfigLoadError):
            Summarizer()

    # fail if model is not valid for summarization
    with mock.patch.dict(os.environ, {"MODEL_NAME": "cardiffnlp/twitter-roberta-base-offensive"}):
        with pytest.raises(InvalidModelError):
            Summarizer()

    # success
    with mock.patch.dict(os.environ, {"MODEL_NAME": "facebook/bart-large-cnn"}):
        model = Summarizer()
    assert model.framework=='pt'

    # fail if unable to retrieve the tokenizer
    with mock.patch.dict(os.environ, {"TOKENIZER_NAME": ""}):
        with pytest.raises(TokenizerConfigLoadError):
            model.summarize(query_text=example_text_1)

    # success
    with mock.patch.dict(os.environ,{"TOKENIZER_NAME": "philschmid/bart-large-cnn-samsum"}):
        assert model.summarize(query_text=example_text_1)==result_1
