def procesar_datos(lista):
    total = 0
    for valor in lista:
        total += valor
    return total / len(lista)

datos = [10, 20, "30", 40]
print(procesar_datos(datos))

# Ejecutar y leer el mensaje de error.

# Usar try/except para capturar excepciones.

# Agregar logging para identificar el valor que falla.










def calcular_promedio(lista):
    try:
        return sum(lista) / len(lista)  # promedio
    except ZeroDivisionError as e:
        logging.error(
            "Error al calcular el promedio: la lista está vacía. Detalle: %s", e
        )
        return None
    except Exception as e:
        logging.error(
            "Error inesperado al calcular el promedio: %s", e
        )
        return None
