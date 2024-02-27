def lenp(frase):
    r = frase.split("")
    l = list(map(len, r))
    print("La lobgitud de cada paraula de la frase {} és {}.".format(frase,l))
    
#PPrincipal
frase = input("Escriu una frase: ")
lenp/frase
