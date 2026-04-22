import random

# 1) Elegir dificultad
def elegir_dificultad():
    print("Seleccione dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (7 intentos)")
    print("3. Difícil (5 intentos)")

    opcion = input("Opción: ")

    if opcion == "1":
        return 10
    elif opcion == "2":
        return 7
    elif opcion == "3":
        return 5
    else:
        print("Opción inválida, se asigna nivel Fácil")
        return 10

# 2) Generar número aleatorio
def generar_numero():
    return random.randint(1, 100)

# BONUS: guardar historial en archivo
def guardar_historial(resultado):
    with open("historial.txt", "a") as archivo:
        archivo.write(resultado + "\n")

# 3) Juego principal
def jugar(intentos):
    numero_secreto = generar_numero()
    historial = []

    print("\nAdivina el número entre 1 y 100")

    while intentos > 0:
        print(f"\nIntentos restantes: {intentos}")
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Correcto! Adivinaste el número")
            resultado = f"Ganó en {intentos} intentos restantes"
            historial.append(resultado)
            guardar_historial(resultado)
            return
        elif intento < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")

        intentos -= 1

    print(f"Perdiste. El número era: {numero_secreto}")
    resultado = f"Perdió. Número era {numero_secreto}"
    historial.append(resultado)
    guardar_historial(resultado)

# Programa principal
def main():
    intentos = elegir_dificultad()
    jugar(intentos)

if __name__ == "__main__":
    main()