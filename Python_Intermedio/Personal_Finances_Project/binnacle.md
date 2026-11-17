
[] = Abierto ó sin hacer
[x] = Finalizado
[*] = En Proceso


Backlog:
1. Requerimientos Funcionales y de Lógica de Negocio
>>Gestión de Categorías:
[x] El usuario debe poder crear y guardar nuevas categorías de movimientos.
[x] Debe solicitarse un nombre y un color (como código HEX) para la categoría.
[x] No se deben permitir categorías con nombres duplicados o vacíos.

>>Registro de Movimientos (Ingresos y Gastos):
[x] El usuario debe poder registrar nuevos ingresos y gastos de forma diferenciada.
[x] Para registrar un movimiento, el usuario debe ingresar un título, un monto y seleccionar una categoría previamente creada.
[x] No se debe permitir registrar un movimiento si no hay categorías creadas.
[x] El sistema debe asignar automáticamente la fecha actual de registro al movimiento.

>>Validaciones de Entrada:
[x] Los montos de los movimientos deben ser estrictamente numéricos (flotantes) y mayores a cero.
[x] Se deben limpiar los datos ingresados para manejar formatos (ej. reemplazar comas por puntos en los decimales).
[x] Los textos ingresados (títulos, nombres de categoría) no deben estar vacíos.

>>Cálculos Financieros:
[x] El sistema debe ser capaz de calcular el total de los ingresos acumulados.
[x] El sistema debe ser capaz de calcular el total de los gastos acumulados.
[x] El sistema debe calcular el balance final neto (Total Ingresos - Total Gastos).

2. Requerimientos de Arquitectura (POO y Modularidad)
>>Programación Orientada a Objetos (POO):
[x] Se debe implementar una clase base Transaction que almacene la categoría (como objeto, aplicando composición), el tipo de transacción, la descripción, el monto y la fecha.
[x] Se deben implementar clases hijas Income (Ingreso) y Expense (Gasto) que hereden de Transaction para automatizar la asignación del tipo de movimiento.
[x] Se debe implementar una clase Category para representar las etiquetas de clasificación con nombre y color.
[x] Se debe implementar una clase central GestorFinanzas que mantenga el estado de la aplicación en memoria activa (almacenando la lista de movimientos y el diccionario de categorias)

>> Estructura Modular (MVC / Capas):

[x] El código debe estar separado en módulos con responsabilidades únicas:
    [x] finance_manager.py: Contiene las clases del modelo de datos y la lógica de negocio.
    [x] gui_interface.py: Exclusivo para la definición de ventanas y captura de eventos visuales (FreeSimpleGUI).
    [x]actions.py: Actúa como controlador intermedio para validar datos visuales e interactuar con el gestor en memoria.
    [x]data_persistence.py: Encargado exclusivo de leer y escribir archivos.
    [x]auth_manager.py: Encargado de la lógica de autenticación.
    [x]main.py: Orquestador principal que instancie el modelo e inicie el flujo gráfico.

3. Requerimientos de Interfaz Gráfica (GUI)
>> Sistema de Autenticación Visual(Esto es algo que yo quise implementar):
[x] El programa debe iniciar mostrando un sistema de autenticación antes de acceder al gestor principal.
[x] Si es la primera vez (no hay cuentas), debe mostrar un formulario de Registro Inicial pidiendo Usuario, Contraseña (oculta con asteriscos *) y una "Palabra Clave" (pregunta de seguridad).
[x] Si ya hay cuenta, debe mostrar un formulario de Inicio de Sesión que solicite credenciales y valide el acceso.
[x] Debe incluir un botón de "Olvidé mi contraseña" que permita restablecerla si el usuario ingresa correctamente su palabra clave de seguridad.

>>Menú Principal (Gestor):
[x] Debe construirse usando la librería FreeSimpleGUI.
[x] Debe tener un título principal claro.
[x] Debe incluir botones claramente identificables (con colores sugeridos) para "Agregar Categoría", "Agregar Ingreso", "Agregar Gasto" y "Salir".
[x] Debe existir un área o contenedor reservado para mostrar una tabla de los movimientos registrados.
[x] Debe manejar adecuadamente los errores visuales (ej. lanzar ventanas emergentes sg.popup_error si una validación falla, sin cerrar o colapsar el programa completo).
    > Esta pendiente validar diferentes tipos de error, de momento notifica cuando no esta creada una categoria. 
