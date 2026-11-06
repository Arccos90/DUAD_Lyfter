from exercise_6 import alphabetical_order
import pytest

def test_alphabetical_order_with_numbers():
    #arrange
    input_text = "4455-1122-9988-7755"
    output_text = "1122-4455-7755-9988"
    #act
    result = alphabetical_order(input_text)
    #assert
    assert result == output_text

def test_alphabetical_order_with_letter():
    #arrange
    input_text = "Hola-muchachos-como-estan"
    output_text = "Hola-como-estan-muchachos"
    #act
    result = alphabetical_order(input_text)
    #assert
    assert result == output_text

def test_alphabetical_order_with_letter():
    #arrange
    input_text = "Hola_muchachos_como_estan"
    output_text = "Hola-como-estan-muchachos"
    #act
    result = alphabetical_order(input_text)
    #assert
    assert result != output_text
