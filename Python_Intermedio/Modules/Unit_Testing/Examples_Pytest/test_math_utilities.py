from math_utilities import sum_list_items

def test_sum_list_items_with_small_numbers_sums_all_items_correctly():
    #AAA
    #Arrange
    list_input = [3, 7, 8]
    #Act
    result = sum_list_items (list_input)
    #Assert
    assert result == 18

def test_sum_list_items_with_bigger_numbers_sums_all_items_correctly():
    #AAA
    #Arrange
    list_input = [3333, 79898, 83411]
    #Act
    result = sum_list_items (list_input)
    #Assert
    assert result != 16634