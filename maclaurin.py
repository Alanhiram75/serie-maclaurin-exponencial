import math

def calcular_exponencial_maclaurin():
    while True:
        try:
            x = float(input("Ingresa el valor de x: "))
            break
        except ValueError:
            print("⚠️ Error: Debes ingresar un número válido para x.")

    while True:
        try:
            tolerancia_error = float(input("Ingresa la tolerancia del Error Verdadero en % (ejemplo 1 para 1%): "))
            if tolerancia_error <= 0:
                print("⚠️ La tolerancia debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("⚠️ Error: Debes ingresar un número válido para la tolerancia.")

    while True:
        try:
            valor_real = float(input("Ingresa el valor de e^x (valor real): "))
            break
        except ValueError:
            print("⚠️ Error: Debes ingresar un número válido para el valor real.")

    iteracion = 0
    aproximacion_actual = 0
    aproximacion_anterior = 0
    condicion = False

    print("\n=== CÁLCULO DE e^x MEDIANTE SERIE DE MACLAURIN ===\n")

    while not condicion:
        resultado_iteracion = (x**iteracion) / math.factorial(iteracion)
        aproximacion_actual += resultado_iteracion

        # Error verdadero en porcentaje
        error_verdadero = abs((valor_real - aproximacion_actual) / valor_real) * 100

        print(f"\nIteración {iteracion + 1}")
        print(f"{'Resultado de iteración:':28s} {resultado_iteracion:>12.6f}")
        print(f"{'Aproximación actual:':28s} {aproximacion_actual:>12.6f}")
        print(f"{'Valor real:':28s} {valor_real:>12.6f}")
        print(f"{'Error relativo verdadero:':28s} {error_verdadero:>12.4f}%   (Tolerancia: {tolerancia_error:.4f}%)")

        if iteracion >= 1:
            diferencia = abs(aproximacion_actual - aproximacion_anterior)
            error_aproximado = diferencia / aproximacion_actual
            print(f"{'Error relativo aproximado:':28s} {error_aproximado:>12.6f}")

        print("-" * 60)

        aproximacion_anterior = aproximacion_actual

        # ✅ Ahora ya comparamos en porcentaje directo
        if error_verdadero <= tolerancia_error:
            condicion = True
        else:
            iteracion += 1

    print("\n=== RESULTADO FINAL ===")
    print(f"Valor aproximado de e^{x} = {aproximacion_actual:.6f}")
    print(f"Total de iteraciones realizadas: {iteracion + 1}")


calcular_exponencial_maclaurin()
