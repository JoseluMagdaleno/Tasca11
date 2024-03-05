def div(a,b):
    try:
        c = a/b
        print("La divisió de {} entre {} és {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segón paràmetre no pot ser zero")

#Programa principal
a = int(input("Escriure el numerador: "))
b = int(input("Escriu el denominador: "))
div(a,b)
