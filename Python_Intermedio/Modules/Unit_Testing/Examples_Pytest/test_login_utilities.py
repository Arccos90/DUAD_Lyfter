import pytest
from login_utilities import try_login

def test_try_login_with_correctly_credential_return_true ():
    #Arrange
     email_input = "a@gmail.com"
     password = "123"
     #Act
     result = try_login(email_input,password)
     assert result

def test_try_login_with_incorrect_credential_return_true ():
    #Arrange
     email_input = "b@gmail.com"
     password = "123"
     #Act & Assert
     with pytest.raises(ValueError):
        try_login(email_input,password)
     