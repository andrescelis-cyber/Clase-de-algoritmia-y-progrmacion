#Calculadora de operaciones basicas
X = float(input("Ingresa el valor de X: "))
Y = float(input("Ingresa el valor de Y: "))

print("Selecciona una operacion:")
print("s = suma")
print("r = resta")
print("m = multiplicacion")
print("d = division")

operacion = input("Elige una opcion: ")

if operacion == "s":
    print("Resultado:", X + Y)

elif operacion == "r":
    print("Resultado:", X - Y)

elif operacion == "m":
    print("Resultado:", X * Y)

elif operacion == "d":
    print("Resultado:", X / Y)

else:
    print("Operacion no valida")