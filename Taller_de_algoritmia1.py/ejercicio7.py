#Eleccion de candidato y partido politico
input_candidato = input("¿Por que candidato quieres votar? (A, M o N): ")
 
if input_candidato == "A":
    print("has decicido votar por el candidato A , eres de derecha")
elif input_candidato == "M":
    print("has decicido votar por el candidato M , eres de izquierda")
    print("que viva petro")
elif input_candidato == "N":
    print("has decicido votar por el candidato N , eres de el frente de la guerilla")
    print("que viva el frente de la guerilla")
else:
    print("candidato no valido,voto en blanco registrado") 