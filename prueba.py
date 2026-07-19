import logging, traceback

logging.basicConfig(
    filename="app.log",                    # Guarda los logs en un archivo (opcional)
    level=logging.INFO,                    # Nivel mínimo que se mostrará
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del mensaje
    datefmt="%Y-%m-%d %H:%M:%S"            # Formato de la fecha/hora
)


logging.info("Inicio del proceso")
logging.warning("Archivo no encontrado, usando ruta alternativa")
logging.error("No se pudo conectar a la base de datos")


try:
    resultado = 10 / 0
except Exception as e:
    logging.error(f"Error detectado: {e}")
    traceback.print_exc()

