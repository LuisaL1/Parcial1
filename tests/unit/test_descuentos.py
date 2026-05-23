from src.libreria.descuentos import aplicar_descuento
import pytest


def test_aplicar_descuento_valido():

    resultado = aplicar_descuento(1000, 20)

    assert resultado == 800


def test_aplicar_descuento_cero():

    resultado = aplicar_descuento(1000, 0)

    assert resultado == 1000


def test_aplicar_descuento_maximo():

    resultado = aplicar_descuento(1000, 40)

    assert resultado == 600


def test_no_permitir_descuento_mayor_a_40():

    with pytest.raises(ValueError):
        aplicar_descuento(1000, 41)


def test_no_permitir_descuento_negativo():

    with pytest.raises(ValueError):
        aplicar_descuento(1000, -1)