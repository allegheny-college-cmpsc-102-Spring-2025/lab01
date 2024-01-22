"""Test suite to ensure that each function words correctly."""

from search import __version__

from search import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_human_readable_boolean_false():
    """Confirm that a False results in a no response."""
    value = False
    response = main.human_readable_boolean(value)
    assert response == "No"


def test_human_readable_boolean_true():
    """Confirm that a True results in a yes response."""
    value = True
    response = main.human_readable_boolean(value)
    assert response == "Yes"


def test_word_found_in_text():
    """Confirm that an existing word is found in the text."""
    word = "Confirm"
    text = "Confirm that an existing word is found in the text."
    response = main.word_search(text, word)
    assert response is True


def test_word_not_found_in_text():
    """Confirm that an existing word is found in the text."""
    word = "confirm"
    text = "Confirm that an existing word is found in the text."
    response = main.word_search(text, word)
    assert response is False
