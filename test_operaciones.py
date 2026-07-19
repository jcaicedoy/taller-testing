from operaciones import sumar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(10, 0) is None  # Verifica manejo del error


