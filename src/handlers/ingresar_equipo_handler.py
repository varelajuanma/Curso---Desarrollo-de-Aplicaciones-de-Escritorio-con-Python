import json

def agregar_equipo(datos_nuevos):
    """
    Guarda los datos de un nuevo jugador en el archivo de equipos.json
    """
    with open('files/equipos.json', 'r') as archivo:
        lista_equipos = json.load(archivo)  # carga todos los equipos
    # Obtener el último id, si no hay ningún equipo, el id es 1
    if not lista_equipos:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_equipos, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_equipos.append(datos_nuevos)
    with open('files/equipos.json', 'w') as archivo:
        json.dump(lista_equipos, archivo, indent=4)

def leer_archivo():
    """
    Lee todos los datos de equipos.json y los devuelve como una lista de diccionarios
    """
    with open('files/equipos.json', 'r') as file:  # r para leer
        datos = json.load(file)  # json.load(file) para leerlo como un diccionario
    # Convierte los datos a una lista de listas para que se pueda mostrar en la tabla
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([dato["-NOMBRE-"], dato["-DOMICILIO-"], dato["-LOCALIDAD-"], dato["-TELEFONO-"]])
    # Lo mismo pero escrito en una sola linea
    return datos_para_tabla