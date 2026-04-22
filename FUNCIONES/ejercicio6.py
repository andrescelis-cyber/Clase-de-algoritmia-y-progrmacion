# taller_ejercicio6.py

# Diccionario de productos
productos = {
    "agua": 1500,
    "gaseosa": 2500,
    "papas": 2000,
    "chocolate": 3000,
    "galletas": 1800
}

# Mostrar productos
def mostrar_productos(diccionario):
    print("\nProductos disponibles:")
    for nombre, precio in diccionario.items():
        print(f"{nombre} -> ${precio}")

# BONUS: verificar dinero insuficiente
def verificar_pago(precio, dinero):
    if dinero < precio:
        return False
    return True

# Proceso de compra
def comprar_producto(diccionario):
    mostrar_productos(diccionario)

    producto = input("\nSeleccione un producto: ").lower()

    if producto not in diccionario:
        print("Producto no disponible.")
        return

    precio = diccionario[producto]
    print(f"El precio de {producto} es: ${precio}")

    dinero = int(input("Ingrese el dinero: "))

    # BONUS
    if not verificar_pago(precio, dinero):
        print("Dinero insuficiente. No se puede realizar la compra.")
        return

    cambio = dinero - precio

    print(f"\nProducto entregado: {producto}")

    if cambio > 0:
        print(f"Su cambio es: ${cambio}")
    else:
        print("No hay cambio.")

# Programa principal
def main():
    while True:
        print("\n--- MÁQUINA DISPENSADORA ---")
        print("1. Comprar producto")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            comprar_producto(productos)
        elif opcion == "2":
            print("Gracias por usar la máquina.")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()