# serie-maclaurin-exponencial
# Serie de Maclaurin para la función exponencial e^x

Este proyecto implementa un método numérico para calcular el valor aproximado de e^x usando la serie de Maclaurin.

---

¿Qué es la serie de Maclaurin?

La serie de Maclaurin representa una función como la suma infinita de términos derivados evaluados en cero. En el caso de e^x, esta serie permite expresar la función como una suma de potencias de x multiplicadas por coeficientes relacionados con factoriales.

Todas las derivadas de e^x son iguales a la función misma, y evaluadas en cero, toman el valor 1. Por lo tanto, cada término de la serie es el recíproco del factorial del orden del término, multiplicado por x elevado a ese orden.

---

Cómo usar el programa

1. Ejecuta el archivo `maclaurin_exp.py`.
2. Ingresa el valor de x para el cual quieres calcular e^x.
3. Ingresa el valor de la tolerancia (error verdadero permitido), por ejemplo 0.0001.
4. Ingresa el valor real de e^x para que el programa calcule el error relativo verdadero.

El programa mostrará iteración por iteración el valor aproximado y los errores relativos hasta alcanzar la tolerancia especificada.

---

Código principal

El código está en `maclaurin.py`. Se basa en la fórmula:

e^x = suma infinita de (x^n / n!)

---

Autor
Alan Hiram Álvarez Bazán
GitHub: [https://github.com/Alanhiram75/Alanhiram75](https://github.com/Alanhiram75/Alanhiram75)

