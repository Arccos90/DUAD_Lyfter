#------------------Actions-----------------------------
from finance_manager import Category, Income, Expense, AdmFinance
from datetime import datetime
from data_persistence import save_data

def validate_amount(amount_str: str)-> float:
    clean_amount_str = amount_str.replace(",",".")
    #Se incluye esta revisión de errores en casos en donde no se ingrese un float()
    try:
        amount = float(clean_amount_str)
    except ValueError:
        raise ValueError("El monto debe ingresarse como número, ejemplo: 1345")      
    if amount <= 0:
        raise ValueError("El monto debe ser mayor a cero")
    return amount
    

def process_new_category(manager: AdmFinance, name:str, color: str):
    clean_name = name.strip()
    clean_color = color.strip()

    if not clean_name:
        raise ValueError("El nombre de la categoría no debe estar vacío")
    if clean_name in manager.categories:
        raise ValueError("Esta categoria ya existe")
    if not clean_color:
        new_category = Category(clean_name)
    else:
        new_category = Category(clean_name,clean_color)
    manager.categories[new_category.name] = new_category
    save_data(manager)
    return new_category


def process_new_transaction(manager:AdmFinance, type_name:str, title:str, amount_string:str, cat_name:str):
    if not manager.categories:
        raise ValueError("No hay categorias disponibles, crea una categoria!")
    if not title.strip():
        raise ValueError("El título no puede estar vacío")
    if not cat_name or cat_name not in manager.categories:
        raise ValueError("Se debe seleccionar una categoría válida!")
    amount = validate_amount(amount_string)
    category_target = manager.categories[cat_name]
    actual_date= datetime.now().strftime("%d/%m/%Y")

    if type_name == "Ingreso":
        transaction = Income(category_target, title.strip(), amount, actual_date)
    else:
        transaction = Expense(category_target, title.strip(),amount,actual_date)

    manager.add_new_transaction(transaction)
    save_data(manager)
    return transaction
