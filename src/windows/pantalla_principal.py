import PySimpleGUI as sg
from src.consts import font

def build():
    """
    Construye la ventana principal
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('SandyBeach')

    menu_def = [
        ['Funciones', ['Ingresar nuevo equipo', 'Ingresar nuevo jugador', 'Salir']],
        ['Información', ['Acerca de']],
    ]

    right_click_equipo = ['',['Eliminar equipo']]
    right_click_jugador = ['',['Eliminar jugador']]
    
    layout_equipos = [
        [sg.Menu(menu_def)],
        [sg.Text("Equipos", font=(font.font_name, 20, "underline"), size=(30, 1), justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Table(values=[["-", "-", "-", "-", "-"]], key="-TABLA_EQUIPOS-", justification='center',
            headings=["    Nombre    ", "    Domicilio    ", "   Localidad   ", " Teléfono "],
            row_height=20, num_rows=10, header_background_color="#AFAFAF", right_click_menu=right_click_equipo)],
    ]

    layout_jugadores = [
        [sg.Text("Jugadores", font=(font.font_name, 20, "underline"), size=(30, 1), justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Table(values=[["-", "-", "-", "-", "-", "-", "-", "-"]], key="-TABLA_JUGADORES-", justification='center',
            headings=["    Club    ", "# Camiseta", " Nombre y Apellido ", "Edad", " Nro Documento ", "Altura", " Teléfono "],
            row_height=20, num_rows=10, header_background_color="#AFAFAF", right_click_menu=right_click_jugador)],
        [sg.Button('BORRAR TODO', size=(14, 1),key="-BORRAR_TODO-", bind_return_key=True)],
        [sg.HorizontalSeparator()],
        [sg.Text("Para eliminar solo un equipo o jugador de la tabla debe posicionarse en el elemento con click izquierdo, luego darle al click derecho y en eliminar.", font=(font.font_name, 10), justification="center")]
    ]
    
    window = sg.Window("Sistema de Informacíon de Torneos", layout=[layout_equipos, layout_jugadores], use_custom_titlebar=True, finalize=True, resizable=True, modal=True)

    return window
