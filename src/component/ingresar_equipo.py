import PySimpleGUI as sg
from src.windows import ingresar_equipo
from src.handlers import ingresar_equipo_handler


def start():
    """
    Lanza la ejecución de la ventana
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    
    window = ingresar_equipo.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-GUARDAR-':
            # Verificar si el valor del Input es válido antes de guardar
            if all(value != '' for value in values.values()):
                ingresar_equipo_handler.agregar_equipo(values)
                sg.popup_ok('Equipo agregado con éxito!', title='EXITO')
                break
            else:
                sg.popup_error('Los campos no pueden estar vacios', title='ERROR')

    return window