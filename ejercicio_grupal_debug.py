"""
Versión corregida del ejercicio grupal.

Objetivo:
- Corregir las cuatro incidencias detectadas.
- Registrar localmente las decisiones y validaciones en app_corregido.log.
- Mantener Sentry inicializado para capturar cualquier error inesperado.
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
    filename="app_corregido.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


# ------------------------------------------------------
# FUNCIONES CORREGIDAS
# ------------------------------------------------------

def dividir(a, b):
    """Devuelve la división de dos números, validando división por cero."""
    logger.info("Solicitud de división: a=%s, b=%s", a, b)

    if b == 0:
        logger.warning("División rechazada: el divisor no puede ser cero.")
        return None

    resultado = a / b
    logger.info("División realizada correctamente. Resultado=%s", resultado)
    return resultado


def promedio(lista_numeros):
    """Calcula el promedio y valida que la lista no esté vacía."""
    logger.info("Solicitud de promedio. Cantidad de elementos=%s", len(lista_numeros))

    if not lista_numeros:
        logger.warning("No se puede calcular el promedio de una lista vacía.")
        return None

    total = 0
    for n in lista_numeros:
        total += n

    resultado = total / len(lista_numeros)
    logger.info("Promedio calculado correctamente. Resultado=%s", resultado)
    return resultado


def obtener_elemento(lista, indice):
    """Devuelve un elemento validando que el índice exista."""
    logger.info(
        "Solicitud de elemento. Índice=%s, tamaño_lista=%s",
        indice,
        len(lista),
    )

    if indice < 0 or indice >= len(lista):
        logger.warning(
            "Índice fuera de rango. Índice solicitado=%s, tamaño_lista=%s",
            indice,
            len(lista),
        )
        return None

    elemento = lista[indice]
    logger.info("Elemento obtenido correctamente. Resultado=%s", elemento)
    return elemento


def calcular_total(precios):
    """Suma solo valores numéricos de una lista de precios."""
    logger.info("Inicio del cálculo total. Elementos=%s", precios)

    total = 0

    for precio in precios:
        if not isinstance(precio, (int, float)):
            logger.warning(
                "Valor no numérico ignorado durante el cálculo: %r",
                precio,
            )
            continue

        total += precio

    logger.info("Total calculado correctamente. Resultado=%s", total)
    return total


# ------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------

def main():
    logger.info("========== INICIO DEL PROGRAMA CORREGIDO ==========")
    print("Ejecutando versión corregida...\n")

    try:
        resultado_div = dividir(10, 0)
        if resultado_div is None:
            print("División: operación no realizada porque el divisor es cero.")
        else:
            print("Resultado de la división:", resultado_div)

        datos = []
        resultado_promedio = promedio(datos)
        if resultado_promedio is None:
            print("Promedio: no se puede calcular con una lista vacía.")
        else:
            print("Promedio:", resultado_promedio)

        lista = [1, 2, 3]
        elemento = obtener_elemento(lista, 5)
        if elemento is None:
            print("Elemento: el índice solicitado está fuera de rango.")
        else:
            print("Elemento:", elemento)

        precios = [10, 20, 20, 40]
        total = calcular_total(precios)
        print("Total de precios válidos:", total)

        logger.info("Programa corregido ejecutado sin excepciones no controladas.")

    except Exception as error:
        # Este bloque solo captura errores inesperados después de las correcciones.
        logger.exception("Error inesperado en la versión corregida.")

        with sentry_sdk.push_scope() as scope:
            scope.set_tag("taller", "gestion_incidencias")
            scope.set_tag("version", "corregida")
            sentry_sdk.capture_exception(error)

        print(f"Se produjo un error inesperado: {type(error).__name__}: {error}")

    finally:
        logger.info("========== FIN DEL PROGRAMA CORREGIDO ==========")
        sentry_sdk.flush(timeout=5)


if __name__ == "__main__":
    main()