import random
import pytest
from BubleSort import bubble_sort

def test_bubble_sort_can_work_with_small_list(): # I defined small list like a less of 10 items
#Arrange
 test_list = [1,60,5,10,9,65,20]
 expected_list = [1,5,9,10,20,60,65]
#act
 bubble_sort (test_list)
#Assert
 assert test_list == expected_list

def test_bubble_sort_can_work_with_bigger_list_with_more_than_100_items(): 
 test_list = [random.randint(1,1000) for _ in range (100)]
 expected_list = sorted(test_list)
#act
 bubble_sort (test_list)
#Assert
 assert len(test_list)==100
 assert test_list == expected_list

def test_bubble_sort_can_work_with_blank_list(): 
 test_list = []
 expected_list = []
#act
 bubble_sort (test_list)
#Assert
 assert test_list == expected_list

def test_bubble_sort_can_not_work_with_no_list_parameter_is_string(): 
 invalid_list = "desordenado"
#act & assert
 with pytest.raises(TypeError):
    bubble_sort(invalid_list)

def test_bubble_sort_can_not_work_with_no_list_parameter_is_tupla(): 
 invalid_list = (10,2,5,6,9)
#act & assert
 with pytest.raises(TypeError):
    bubble_sort(invalid_list)

def test_bubble_sort_can_not_work_with_no_list_parameter_is_integer(): 
 invalid_list = 12569
#act & assert
 with pytest.raises(TypeError):
    bubble_sort(invalid_list)

def test_bubble_sort_can_not_work_with_string_item_in_the_list(): 
 invalid_list = ["a","b",6,9,4]
#act & assert
 with pytest.raises(TypeError):
    bubble_sort(invalid_list)