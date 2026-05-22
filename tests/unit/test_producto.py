from src.libreria.producto import Producto
import pytest


def test_crear_producto_con_precio_valido():
    producto = Producto("Libro", 1000)
    assert producto.precio_base == 1000


def test_no_permitir_precio_cero():
    with pytest.raises(ValueError):
        Producto("Libro", 0)


def test_no_permitir_precio_negativo():
    with pytest.raises(ValueError):
        Producto("Libro", -100)