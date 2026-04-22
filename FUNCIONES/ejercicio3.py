# taller_ejercicio3.py

# Diccionario inicial (puede empezar vacío)
inventario = {}

# 1) Agregar producto
def agregar_producto(diccionario, nombre, cantidad, precio):
    diccionario[nombre] = {
        "cantidad": cantidad,
        "precio": precio
    }

# 2) Eliminar producto
def eliminar_producto(diccionario, nombre):
    if nombre in diccionario:
        del diccionario[nombre]
    else:
        print("El producto no existe.")

# 3) Calcular valor total
def calcular_valor_total(diccionario):
    total = 0
    for producto in diccionario:
        cantidad = diccionario[producto]["cantidad"]
        precio = diccionario[producto]["precio"]
        total += cantidad * precio
    return total

# 4) Mostrar inventario
def mostrar_inventario(diccionario):
    if not diccionario:
        print("Inventario vacío.")
    else:
        print("\nInventario:")
        for producto in diccionario:
            datos = diccionario[producto]
            print(f"{producto} -> Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

# Programa principal con menú
def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Calcular valor total")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario, nombre, cantidad, precio)

        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "3":
            mostrar_inventario(inventario)

        elif opcion == "4":
            total = calcular_valor_total(inventario)
            print("Valor total del inventario:", total)

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

# Ejecutar programa
if __name__ == "__main__":
    main()