4. Requerimientos de Persistencia de Datos
>> Almacenamiento Local de Datos:
[x] La información de las cuentas de usuario (credenciales) debe guardarse en un archivo JSON local (ej. credenciales.json).
[x] La información de las finanzas (categorías y movimientos) debe exportarse e importarse desde un archivo JSON (ej. finance_data.json).
[x] Las clases del modelo de datos deben contar con un método (ej. .to_dict()) para traducir sus variables internas a una estructura de diccionarios anidados compatible con la librería json antes de guardar.
[x] Al abrir el programa (tras un inicio de sesión exitoso), los datos del archivo financiero deben cargarse y reconstruir automáticamente la memoria del

Worlsession: 06/11/26 - 09/11/26
Agenda
[x] Crear un documento para registrar los requerimientos y avances y temas pendientes por trabajar
[x] Definir la estructura del programa. Módulos, Clases, métodos. Tomando en cuenta POO
[x] Trabajar en los requerimientos de la interfaz 
R/ me apoyé con IA para trabajar esta parte. Luego hice ajustes para customizar algunas cosas a mi criterio.
[x] Trabajar en las funcionalidades de ingreso con uso de credenciales, esto es algo que quiero que tenga el programa.


Worksession: 10/11/26
Agenda:
[x] Voy a revisar por que no esta guardando los archivos JSON en la dirección definida.
R/Listo, incluí que los archivos JSON, usen la dirección de la carpeta para que guarde y lea los archivos.
[x] Validar que las transacciones se estén guardando con la fecha actual de manera automatica.
R/Listo, las transacciones se guarda usando el modulo Date de python.
[x] Revisar si se puede incluir una calculadora para hacer sumas, restas o multiplicaciones, cuando se desea ingresar una transacción.
R/Listo, se incluyó un boton que abre una ventana en donde se puede indicar montos y simbolos para realizar las operaciones básicas.
[x] Trabajar en como mostrar la tabla de transacciones en la interfaz.
R/ Ya el programa muestra las transacciones realizadas.

To_do:
[] incluir funciones para modificar o eliminar transacciones.
[] incluir funciones para modificar o eliminar categorias.
[] hacer test de métodos
[] trabajar en requerimientos extra 
[] Definir filtros para mostrar información en la tabla

Worksession: 16/11/26
To_do:
>>>> It's feedback of the first commit.
>>>Notes:
1. Se cambio el txt a un formato .md para poder hacer mas visual la bitacora.
2. Se dará prioridad al feedback del primer entregable
3. Posterior se incluiran las funcionalidades del sprint anterior.

[x] 1.En **process_new_transaction**, las validaciones de categorías vacías y título vacío solo hacen print, así que el flujo continúa y se puede guardar un movimiento sin título. Verifica que esas validaciones detengan el proceso igual que lo hace la de la categoría, para que la interfaz pueda mostrar el error con sg.popup_error.
>>R/ Cambié los prints por raise ValueError. 

[x] 2.Cuando el monto no es un número (por ejemplo "abc"), *float()*  lanza un ValueError con un mensaje en inglés que llega tal cual al usuario. Revisa cómo podrías capturar ese caso en *validate_amount* para mostrar un mensaje más claro.
>>R/ Revise el método validate_amount. Agregué un try/except ValueError para que capte todo lo que no sea un float como un error. Y muestre el mensaje más claro del tipo de error y no deje continuar el programa hasta que sea corregido o modificado.

[x] 3.La calculadora usa *eval()*, que ejecuta cualquier código Python que se escriba en ese campo, no solo sumas y restas. Además, el propio ejemplo que muestras ("₡500 + ₡350 - ₡50") falla porque el símbolo ₡ no es válido para Python. Investiga una forma de separar la expresión en números y operadores y hacer el cálculo tú mismo, así controlas exactamente qué se permite.
>>R/ Sustituí *eval()* por una funcion llamada depurador_monto_compuesto. Con esto lo que se busca es "limpiar" el valor o la expresión que el usuario introduzca, para que sea acorde a las funcionalidades de la calculadora. Si se ingresa $ o ₡ la función lo va a traducir a un float sencillo.

[x] 4.Para refrescar la ventana principal, *draw_main_window* se llama a sí misma cada vez que se agrega algo, incluso si el usuario presiona "Cancelar". Eso es recursión: cada acción deja una llamada abierta en la pila. Revisa el método *update()* de los elementos de FreeSimpleGUI, por ejemplo window["-TABLE-"].update(values=...) y lo mismo para los textos del resumen, para actualizar la tabla sin cerrar y volver a construir la ventana.

>>>R/ Acá se aplicaron las sugerencias de no cerrar y volver a llamar la funcion *draw_main_windows* si no usar .update(). Tuve que buscar información de como hacer para no afectar lo que ya estaba estructurado.

