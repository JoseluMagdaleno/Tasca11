import os

companys=["Jordi", "Claudia","Ian", "Joan", "Marc", "Hugo", "Josep", "Fede", "José Luis", "Leiner", "David", "Ayoub", "Óscar", "Paula", "Sebas", "Anas", "Sergi", "Álvaro", "Clara"]
os.mkdir("/home/cicles/AO/Tasca10/Tasca11/Prova")
os.chdir("/home/cicles/AO/Tasca10/Tasca11/Prova")
with fopen("ex12.txt", "w") as f:
    print("El fitxer s'ha creat correctament!")
    for e in companys:
        f.write(e+"\n")
professors=["David", "Pep", "Fela", "Lluís", "Joan"]
with open("ex12.txt", "a+") as f:
    for e in professors:
        f.write(e+"\n")
a = []
with open("ex12.txt", "r") as f:
    for e in professors:
        c = e.split("\n")
        a.append(c[0])
print(a)
