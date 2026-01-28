def registros_operaciones(lista_registros):

    """Analiza una lista de registros operativos y devuelve un resumen
    de la cantidad total de incidentes por área.

    Solo se consideran los registros:
    - con estado "valido"
    - con incidentes mayores a cero

    Parámetros:
    lista_registros: lista de diccionarios con las claves 'area', 'incidentes' y 'estado'

    Retorna:
    dict: resumen de incidentes acumulados por área"""

    if not lista_registros:
        return {} #retorno dict vacío porque mantiene el tipo de retorno

    resumen = {}

    for r in lista_registros:

        # validación de claves obligatorias: 
        # Si falta alguna → se ignora ese registro, no se rompe la función.
        if "area" not in r or "incidentes" not in r or "estado" not in r:
            continue


        if r["incidentes"] > 0 and r["estado"] == "valido":

            area = r["area"]
            incidentes = r["incidentes"]


            if area not in resumen:
                resumen[area] = incidentes

            else:
                resumen[area] += incidentes
    
    return resumen


#Estructura de los datos
registros = [
    {"area": "Soporte", "incidentes": 3, "estado": "valido"},
    {"area": "IT", "incidentes": 0, "estado": "valido"},
    {"area": "Soporte", "incidentes": 2, "estado": "valido"},
    {"area": "RRHH", "incidentes": 1, "estado": "invalido"},
    {"area": "IT", "incidentes": 4, "estado": "valido"},
]

resumen_final = registros_operaciones(registros)
print(resumen_final)


