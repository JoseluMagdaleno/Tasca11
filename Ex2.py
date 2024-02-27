from  functools import reduce
def Passar_a_numero(llista):
    a = list(map(lambda x: str(x), llista))
    b = reduce(lambda x,y : x+y , a)
print("La llista {} és el número {}".format(llista, b))

#PPrincipal
l = [3, 5, 7, 8, 1]
Passar_a_numero(l)
