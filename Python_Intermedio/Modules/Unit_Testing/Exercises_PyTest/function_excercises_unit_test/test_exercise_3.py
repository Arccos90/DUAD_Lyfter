from exercise_3 import sum_numbers
def test_sum_numbers_sums_correctly ():
 #arrange
 test_list = [4,5,20,50,40]
 #act
 result = sum_numbers(test_list)
 assert result == 119
