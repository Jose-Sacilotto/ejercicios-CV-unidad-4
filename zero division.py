try:
    preciototal=float(input("Ingresa el total de la cuenta: "))
    cantidadpersonas=int(input("Ingresa la cantidad de personas: "))
    if cantidadpersonas == 0:
        raise ValueError("Debe ingresar más de un integrate de grupo")
    preciopersonas=preciototal/cantidadpersonas
    print(F"${preciopersonas:.2f}")
except ValueError as e:
    print(e)
