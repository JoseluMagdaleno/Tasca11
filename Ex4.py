#Ex4. Tasca11
def adjuntar(l,d,c):
    a = []
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
    print("La unió de les llistes {} i {} és {}".format(l,d,a))
#Propgrama principal. Ex4. Tasca 11
l=["Super", "Hiper", "Mini", "Maxi"]
d=["Women", "Bole", "Mouse", "Boom"]
adjuntar(l,d," ")
#ProgramaPrincipal