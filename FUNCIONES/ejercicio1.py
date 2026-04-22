# taller_ejercicio1.py

# Lista de temperaturas (24 valores, uno por cada hora)
temperaturas = [
    18, 17, 16, 16, 15, 15, 16, 18,
    20, 22, 24, 26, 28, 29, 30, 29,
    27, 25, 23, 22, 21, 20, 19, 18
]

# Función para calcular el promedio
def promedio(lista):
    return sum(lista) / len(lista)

# Función para obtener la temperatura máxima y mínima
def extremos(lista):
    return max(lista), min(lista)

# Función para contar cuántas temperaturas están sobre el promedio
def dias_sobre_promedio(lista):
    prom = promedio(lista)
    contador = 0
    for temp in lista:
        if temp > prom:
            contador += 1
    return contador

# Programa principal
def main():
    prom = promedio(temperaturas)
    maxima, minima = extremos(temperaturas)
    sobre_prom = dias_sobre_promedio(temperaturas)

    print("Temperaturas del día:", temperaturas)
    print("Temperatura promedio:", round(prom, 2), "°C")
    print("Temperatura máxima:", maxima, "°C")
    print("Temperatura mínima:", minima, "°C")
    print("Cantidad de horas sobre el promedio:", sobre_prom)

# Ejecutar el programa
if __name__ == "__main__":
    main()