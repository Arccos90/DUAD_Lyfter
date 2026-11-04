from exercise_4 import reverse_string 

def test_reverse_string_can_make_reverse_proccess ():
    #arrange
    original_text = "Hola Mundo"
    reverse_text = "odnuM aloH"
    #act
    result = reverse_string(original_text)
    #assert
    assert result == reverse_text
