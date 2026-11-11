import json
import os
from finance_manager import Category, Income, Expense, AdmFinance

data_file = os.path.dirname(os.path.abspath(__file__))+"/finance_data.json"


def save_data(manager:AdmFinance):
    """
    Exporta la memoria del gestor hacia el archivo JSON.
    Usa el método to_dict() de las categorías y movimientos para estructurarlos.
    """
    category_dict = {}
    for name, category_target in manager.categories.items():
        category_dict[name] = category_target.to_dict()

    transaction_list = []
    for trans in manager.transactions_list:
        transaction_list.append(trans.to_dict())

    data = {
        "categories": category_dict,
        "transactions": transaction_list
    }
    with open(data_file,'w', encoding='utf-8')as file:
        json.dump(data, file, indent=4)

def load_data(manager:AdmFinance):
    """
    Importa los datos del JSON hacia la memoria del gestor al iniciar el programa.
    """
    if not os.path.exists(data_file):
        return # Si el archivo no existe, la sesión arranca en blanco.
    try:
        with open(data_file, 'r', encoding='utf-8')as file:
            data = json.load(file)
        if "categories" in data:
            for name, cat_info in data["categories"].items():
                new_cat = Category(cat_info["name"], cat_info["color"])
                manager.categories[name] = new_cat
        if "transactions" in data:
            for trans_info in data["transactions"]:
                cat_name=trans_info["category"]["name"]
                category_target=manager.categories.get(cat_name)
                if category_target:
                    if trans_info["trans_type"]== "Ingreso":
                        new_trans = Income(category_target, trans_info["description"], trans_info["amount"], trans_info["date"])
                    elif trans_info["trans_type"] == "Gasto":
                        new_trans = Expense(category_target, trans_info["description"], trans_info["amount"], trans_info["date"])

                    manager.add_new_transaction(new_trans)

    except json.JSONDecodeError:
        print("Error: El archivo JSON está corrupto o vacío")

    