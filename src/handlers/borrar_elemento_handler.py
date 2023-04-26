import json

def borrar_equipo(values):
    """
    Elimina el equipo seleccionado de la tabla en el archivo equipos.json
    """
    with open('files/equipos.json', 'r') as archivo:
        equipos = json.load(archivo)  # carga todos los equipos
    selected_row = values['-TABLA_EQUIPOS-'][0]
    del equipos[selected_row]
    with open('files/equipos.json', 'w') as archivo:
        json.dump(equipos, archivo, indent=4)

def borrar_jugador(values):
    """
    Elimina el jugador seleccionado de la tabla en el archivo jugadores.json
    """
    with open('files/jugadores.json', 'r') as archivo:
        jugadores = json.load(archivo)  # carga todos los jugadores
    selected_row = values['-TABLA_JUGADORES-'][0]
    del jugadores[selected_row]
    with open('files/jugadores.json', 'w') as archivo:
        json.dump(jugadores, archivo, indent=4)

def borrar_todo():
    """
    Elimina todos los datos de las tablas
    """
    with open('files/equipos.json', 'r') as archivo:
        equipos = json.load(archivo)  # carga todos los equipos
    with open('files/jugadores.json', 'r') as archivo:
        jugadores = json.load(archivo)  # carga todos los jugadores
    equipos.clear()
    jugadores.clear()
    with open('files/equipos.json', 'w') as archivo:
        json.dump(equipos, archivo, indent=4)
    with open('files/jugadores.json', 'w') as archivo:
        json.dump(jugadores, archivo, indent=4)

