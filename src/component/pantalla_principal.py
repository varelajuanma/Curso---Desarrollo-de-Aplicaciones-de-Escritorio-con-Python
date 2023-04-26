import PySimpleGUI as sg
import json
from src.windows import pantalla_principal
from src.component import ingresar_equipo
from src.component import ingresar_jugador
from src.component import pantalla_acerca_de
from src.handlers import ingresar_equipo_handler
from src.handlers import ingresar_jugador_handler
from src.handlers import borrar_elemento_handler

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
    window = pantalla_principal.build()
    window["-TABLA_EQUIPOS-"].update(ingresar_equipo_handler.leer_archivo())
    window["-TABLA_JUGADORES-"].update(ingresar_jugador_handler.leer_archivo())

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        if event == 'Ingresar nuevo equipo':
            ingresar_equipo.start()
            window["-TABLA_EQUIPOS-"].update(ingresar_equipo_handler.leer_archivo())
        
        if event == 'Ingresar nuevo jugador':
            ingresar_jugador.start()
            window["-TABLA_JUGADORES-"].update(ingresar_jugador_handler.leer_archivo())
 
        if event == 'Acerca de':
            pantalla_acerca_de.start()

        if event == '-BORRAR_TODO-':
            if sg.popup_yes_no('Esta por borrar toda la informacíon ¿Esta seguro?') == 'Yes':
                borrar_elemento_handler.borrar_todo()
                sg.popup_ok('Se han eliminado todos los datos correctamente', title="Datos eliminados")
                window["-TABLA_EQUIPOS-"].update(ingresar_equipo_handler.leer_archivo())
                window["-TABLA_JUGADORES-"].update(ingresar_jugador_handler.leer_archivo())
            
        if event == 'Eliminar equipo':
            borrar_elemento_handler.borrar_equipo(values)
            sg.popup_ok('El equipo seleccionado fue eliminado correctamente', title="Equipo eliminado")
            window["-TABLA_EQUIPOS-"].update(ingresar_equipo_handler.leer_archivo())
        
        if event == 'Eliminar jugador':
            borrar_elemento_handler.borrar_jugador(values)
            sg.popup_ok('El jugador seleccionado fue eliminado correctamente', title="Jugador eliminado")
            window["-TABLA_JUGADORES-"].update(ingresar_jugador_handler.leer_archivo())

        if event == 'Salir':
            break
      
    return window

