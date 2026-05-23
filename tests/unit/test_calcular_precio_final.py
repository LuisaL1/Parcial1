from src.libreria.calcular_precio_final import calcular_precio_final


def test_calcular_precio_final_correctamente():

    resultado = calcular_precio_final(1000, 20)

    assert resultado == 952


def test_calcular_precio_final_sin_descuento():

    resultado = calcular_precio_final(1000, 0)

    assert resultado == 1190


def test_precio_final_nunca_negativo():

    resultado = calcular_precio_final(1000, 40)

    assert resultado >= 0