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
# EJECUCIÓN CONTROLADA DE CADA INCIDENCIA
# ------------------------------------------------------

def ejecutar_prueba(nombre, funcion):
    """
    Ejecuta una prueba de forma aislada.
    Si ocurre una excepción:
    - se muestra en consola,
    - se registra en app_errores.log,
    - se envía a Sentry,
    - y el programa continúa con la siguiente prueba.
    """
    logger.info("Inicio de prueba: %s", nombre)

    try:
        resultado = funcion()
        print(f"[OK] {nombre}: {resultado}")
        logger.info("Prueba completada correctamente: %s. Resultado: %s", nombre, resultado)

    except Exception as error:
        print(f"[ERROR] {nombre}: {type(error).__name__}: {error}")

        # Incluye automáticamente el traceback completo en el archivo .log.
        logger.exception("Error detectado en la prueba '%s'", nombre)

        # Envía la excepción con contexto a Sentry.
        with sentry_sdk.push_scope() as scope:
            scope.set_tag("taller", "gestion_incidencias")
            scope.set_tag("prueba", nombre)
            scope.set_context(
                "detalle_incidencia",
                {
                    "nombre": nombre,
                    "tipo_error": type(error).__name__,
                    "mensaje": str(error),
                },
            )
            sentry_sdk.capture_exception(error)

    finally:
        logger.info("Fin de prueba: %s", nombre)


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