import PySimpleGUI as sg

def build():
    """
    Construye la ventana de informacion "Acerca de"
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('SandyBeach')

    layout = [
            [sg.Image('src/resources/images/acercade.png', tooltip="Imagen sacada de internet")],
            [sg.Text('Aplicación pensada para llevar la información de los equipos y jugadores de un torneo.', font=('Bahnschrift SemiLight', 14), justification='center')],
            [sg.Text('La misma se encuentra en desarrollo, en las proximas versiones se podran editar los datos', font=('Bahnschrift SemiLight', 14), justification='center')],
            [sg.Text('y se agregaran funciones para incluir a los jugadores dentro de los equipos.', font=('Bahnschrift SemiLight', 14), justification='center')],
            [sg.Text(' -- Versión 1.0 -- ', font=('Helvetica', 12, 'bold'), justification='center')],
            [sg.Text(' -- Autor: jmvarela06@gmail.com -- ', font=('Helvetica', 12, 'bold'), justification="center")]
    ]

    window = sg.Window("Acerca de", layout=layout, modal=True)

    return window