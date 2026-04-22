# taller_ejercicio4.py

notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Draco": [4.5, 4.2, 5.0],
    "Neville": [2.5, 3.0, 3.2]
}

# 1) Promedio simple
def promedio_simple(lista):
    return sum(lista) / len(lista)

# 2) Promedio ponderado (30%, 30%, 40%)
def promedio_ponderado(lista):
    return lista[0]*0.3 + lista[1]*0.3 + lista[2]*0.4

# 3) Estudiante con mayor promedio
def mejor_estudiante(diccionario):
    mejor = None
    mejor_prom = -1

    for nombre in diccionario:
        prom = promedio_ponderado(diccionario[nombre])
        if prom > mejor_prom:
            mejor_prom = prom
            mejor = nombre

    return mejor, mejor_prom

# 4) Mostrar aprobados
def estudiantes_aprobados(diccionario):
    aprobados = []
    for nombre in diccionario:
        prom = promedio_ponderado(diccionario[nombre])
        if prom >= 3.0:
            aprobados.append(nombre)
    return aprobados

# BONUS: Mensaje de aprobación
def estado_estudiantes(diccionario):
    for nombre in diccionario:
        prom = promedio_ponderado(diccionario[nombre])
        if prom >= 3.0:
            print(f"{nombre} aprobó la clase de McGonagall con {round(prom,2)}")
        else:
            print(f"{nombre} no aprobó la clase de McGonagall con {round(prom,2)}")

# Programa principal
def main():
    print("Promedios simples:")
    for nombre in notas:
        print(nombre, ":", round(promedio_simple(notas[nombre]), 2))

    print("\nPromedios ponderados:")
    for nombre in notas:
        print(nombre, ":", round(promedio_ponderado(notas[nombre]), 2))

    mejor, prom = mejor_estudiante(notas)
    print(f"\nMejor estudiante: {mejor} con promedio {round(prom,2)}")

    print("\nEstudiantes aprobados:")
    print(estudiantes_aprobados(notas))

    print("\nEstado final:")
    estado_estudiantes(notas)

if __name__ == "__main__":
    main()