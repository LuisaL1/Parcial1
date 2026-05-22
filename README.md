# Librería Parcial

Proyecto del examen parcial de Pruebas de Software.

---

# Tecnologías

- Python
- Pytest
- Pytest-Cov
- Behave / Pytest-BDD

---

# Estructura del proyecto

```text
libreria-parcial-tunombre/
│
├── src/
├── tests/
├── features/
├── README.md
├── TEORIA.md
└── requirements.txt
```

---

# Parte 1 — Análisis

## Regla 1 — Precio base

### Particiones de equivalencia

| Partición | Tipo | Valor | Resultado esperado |
|---|---|---|---|
| Precio > 0 | Válida | 1000 | Producto creado |
| Precio = 0 | Inválida | 0 | Error |
| Precio < 0 | Inválida | -50 | Error |

---

## Regla 2 — Descuento

### Particiones de equivalencia

| Partición | Tipo | Valor | Resultado esperado |
|---|---|---|---|
| 0% a 40% | Válida | 20% | Descuento válido |
| 0% | Válida | 0% | Descuento válido |
| 40% | Válida | 40% | Descuento válido |
| Mayor a 40% | Inválida | 41% | Error |
| Menor a 0% | Inválida | -1% | Error |

---

## Valores límite — Regla 2

| Valor | Resultado esperado |
|---|---|
| -1% | Inválido |
| 0% | Válido |
| 40% | Válido |
| 41% | Inválido |

---

## Regla 3 — Pregunta al administrador

### Pregunta
¿El precio final debe redondearse?

### Justificación
El redondeo puede cambiar el resultado esperado de las pruebas.

---

# Parte 2 — Casos de prueba

| ID | Regla | Descripción | Datos de entrada | Resultado esperado | Tipo |
|---|---|---|---|---|---|
| CP-01 | 1 | Crear producto válido | Precio = 1000 | Producto creado | Positivo |
| CP-02 | 1 | Precio igual a cero | Precio = 0 | Error | Negativo |
| CP-03 | 1 | Precio negativo | Precio = -100 | Error | Negativo |
| CP-04 | 2 | Descuento válido | 20% | Descuento aplicado | Positivo |
| CP-05 | 2 | Descuento límite válido | 40% | Descuento aplicado | Borde |
| CP-06 | 2 | Descuento inválido | 41% | Error | Negativo |
| CP-07 | 3 | Calcular precio final | 1000 y 20% | Precio final correcto | Positivo |
| CP-08 | 3 | Precio final con límite | 5000 y 40% | Precio válido | Borde |

---

# Cobertura

```bash
pytest --cov=src
```