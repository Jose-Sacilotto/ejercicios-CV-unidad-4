edad=int(input("Ingrese su edad: "))
tarifa=150
tarifa2=150/3
tarifa3=150/2
if edad <=4:
    print("Para menores de 4 años: $ 0")
elif edad >=5 and edad <=12:
    print(f"Para un menor: $ {tarifa2}")
elif edad >=13 and edad <=18:
    print(f"Para menores de 18: $ {tarifa3}")
elif edad >=19 and edad <=60:
    print(f"Para adultos: $ {tarifa}")
else:
    print(f"Para adultos mayores y jubilados: $ {tarifa3}")
