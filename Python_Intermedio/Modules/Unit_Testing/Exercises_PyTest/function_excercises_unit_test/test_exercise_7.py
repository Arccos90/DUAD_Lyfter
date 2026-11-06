from exercise_7 import prime_detector
import pytest

def test_prime_detector_with_prime_number():
    #arrange
    input_number = "2"
    #act
    result = True
    #asser
    assert result == True

def test_prime_detector_with_noprime_number():
    #arrange
    input_number = "3"
    #act
    output = False
    #assert
    assert output == False

def test_prime_detector_with_letter_input():
    #arrange
    input = "a"
    #act & assert
    with pytest.raises (TypeError) as error:
        prime_detector(input)
    print(f"Este es el error: {error}")