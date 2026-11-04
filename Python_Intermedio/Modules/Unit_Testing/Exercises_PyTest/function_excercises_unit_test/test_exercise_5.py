from exercise_5 import upper_letters, lower_letters

def test_upper_letters_count_all_upper_letter ():
    #arrange
    original_phrase = "Hola Mundo Entero"

    #act
    result=upper_letters(original_phrase)
    #assert
    assert result == 3

def test_lower_letters_count_all_lower_letter ():
    #arrange
    original_phrase = "Hola Mundo"
    #act
    result = lower_letters(original_phrase)
    #assert
    assert result == 7