import sentry_sdk

sentry_sdk.init(
    dsn="https://79011d01e0f3c658e4f0d4ac5172307b@o4510210301755392.ingest.us.sentry.io/4510210305949696",
    traces_sample_rate=1.0,
)

def procesar_datos(lista):
    total = 0
    for valor in lista:
        total += valor
    return total / len(lista)

datos = []
print(procesar_datos(datos))