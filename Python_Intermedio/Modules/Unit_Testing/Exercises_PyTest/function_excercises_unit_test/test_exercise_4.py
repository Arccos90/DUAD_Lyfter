from exercise_4 import reverse_string 
import pytest

def test_reverse_string_can_make_reverse_proccess ():
    #arrange
    original_text = "Hola Mundo"
    reverse_text = "odnuM aloH"
    #act
    result = reverse_string(original_text)
    #assert
    assert result == reverse_text


def test_reverse_string_can_make_reverse_proccess_with_numbers ():
    #arrange
    original_text = "123456"
    reverse_text = "654321"
    #act
    result = reverse_string(original_text)
    #assert
    assert result == reverse_text

def test_reverse_string_can_make_reverse_proccess_with_numbers_letter ():
    #arrange
    original_text = "a1b2c3b5"
    reverse_text = "5b3c2b1a"
    #act
    result = reverse_string(original_text)
    #assert
    assert result == reverse_text

def test_reverse_string_can_make_reverse_proccess_with_numbers_letter_and_symbols ():
    #arrange
    original_text = "a1b2c3b5$"
    #act & assert
    with pytest.raises (ValueError) as error:
        reverse_string(original_text)

    print(f"El Error Es: {error.value}")
    