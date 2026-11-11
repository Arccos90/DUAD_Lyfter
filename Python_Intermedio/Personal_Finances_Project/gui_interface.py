import FreeSimpleGUI as sg
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

def ventana_agregar_categoria(manager: AdmFinance):
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

def calcular_monto_compuesto():
    """
    Despliega una mini-calculadora donde el usuario puede ingresar
    una fórmula matemática simple (sumas/restas) y retorna el resultado.
    """
    layout = [
        [sg.Text("Ingresa los montos a sumar o restar (ej. ₡500 + ₡350 - ₡50):")],
        [sg.Input(key="-CALC-EXPR-")],
        [sg.Button("Calcular"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Calculadora", layout)
    
    resultado_final = None
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Calcular":
            expresion = values["-CALC-EXPR-"]
            try:
                # eval() evalúa el string como código Python. 
                # En un entorno controlado como este, nos permite sumar la cadena fácilmente.
                resultado_final = float(eval(expresion))
                break
            except Exception:
                sg.popup_error("Expresión inválida. Usa solo números, '+' y '-'.")
    window.close()
    return resultado_final

def ventana_agregar_movimiento(manager: AdmFinance, tipo: str):
    # Verificación temprana exigida por las instrucciones
    if not manager.categories:
        sg.popup_error("Error: No hay categorías disponibles. Crea una categoría primero.")
        return

    nombres_categorias = list(manager.categories.keys())
    
    layout = [
        [sg.Text(f"Nuevo {tipo}", font=("Helvetica", 14, "bold"))],
        [sg.Text("Título:"), sg.Input(key="-TITULO-")],
        [sg.Text("Monto:"), sg.Input(key="-MONTO-", size=(25,1)), sg.Button("🧮 Calcular", key="-BTN_CALC-")],
        [sg.Text("Categoría:"), sg.Combo(nombres_categorias, key="-CATEGORIA-", readonly=True, size=(20, 1))],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]
    window = sg.Window(f"Agregar {tipo}", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break

        if event == "-BTN_CALC-":
            monto_calculado = calcular_monto_compuesto()
            if monto_calculado is not None:
                # Actualiza el valor de la ventana con el resultado
                window["-MONTO-"].update(monto_calculado)

        if event == "Guardar":
            try:
                actions.process_new_transaction(
                    manager, tipo, values["-TITULO-"], values["-MONTO-"], values["-CATEGORIA-"]
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
    for mov in manager.transactions_list:
        # Formateamos el monto para que incluya el símbolo y 2 decimales
        monto_str = f"₡{mov.amount:,.2f}" 
        
        # Agregamos cada fila como una sublista [Fecha, Tipo, Categoría, Descripción, Monto]
        fila = [mov.date, mov.trans_type, mov.category.name, mov.description, monto_str]
        table_data.append(fila)
    return table_data

def draw_main_window(manager: AdmFinance):
    """
    Dibuja la ventana principal, con la tabla y los balances actualizados.
    """
    # 1. Calculamos los totales y preparamos los datos de la tabla
    total_incomes = manager.sum_incomes()
    total_expenses = manager.sum_expenses()
    balance = manager.calc_balance()
    table_data = build_table_data(manager)

    # 2. Definimos los encabezados de la tabla
    headings = ['Fecha', 'Tipo', 'Categoría', 'Descripción', 'Monto']

    # 3. Definimos el diseño (layout) de la interfaz gráfica
    layout = [
        # Título
        [sg.Text("Gestor de Finanzas Personales", font=("Helvetica", 16, "bold"), justification="center")],
        
        # Panel de Resumen Financiero
        [
            sg.Frame("Resumen Financiero", [
                [sg.Text(f"Ingresos Totales: ₡{total_incomes:,.2f}", text_color="green",background_color="White", font=("Helvetica", 12))],
                [sg.Text(f"Gastos Totales: ₡{total_expenses:,.2f}", text_color="red",background_color="white" ,font=("Helvetica", 12))],
                [sg.Text(f"Balance Neto: ₡{balance:,.2f}", background_color="black",font=("Helvetica", 12, "bold"))]
            ], element_justification='center')
        ],
        
        # Tabla de Movimientos
        [sg.Table(values=table_data, headings=headings, max_col_width=25,
                  auto_size_columns=True, justification='center', num_rows=15, 
                  key='-TABLE-', row_height=30, expand_x=True, expand_y=True)],
        
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
            
        # Cuando el usuario agrega algo, la ventana principal necesita refrescarse para mostrar 
        # el nuevo registro en la tabla. En Tkinter/FreeSimpleGUI, la forma más limpia de hacerlo 
        # es cerrar la ventana actual y volver a dibujarla con los datos actualizados.
        
        if event == "Agregar Categoría":
            ventana_agregar_categoria(manager)
            window.close()
            draw_main_window(manager) # Refresca la ventana
            return # Evita que el bucle viejo siga corriendo en segundo plano
            
        elif event == "Agregar Ingreso":
            ventana_agregar_movimiento(manager, "Ingreso")
            window.close()
            draw_main_window(manager)
            return
            
        elif event == "Agregar Gasto":
            ventana_agregar_movimiento(manager, "Gasto")
            window.close()
            draw_main_window(manager)
            return

    window.close()