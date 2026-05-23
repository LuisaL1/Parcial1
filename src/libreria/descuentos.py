def aplicar_descuento(precio, descuento):

    if descuento < 0 or descuento > 40:
        raise ValueError("Descuento inválido")

    return precio - (precio * descuento / 100)