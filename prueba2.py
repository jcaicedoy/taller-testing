import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def calcular_promedio(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        logging.error("Error: división para cero al calcular el promedio.")


datos = []  
promedio = calcular_promedio(datos)
print("Promedio:", promedio)
