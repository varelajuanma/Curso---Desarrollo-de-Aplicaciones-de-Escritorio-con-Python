import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('LightGreen6')

def build():

    layout = [
        [sg.Text('Jugador Nuevo',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text('Club', size=(15,1)), sg.Input(size=(30,1), key="-CLUB-")],
        [sg.Text('#Camiseta', size=(15,1)), sg.Spin(list(range(9999)), size=(10,1), key="-NRO_CAMISETA-")],
        [sg.Text('Nombre y Apellido', size=(15,1)), sg.Input(size=(30,1), key="-NOMBRE_Y_APELLIDO-")],
        [sg.Text('Edad', size=(15,1)), sg.Input(size=(30,1),key='-EDAD-')],
        [sg.Text('Nro Documento', size=(15,1)), sg.Input(size=(30,1),key='-DNI-')],
        [sg.Text('Altura', size=(15,1)), sg.Input(size=(30,1),key='-ALTURA-')],
        [sg.Text('Teléfono', size=(15,1)), sg.Input(size=(30,1),key='-TELEFONO-')],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Ingresar jugador', layout=layout, font=(font_name,font_size), modal=True)
    
    return window