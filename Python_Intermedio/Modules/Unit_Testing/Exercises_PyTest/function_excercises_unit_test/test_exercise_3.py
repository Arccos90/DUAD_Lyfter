from exercise_3 import sum_numbers
import pytest
def test_sum_numbers_sums_correctly ():

   #arrange
   test_list = [4,5,20,50,40]
   #act
   result = sum_numbers(test_list)
   assert result == 119

def test_sum_numbers_with_string_list():
   #arrange
   test_list = ["a","b",3,6,7,8]
   #act & assert
   with pytest.raises(TypeError) as error:
      sum_numbers(test_list)
   print(f"\n[DEBUG] Mensaje real capturado: {error.value}") 

def test_sum_numbers_with_tupla():
   #arrange
   test_input = (4,5,20,50,40)
   #act
   result=sum_numbers(test_input)
   #assert
   assert result == 119 # Parece que con una tupla la herramienta puede sumar

def test_sum_numbers_with_string():
   #arrange
   test_list = "abcd"
   #act & assert
   with pytest.raises(TypeError) as error:
      sum_numbers(test_list)
   print(f"\n[DEBUG] Mensaje real capturado: {error.value}") 