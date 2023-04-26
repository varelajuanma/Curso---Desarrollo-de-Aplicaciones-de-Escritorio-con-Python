import json


def agregar_jugador(datos_nuevos):
    """
    Guarda los datos de un nuevo jugador en el archivo de jugadores.json
    """
    with open('files/jugadores.json', 'r') as archivo:
        lista_jugadores = json.load(archivo)  # carga todos los jugadores
    # Obtener el último id, si no hay ningún expediente, el id es 1
    if not lista_jugadores:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_jugadores, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_jugadores.append(datos_nuevos)
    with open('files/jugadores.json', 'w') as archivo:
        json.dump(lista_jugadores, archivo, indent=4)

def leer_archivo():
    """
    Lee todos los datos de jugadores.json y los devuelve como una lista de diccionarios
    """
    with open('files/jugadores.json', 'r') as file:  # r para leer
        datos = json.load(file)  # json.load(file) para leerlo como un diccionario
    # Convierte los datos a una lista de listas para que se pueda mostrar en la tabla
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([dato["-CLUB-"], dato["-NRO_CAMISETA-"], dato["-NOMBRE_Y_APELLIDO-"], dato["-EDAD-"], dato["-DNI-"], dato["-ALTURA-"], dato["-TELEFONO-"]])
    # Lo mismo pero escrito en una sola linea
    return datos_para_tabla