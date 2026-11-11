from gui_interface import draw_login_window, draw_main_window
from finance_manager import AdmFinance
from data_percistence import load_data

def main():
    gestor_activo = AdmFinance()
    # Solo si la función login retorna True, dibuja el programa completo
    if draw_login_window():
        load_data(gestor_activo)
        draw_main_window(gestor_activo)

if __name__ == '__main__':
    main()