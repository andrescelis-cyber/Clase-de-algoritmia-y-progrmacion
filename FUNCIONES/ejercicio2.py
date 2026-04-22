# taller_ejercicio2.py

# Operaciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

# Función principal de operación
def operacion(op, a, b):
    if op == "+":
        return suma(a, b)
    elif op == "-":
        return resta(a, b)
    elif op == "*":
        return multiplicacion(a, b)
    elif op == "/":
        return division(a, b)
    else:
        return "Operación no válida"

# Potencia usando multiplicación
def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado = multiplicacion(resultado, base)
    return resultado

# Raíz cuadrada (aproximada)
def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: número negativo"
    
    x = numero
    for _ in range(10):  # método iterativo (aproximación)
        x = (x + numero / x) / 2
    return x

# Factorial
def factorial(n):
    if n < 0:
        return "Error: no existe factorial de negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado = multiplicacion(resultado, i)
    return resultado

# Inversa
def inversa(numero):
    if numero == 0:
        return "Error: no existe inversa de 0"
    return 1 / numero

# Programa principal
def main():
    print("Calculadora Nivel 2")

    print("Suma:", suma(5, 3))
    print("Resta:", resta(5, 3))
    print("Multiplicación:", multiplicacion(5, 3))
    print("División:", division(5, 3))

    print("Potencia (2^3):", potencia(2, 3))
    print("Raíz cuadrada de 16:", raiz_cuadrada(16))

    print("Factorial de 5:", factorial(5))
    print("Inversa de 2:", inversa(2))

if __name__ == "__main__":
    main()