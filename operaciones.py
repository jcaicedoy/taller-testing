import logging

# Configuración del log
logging.basicConfig(
    level=logging.INFO,                    # Nivel de detalle mínimo
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def sumar(a, b):
    resultado = a + b
    logging.info(f"Suma realizada: {a} + {b} = {resultado}")
    return resultado

def dividir(a, b):
    try:
        resultado = a / b
        logging.info(f"División realizada: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        logging.error(f"Error de división: {e}")
        return None
    
print(sumar(5, 3))
print(dividir(10, 2))