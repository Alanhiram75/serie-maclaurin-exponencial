# Serie de Maclaurin para la función exponencial eˣ

Este proyecto implementa un método numérico para calcular el valor aproximado de `e^x` usando la serie de Maclaurin.

---

## ¿Qué es la serie de Maclaurin?

La serie de Maclaurin representa una función como la suma infinita de términos derivados evaluados en cero. En el caso de `e^x`, esta serie permite expresar la función como una suma de potencias de `x` multiplicadas por coeficientes relacionados con factoriales.

---

## Cómo usar este archivo en otro proyecto

Puedes reutilizar el método definido en `maclaurin.py` desde otro archivo Python.

### 1. Importar el método

Primero, asegúrate de tener el archivo [`maclaurin.py`](https://github.com/Alanhiram75/serie-maclaurin-exponencial/blob/main/maclaurin.py) en la misma carpeta que tu archivo principal.

Luego, en tu script principal, importa el método con la siguiente línea:

```python
from maclaurin import calcular_exponencial_maclaurin
```

### 2. Llamar al método

Una vez importado, puedes llamarlo así en cualquier parte de tu código:

```python
calcular_exponencial_maclaurin()
```

---

## Archivo principal

* [`maclaurin.py`](https://github.com/Alanhiram75/serie-maclaurin-exponencial/blob/main/maclaurin.py)

---

## Autor

Alan Hiram Álvarez Bazán
GitHub: [https://github.com/Alanhiram75/Alanhiram75](https://github.com/Alanhiram75/Alanhiram75)
