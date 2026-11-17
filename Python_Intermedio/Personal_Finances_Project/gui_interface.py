import FreeSimpleGUI as sg
import re
from auth_manager import load_credentials, save_credentials
import actions
from finance_manager import AdmFinance

def draw_login_window():
    creds = load_credentials()
    
    # Caso A: No hay cuenta creada (Registro)
    if creds is None:
        layout = [
            [sg.Text("Bienvenido. Crea tu cuenta de administrador:")],
            [sg.Text("Usuario:"), sg.Input(key="-USER-")],
            [sg.Text("Contraseña:"), sg.Input(key="-PWD-", password_char="*")],
            [sg.Text("Palabra clave para recuperar (ej. tu mascota):"), sg.Input(key="-HINT-")],
            [sg.Button("Registrar")]
        ]
        window = sg.Window("Registro Inicial", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return False
            if event == "Registrar":
                save_credentials(values["-USER-"], values["-PWD-"], values["-HINT-"])
                sg.popup("Cuenta creada exitosamente. Reinicia la aplicación para entrar.")
                window.close()
                return False

    # Caso B: Ya existe una cuenta (Login)
    else:
        layout = [
            [sg.Text("Inicio de Sesión", font=("Helvetica", 14, "bold"))],
            [sg.Text("Usuario:"), sg.Input(key="-USER-")],
            [sg.Text("Contraseña:"), sg.Input(key="-PWD-", password_char="*")],
            [sg.Button("Entrar"), sg.Button("Olvidé mi contraseña")]
        ]
        window = sg.Window("Login", layout)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return False
                
            if event == "Entrar":
                if values["-USER-"] == creds["username"] and values["-PWD-"] == creds["password"]:
                    window.close()
                    return True # Autorización exitosa
                else:
                    sg.popup_error("Usuario o contraseña incorrectos.")
                    
            if event == "Olvidé mi contraseña":
                answer = sg.popup_get_text("Pregunta de seguridad: ¿Cuál es tu palabra clave?")
                if answer == creds["security_answer"]:
                    new_pwd = sg.popup_get_text("Ingresa tu nueva contraseña:")
                    if new_pwd:
                        save_credentials(creds["username"], new_pwd, creds["security_answer"])
                        sg.popup("Contraseña actualizada. Intenta entrar de nuevo.")
                        creds["password"] = new_pwd # Actualiza la memoria actual
                else:
                    sg.popup_error("Palabra clave incorrecta.")

def window_add_category (manager: AdmFinance):
    layout = [
        [sg.Text("Nombre de Categoría:"), sg.Input(key="-NOMBRE-")],
        [sg.Text("Color:"), sg.Input(key="-COLOR-", size=(10,1)), sg.ColorChooserButton("Elegir Color", target="-COLOR-")],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Nueva Categoría", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Guardar":
            try:
                actions.process_new_category(manager, values["-NOMBRE-"], values["-COLOR-"])
                sg.popup("Categoría guardada exitosamente.")
                break
            except ValueError as e:
                sg.popup_error(str(e))
    window.close()

def compound_amount_calculator(value: str) ->float:
    # El objetivo es limpiar el dato que se ingrese en la calculadora de cualquier elemento que afecte su funcion como $,% entre otros.
    clean_value=value.replace("₡", "").replace("$", "").replace(" ", "").replace(",",".")
    clean_value=clean_value.replace("+"," + ").replace("-"," - ")
    split= clean_value.split()
    print(split)
    if not split:
        return 0.0
    total= float(split[0])
    print(total)
    # el objetivo es recorrer la lista para determinar que elemento se debe sumar o restar. La lista se recorre de 2 en 2 para conocer el simbolo de suma o resta.
    for i in range(1,len(split),2):
        operator = split[i]
        next_number = float(split[i+1])
        if operator == "+":
            total += next_number
            print(total)
        elif operator == "-":
            total -= next_number
            print (total)
    print(total)
    return total
    
    
def calculate_compound_amount():
    """
    Despliega una mini-calculadora donde el usuario puede ingresar
    una fórmula matemática simple (sumas/restas) y retorna el resultado.
    """
    layout = [
        [sg.Text("Ingresa los AMOUNTs a sumar o restar (ej. ₡500 + ₡350 - ₡50):")],
        [sg.Input(key="-CALC-EXPR-")],
        [sg.Button("Calcular"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Calculadora", layout)
    
    final_result = None
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Calcular":
            expresion = values["-CALC-EXPR-"]
            try:
                # se omitió eval() y se llama a la función compound_amount_depurator
                final_result = float(compound_amount_depurator(expresion))
                break
            except Exception:
                sg.popup_error("Expresión inválida. Usa solo números, '+' y '-'.")
    window.close()
    return final_result

def windows_add_transactions(manager: AdmFinance, tipo: str):
    # Verificación temprana exigida por las instrucciones
    if not manager.categories:
        sg.popup_error("Error: No hay categorías disponibles. Crea una categoría primero.")
        return

    categories_names = list(manager.categories.keys())
    
    layout = [
        [sg.Text(f"Nuevo {tipo}", font=("Helvetica", 14, "bold"))],
        [sg.Text("Título:"), sg.Input(key="-TITLE-")],
        [sg.Text("AMOUNT:"), sg.Input(key="-AMOUNT-", size=(25,1)), sg.Button("🧮 Calcular", key="-BTN_CALC-")],
        [sg.Text("Categoría:"), sg.Combo(categories_names, key="-CATEGORY-", readonly=True, size=(20, 1))],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]
    window = sg.Window(f"Agregar {tipo}", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break

        if event == "-BTN_CALC-":
            calculated_amount = calculate_compound_amount()
            if calculated_amount is not None:
                # Actualiza el valor de la ventana con el resultado
                window["-AMOUNT-"].update(calculated_amount)

        if event == "Guardar":
            try:
                actions.process_new_transaction(
                    manager, tipo, values["-TITLE-"], values["-AMOUNT-"], values["-CATEGORY-"]
                )
                sg.popup(f"{tipo} guardado exitosamente.")
                break
            except ValueError as e:
                sg.popup_error(str(e))
    window.close()

def build_table_data(manager: AdmFinance):
    """
    Función auxiliar para leer la lista de transacciones del modelo financiero 
    y convertirla en una lista de listas que sg.Table pueda procesar.
    """
    table_data = []
    row_colors = [] # Tabla para aplicar los colores de las CATEGORYs.

    for index, mov in enumerate(manager.transactions_list):
        # Formateamos el AMOUNT para que incluya el símbolo y 2 decimales
        AMOUNT_str = f"₡{mov.amount:,.2f}" 

        
        # Agregamos cada fila como una sublista [Fecha, Tipo, Categoría, Descripción, AMOUNT]
        fila = [mov.date, mov.trans_type, mov.category.name, mov.description, AMOUNT_str]
        table_data.append(fila)
        colors = mov.category.color
        row_colors.append((index,colors))
        print(row_colors)
    return table_data,row_colors

def draw_main_window(manager: AdmFinance):
    """
    Dibuja la ventana principal, con la tabla y los balances actualizados.
    """
    # 1. Calculamos los totales y preparamos los datos de la tabla
    total_incomes = manager.sum_incomes()
    total_expenses = manager.sum_expenses()
    balance = manager.calc_balance()
    table_data, table_colors = build_table_data(manager)

    # 2. Definimos los encabezados de la tabla
    headings = ['Fecha', 'Tipo', 'Categoría', 'Descripción', 'AMOUNT']

    # 3. Definimos el diseño (layout) de la interfaz gráfica
    layout = [
        # Título
        [sg.Text("Gestor de Finanzas Personales", font=("Helvetica", 16, "bold"), justification="center")],
        
        # Panel de Resumen Financiero
        [
                sg.Frame("Resumen Financiero", [
                [sg.Text(f"Ingresos Totales: ₡{total_incomes:,.2f}", text_color="green", font=("Helvetica", 12), key='-LBL_INCOME-')],
                [sg.Text(f"Gastos Totales: ₡{total_expenses:,.2f}", text_color="red", font=("Helvetica", 12), key='-LBL_EXPENSE-')],
                [sg.Text(f"Balance Neto: ₡{balance:,.2f}", text_color="white", font=("Helvetica", 12, "bold"), key='-LBL_BALANCE-')]
            ], element_justification='center')
        ],
        
        # Tabla de Movimientos
        [sg.Table(values=table_data, headings=headings, max_col_width=25,
                  auto_size_columns=True, justification='center', num_rows=15, 
                  key='-TABLE-', row_height=30, expand_x=True, expand_y=True,row_colors=table_colors)],
        
        # Botones de Acción
        [
            sg.Button("Agregar Categoría", button_color="blue"), 
            sg.Button("Agregar Ingreso", button_color="green"),
            sg.Button("Agregar Gasto", button_color="red")
        ],
        
        # Salida
        [sg.Button("Salir", button_color="black")]
    ]

    window = sg.Window("Finanzas Personales", layout, size=(900, 700), element_justification='c', resizable=True, finalize=True)
    window.maximize()
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Salir":
            break
        # Ejecutamos las ventanas secundarias
        if event == "Agregar Categoría":
            window_add_category (manager)
          
        elif event == "Agregar Ingreso":
            windows_add_transactions(manager, "Ingreso")
           
        elif event == "Agregar Gasto":
            windows_add_transactions(manager, "Gasto")

        # DESPUÉS de cualquier acción, recalculamos y actualizamos la interfaz actual
        # sin cerrar la ventana ni llamar a draw_main_window de forma recursiva.
        
        # 1. Obtenemos los nuevos valores del modelo           
        new_incomes = manager.sum_incomes()
        new_expenses = manager.sum_expenses()
        new_balance = manager.calc_balance()
        new_table_data, new_table_colors = build_table_data(manager)

        
        # 2. Inyectamos los nuevos valores en la interfaz gráfica usando .update()
        window['-LBL_INCOME-'].update(f"Ingresos Totales: ₡{new_incomes:,.2f}")
        window['-LBL_EXPENSE-'].update(f"Gastos Totales: ₡{new_expenses:,.2f}")
        window['-LBL_BALANCE-'].update(f"Balance Neto: ₡{new_balance:,.2f}")
        window['-TABLE-'].update(values=new_table_data, row_colors=new_table_colors)       

    window.close()