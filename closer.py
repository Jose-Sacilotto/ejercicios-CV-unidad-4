numero1=int(input("Ingrese el número principal: "))
numero2=int(input("Jugador 1 ingrese su número: "))
numero3=int(input("Jugador 2 ingrese su número: "))
diferencia1=abs(numero1-numero2)
diferencia2=abs(numero1-numero3)
if diferencia1<diferencia2:
    print("Ganador jugador 1")
elif diferencia2<diferencia1:
    print("Ganador jugador 2")
else:
    print("Empate")
