montototal=float(input("Ingrese el monto total de la venta: "))
tipocliente=int(input("1- Estudiante\n 2- Docente\n 3- Otros\n N°: "))
if tipocliente == 1:
    resultado=(montototal*0.90)
    print("El importe es $",resultado," se le descuentan 10% del total. Debe pagar ",resultado)
elif tipocliente ==2:
    print("Se agregó ",montototal, "a su cuenta")
elif tipocliente ==3:
    print("Debe pagar ",montototal)
else:
    print("El número ingresado no corresponde a un tipo de cliente válido")