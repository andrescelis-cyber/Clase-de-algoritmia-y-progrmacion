hora = int(input("¿Qué hora es? "))

if hora == 6:                    
    print("¡Alarma! suena durante 1 minuto (o hasta apagarla)")
    apagar = input("El usuario ya apagó la alarma?  ")
    if apagar == "si": 
        print("alarma apagada")
        print("Esperando a las 6 A.M de nuevo...")
    elif apagar == "no":
        print("la alarma sigue sonando")
elif hora < 6:
    print("Aùn no suena alarma")
    print("Esperando a las 6 A.M...")
elif hora > 6:
    print("Aùn no suena alarma")
    print("Esperando a las 6 A.M...")