[X] 5.En **process_new_category**, la verificación de duplicados se hace con el nombre sin strip(), pero luego se guarda limpio, así que " Comida" pasa la validación aunque "Comida" ya exista. También, si el usuario no elige color, se guarda un string vacío y el valor por defecto "#FFFFFF" de Category nunca se usa. Verifica ambos casos.
>>>R/ Se corrigió incluyendo que para ambos parametros (name & color) se ejecute usando .strip(). Y modifique la funcion para que cuando el usuario no ingrese color, no se guardará como vacío si no con el valor por defecto de las Clase Category()

[x] 6.En **load_data**, si un movimiento tiene un trans_type distinto de "Ingreso" o "Gasto", la variable new_trans no se crea en esa vuelta y se termina agregando la del movimiento anterior (o falla si es el primero). Además, cada transacción guarda en el JSON el diccionario completo de su categoría, duplicando el color. ¿Qué dato mínimo necesitas realmente guardar para reconstruir la relación?
>>>R/ _Ahora busca la información de la transacción como un str, ya que estaba como un un diccionario. Y se agrega como una nueva transacción.
>>>   _Solo se necesito el nombre de la categoría, no vamos a cargar el código del color.

[x] 7.Ya estás recolectando el color de cada categoría, pero todavía no se usa en la tabla. Si quieres completar ese requerimiento opcional, revisa el parámetro row_colors de sg.Table.
>>> R/ busque en internet como hacerlo, por que tenia que enlazar la informacions guardada para poder mostrar el color para cada transaccions-categoria. agregue una lista row_color.

[x] 8.Todos los identificadores de código deben estar en inglés. En gui_interface.py hay varios en español: ventana_agregar_categoria, ventana_agregar_movimiento, calcular_monto_compuesto, nombres_categorias, resultado_final, expresion, monto_str, fila, tipo y las keys como NOMBRE-, TITULO-, MONTO-. Los textos que ve el usuario sí pueden quedarse en español. Revisa también los nombres de archivo data_percistence.py y credencials.json, y el parámetro type en process_new_transaction, que oculta la función integrada de Python con ese nombre.
>>> Se modificaron los nombre de variables y funciones en espanol en el módulo gui_interface.py
>>> Se corrigieron los nombres de los archivos .py (credentials.py y data_persistence.py)
>>> modifique la variable type por type_name para que no afecte con la función integrada de python.

[*] 9.El PR incluye carpetas __pycache__ con archivos .pyc, además de credencials.json con tu usuario y contraseña en texto plano y finance_data.json con tus datos. Investiga cómo usar un archivo .gitignore para que nada de eso se suba al repositorio.
>>> para el próximo commit se omitira estos archivos.
> 1. Elimina las credenciales del rastreo de Git
    git rm --cached Python_Intermedio/Personal_Finances_Project/credentials.json
> 2. Elimina la base de datos personal del rastreo de Git
    git rm --cached Python_Intermedio/Personal_Finances_Project/finance_data.json
> 3. Elimina toda la caché de Python del rastreo de Git
    find . -name "__pycache__" -exec git rm -r --cached {} +
    find . -name "*.pyc" -exec git rm -r --cached {} +
    >>> no estoy seguro de esta parte, luego de este commit valido si funcionó esta parte.

[x] 10.El archivo test_logic.py está vacío y el enunciado pide mínimo 8 pruebas unitarias que corran sin la interfaz. Tu lógica ya está bastante bien separada, así que tienes buenos candidatos: 
>>> voy a utilizar una carpeta llamada Test y haré un .py para cada módulo a testear.
>validate_amount: Listo, prueba si se corrige el uso de "," como decimal a "."
>                 También se hizo un test para validar el error si se ingresa un string                      
>process_new_category: Listo
>process_new_transaction: Listo, identifica si la categoria existe
>sum_incomes: Listo, solo suma incomes
>sum_expenses: Listo, solo suma expenses
>calc_balance: Listo, suma todo y da el balance final.
>process_new_user: Listo, se valida si al crear un usuario se deja algun valor en blanco.
Revisa también que al probar actions no termines escribiendo sobre tu finance_data.json real, ya que esas funciones llaman a save_data. ¿Cómo podrías probar esa lógica sin tocar tus datos?
>>> Encontré una manera de hacer estas pruebas sin afectar finance_data.json. El método se llama "Mocking" hay que importar una libreria *from unittest.mock import patch*

[x] En el registro inicial se puede crear una cuenta con usuario o contraseña vacíos. Como es un extra que tú mismo agregaste, vale la pena aplicarle las mismas validaciones básicas que al resto de formularios.
>>> Se incorporó una validación con .strip y un ciclio de validación para evitar que se ingrese dejando vacios los espacios. ahora lanza un error pero no cierra el programa, solo pide que vuelva a ingresa la información.