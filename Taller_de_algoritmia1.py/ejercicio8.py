# Moviemntos con dado
import random



input("Presiona Enter para lanzar el dado...")
print("Lanzando el dado...")
estado_dado = random.randint(1, 4)
print(f"El dado muestra: {estado_dado}")
 
int(input("¿Que numero de 1 al 6 muestra el dado? (1 para (mover una unidad hacia la derecha), 2 para (mover una unidad hacia abajo),3 para (mover una unidad hacia la izquierda),4 para (mover una unidad hacia arriba)"))
if estado_dado == 1:
    print("¡Movimiento hacia la derecha!")
elif estado_dado == 2:
    print("¡Movimiento hacia abajo!")   
elif estado_dado == 3:      
    print("¡Movimiento hacia la izquierda!")
elif estado_dado == 4:
    print("¡Movimiento hacia arriba!")
else:
    print("Número no válido. El dado solo muestra números del 1 al 4.")
    