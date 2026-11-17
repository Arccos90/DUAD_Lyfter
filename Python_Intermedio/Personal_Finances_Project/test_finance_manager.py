from finance_manager import AdmFinance, Income,Expense,Category
import pytest

def test_sum_incomes_calcula_total_ignorando_gastos():
    manager = AdmFinance()
    cat_salario = Category("Salario", "#00FF00")
    cat_comida = Category("Comida", "#FF0000")
    
    manager.add_new_transaction(Income(cat_salario, "Quincena 1", 500.0, "01/10/2026"))
    manager.add_new_transaction(Income(cat_salario, "Quincena 2", 500.0, "15/10/2026"))
    manager.add_new_transaction(Expense(cat_comida, "Supermercado", 200.0, "16/10/2026"))
    
    total_ingresos = manager.sum_incomes()
    
    assert total_ingresos == 1000.0
    print(f"El total usando sum_incomes es:{total_ingresos}")


def test_sum_expenses_calcula_total_ignorando_ingresos():
    manager = AdmFinance()
    cat_salario = Category("Salario", "#00FF00")
    cat_comida = Category("Comida", "#FF0000")

    manager.add_new_transaction(Income(cat_salario, "Quincena 1", 500.0, "01/10/2026"))
    manager.add_new_transaction(Income(cat_salario, "Quincena 2", 500.0, "15/10/2026"))
    manager.add_new_transaction(Expense(cat_comida, "Supermercado", 200.0, "16/10/2026"))
    
    total_ingresos = manager.sum_expenses()
    
    assert total_ingresos == 200.0
    print(f"El total usando sum_expenses es:{total_ingresos}")


def test_calc_balance_calculate_total():
    manager = AdmFinance()
    
    cat_salario = Category("Salario", "#00FF00")
    cat_comida = Category("Comida", "#FF0000")
    
    manager.add_new_transaction(Income(cat_salario, "Quincena 1", 500.0, "01/10/2026"))
    manager.add_new_transaction(Income(cat_salario, "Quincena 2", 500.0, "15/10/2026"))
    manager.add_new_transaction(Expense(cat_comida, "Supermercado", 200.0, "16/10/2026"))
    
    total_ingresos = manager.calc_balance()
    

    assert total_ingresos == 800.0
    print(f"El total usando calc_balanca es:{total_ingresos}")