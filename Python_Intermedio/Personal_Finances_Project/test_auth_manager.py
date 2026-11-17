from auth_manager import process_new_user
import pytest

def test_process_new_user_with_blanc_spaces_user():
    test_user = ""
    test_pwd = "Sansa"

    with pytest.raises(ValueError) as exc_info:
        process_new_user(test_user,test_pwd)
        assert "El nombre de usuario no puede estar vacío." in str(exc_info.value)
    print(f"\n[DEBUG] el mensaje de error es: {exc_info.value}")