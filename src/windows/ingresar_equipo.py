import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('LightGreen6')

def build():

    layout = [
        [sg.Text('Equipo Nuevo',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text('Nombre', size=(15,1)), sg.Input(size=(30,1), key="-NOMBRE-")],
        [sg.Text('Domicilio', size=(15,1)), sg.Input(size=(30,1), key="-DOMICILIO-")],
        [sg.Text('Localidad', size=(15,1)), sg.Input(size=(30,1),key='-LOCALIDAD-')],
        [sg.Text('Teléfono', size=(15,1)), sg.Input(size=(30,1),key='-TELEFONO-')],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Ingresar equipo', layout=layout, font=(font_name,font_size), modal=True)
    
    return window