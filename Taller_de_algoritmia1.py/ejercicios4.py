# Simulación de tanque con válvula
estado_tanque = int(input("¿El tanque está lleno? (1 para sí, 0 para no): "))

if estado_tanque == 1:
    print("Tanque lleno detectado")
    print("Cerrando válvula")
elif estado_tanque == 0:
    print("Tanque vacío detectado")
    print("Abriendo válvula...")
else:
    print("Estado inválido. Ingresa 1 o 0.")
    
