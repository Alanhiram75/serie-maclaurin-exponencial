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
            tolerancia_error = float(input("Ingresa el valor del Error Verdadero (tolerancia, por ejemplo 0.0001): "))
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
        error_verdadero = abs((valor_real - aproximacion_actual) / valor_real)

        print(f"Iteración {iteracion + 1}")
        print(f"  Resultado de iteración: {resultado_iteracion:.6f}")
        print(f"  Aproximación actual: {aproximacion_actual:.6f}   Valor real: {valor_real}")
        print(f"  Error relativo verdadero: {error_verdadero:.6f}  (Tolerancia: {tolerancia_error})")

        if iteracion >= 1:
            diferencia = abs(aproximacion_actual - aproximacion_anterior)
            error_aproximado = diferencia / aproximacion_actual
            print(f"  Error relativo aproximado: |{aproximacion_actual:.6f} - {aproximacion_anterior:.6f}| / {aproximacion_actual:.6f} = {error_aproximado:.6f}")
        
        print("-" * 60)

        aproximacion_anterior = aproximacion_actual

        if round(error_verdadero, 2) <= round(tolerancia_error, 2) and round(aproximacion_actual, 2) >= round(valor_real, 2):
            condicion = True
        else:
            iteracion += 1

    print("\n=== RESULTADO FINAL ===")
    print(f"Valor aproximado de e^{x} = {aproximacion_actual:.6f}")
    print(f"Total de iteraciones realizadas: {iteracion + 1}")


calcular_exponencial_maclaurin()
