from actions import process_new_category, process_new_transaction, AdmFinance, validate_amount
import pytest
from unittest.mock import patch

@patch('actions.save_data')
def test_process_new_category_create_new_category_without_modify_json_file(mock_safe_data):
    #arrange
    simulated_manager=AdmFinance()
    dirty_name=" Entretenimiento "
    color = '#FF0000'
    #act
    process_new_category(simulated_manager, dirty_name, color)

    assert "Entretenimiento" in simulated_manager.categories
    mock_safe_data.assert_called_once()

@patch('actions.save_data')
def test_process_new_transaction_create_new_transaction_without_modify_json_file_call_error(mock_safe_data):
    #arrange
    simulated_manager=AdmFinance()
    simulated_type_name = "Gasto"
    simulated_title = "Prueba Pytest"
    simulated_amount = "1234,1"
    simulated_category= "Entretenimiento"
    
    #act
    with pytest.raises(ValueError) as exc_info:
        process_new_transaction(simulated_manager,simulated_type_name,simulated_title,simulated_amount,simulated_category)
        assert "Se debe seleccionar una categoría válida" in str(exc_info.value)
    print(f"\n[DEBUG] el mensaje de error es: {exc_info.value}")
    mock_safe_data.assert_not_called()


def test_validate_amount_fix_decimal_format ():
    #arrange
    test_amount = "1325,25"
    #act
    result = validate_amount(test_amount)

    assert result == float(1325.25)
    print(f"El valor convertido es: {result}")


def test_validate_amount_fix_string_value ():
    #arrange
    test_amount = "mil quinientos"
    #act
    with pytest.raises(ValueError) as exc_info:
        validate_amount(test_amount)
        assert "El monto debe ingresarse como número, ejemplo: 1345" in str(exc_info.value)
    print(f"\n[DEBUG] el mensaje de error es: {exc_info.value}")