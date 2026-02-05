# Proyecto1 – Resumen de Incidentes Operativos

Este proyecto está desarrollado en Python y permite **analizar una lista de registros operativos** y devolver un resumen de la **cantidad total de incidentes por área**.

## Funcionalidad principal

- Solo se consideran los registros:
  - Con estado "valido"
  - Con incidentes mayores a cero

- Parámetros de entrada:
  - "lista_registro". lista de diccionarios con las claves:
    - "area"
    - "incidentes"
    - "estado"

- Retorna:
  - Un diccionario (dict) con el **resumen de incidentes acumulados por área**.

## Ejemplo de uso

```python
# Crear un archivo nuevo en la misma carpeta, por ejemplo test.py

from mini_proyecto import registros_operaciones

registros = [
    {"area": "Soporte", "incidentes": 3, "estado": "valido"},
    {"area": "IT", "incidentes": 0, "estado": "valido"},
    {"area": "Soporte", "incidentes": 2, "estado": "valido"},
    {"area": "RRHH", "incidentes": 1, "estado": "invalido"},
    {"area": "IT", "incidentes": 4, "estado": "valido"},
]

resumen_final = registros_operaciones(registros)
print(resumen_final)  # Salida esperada: {'Soporte': 5, 'IT': 4}

```

Este proyecto es parte de prácticas de Python orientadas a backend