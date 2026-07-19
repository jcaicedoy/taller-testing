"""
Versión de demostración con errores controlados.

Objetivo:
- Ejecutar los cuatro casos problemáticos del taller.
- Registrar cada error localmente en app_errores.log.
- Enviar cada excepción a Sentry.
- Permitir que el programa continúe para evidenciar todos los errores.
"""

import logging
import sentry_sdk


# ------------------------------------------------------
# CONFIGURACIÓN DE SENTRY
# ------------------------------------------------------

sentry_sdk.init(
    dsn="https://77dbf056128bb50f0e3ed444d42449d4@o4511756724928512.ingest.us.sentry.io/4511756732661760",
    traces_sample_rate=1.0,
)


# ------------------------------------------------------
# CONFIGURACIÓN DE LOGS LOCALES
# ------------------------------------------------------

logging.basicConfig(
    filename="app_errores.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


# ------------------------------------------------------
# FUNCIONES ORIGINALES CON ERRORES POTENCIALES
# ------------------------------------------------------

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
    logger.info("========== INICIO DEL PROGRAMA CON ERRORES ==========")
    print("Ejecutando casos con errores para demostración...\n")

    ejecutar_prueba(
        "Incidencia 1 - División por cero",
        lambda: dividir(10, 0),
    )

    ejecutar_prueba(
        "Incidencia 2 - Promedio de lista vacía",
        lambda: promedio([]),
    )

    ejecutar_prueba(
        "Incidencia 3 - Índice fuera de rango",
        lambda: obtener_elemento([1, 2, 3], 5),
    )

    ejecutar_prueba(
        "Incidencia 4 - Tipo de dato inválido en precios",
        lambda: calcular_total([10, 20, "treinta", 40]),
    )

    print("\nEjecución finalizada.")
    print("Revise el archivo app_errores.log y el panel de Sentry.")

    logger.info("========== FIN DEL PROGRAMA CON ERRORES ==========")

    # Fuerza el envío de eventos pendientes antes de cerrar el proceso.
    sentry_sdk.flush(timeout=5)


if __name__ == "__main__":
    main()