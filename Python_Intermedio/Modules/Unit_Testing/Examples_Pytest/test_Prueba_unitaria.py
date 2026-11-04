from Prueba_unitaria import suma
def test_sum_sums_correctly():
#Arrange
    a = 3
    b = 5
    #Act
    result = suma(a,b)
    #Assert
    assert result == 8