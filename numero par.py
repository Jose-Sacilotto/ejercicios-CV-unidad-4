numero=int(input("Ingrese un número: "))
def es_par(numero):
    return numero%2==0
if es_par(numero):
    print(numero,"es par")
else:
    print(numero,"es impar")
