"""
Pytest config for setting environment variables.

    Methods
        -------
            pytest_configure
                Sets the configuration for pytest.

"""

import pytest


def pytest_configure():

    """Sets the configuration for pytest."""

    with open("test/resources/Edge Cases/english_text_1.txt", "r") as _:
        english_example = _.read()
    with open("test/resources/Edge Cases/summary_1.txt", "r") as _:
        summary_1 = _.read()
    with open("test/resources/Edge Cases/english_text_2.txt", "r") as _:
        english_example_2 = _.read()
    with open("test/resources/Edge Cases/summary_2.txt", "r") as _:
        summary_2 = _.read()
    with open("test/resources/Edge Cases/spanish_text_1.txt", "r") as _:
        spanish_example = _.read()
    with open("test/resources/Edge Cases/english_german.txt", "r") as _:
        german_english = _.read()

    data = {
        "URL": "http://127.0.0.1:5000/summarize",
        "ENGLISH_TEXT_1": english_example,
        "ENGLISH_RESULT_1": summary_1,
        "ENGLISH_TEXT_2": english_example_2,
        "ENGLISH_RESULT_2": summary_2,
        "SPANISH_TEXT_1": spanish_example,
        "GERMAN_ENGLISH": german_english,
    }

    pytest.env_var = data
