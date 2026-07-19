"""
Este programa contiene errores simples de lógica y ejecución.
El objetivo es detectar, registrar, corregir y documentar cada incidencia.
"""

import logging

def dividir(a, b):
    """Devuelve la división de dos números."""
    return a / b  

def promedio(lista_numeros):
    """Calcula el promedio de una lista de números."""
    total = 0
    for n in lista_numeros:
        total += n
    return total / len(lista_numeros)  

def obtener_elemento(lista, indice):
    """Devuelve un elemento de la lista según el índice indicado."""
    return lista[indice] 

def calcular_total(precios):
    """Suma los precios de una lista."""
    total = 0
    for p in precios:
        total += p
    return total  

# ------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------

def main():
    logging.info("Inicio del programa")

    resultado_div = dividir(10, 0)
    print("Resultado de la división:", resultado_div)

    datos = []
    print("Promedio:", promedio(datos))

    lista = [1, 2, 3]
    print("Elemento:", obtener_elemento(lista, 5))

    
    precios = [10, 20, "treinta", 40]
    print("Total de precios:", calcular_total(precios))

    logging.info("Fin del programa")

if __name__ == "__main__":
    main()
