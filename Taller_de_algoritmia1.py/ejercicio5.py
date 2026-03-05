# Secuencia de luces de un semáforo

estado_semaforo = int(input("¿Qué luz del semáforo quieres ver? (1 para rojo, 2 para amarillo, 3 para verde): "))

if estado_semaforo == 1:
    print("Luz roja")
    print("¡Alto! Detén tu vehículo")
elif estado_semaforo == 2:
    print("Luz amarilla")
    print("Prepárate para avanzar")
elif estado_semaforo == 3:
    print("Luz verde")
    print("¡Adelante! Puedes avanzar")
else:
    print("Número inválido. Ingresa 1, 2 o 3")

