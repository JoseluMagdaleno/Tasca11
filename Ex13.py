class Animal():
    def _init_(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        pass
    def mourem():
        pass
    def quisoc():
        print("Soc un animal: ")

class Cavall(Animal):
    def xerrar(self):
        print("Iíííiíííííií")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un cavall")
class Dofi(Animal):
    def xerrar(self):
        print("IchIchIchIch")
    def mourem(self):
        print("Em moc nadant")
    def quisoc(self):
        print("Soc un dofí")
class Abella(Animal):
    def xerrar(self):
        print("ZZZZZZ")
    def moure(self):
        print("Em moc volant")
    def quisoc(self):
        print("Soc una abella")
class Centaure(Humà, Cavall):
    def xerrar(self):
        print("Hola, nosaltres utilitzem un idioma per xerrar")
    def moure(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un centaure")
class Humà(Animal):
    def xerrar(self):
        print("Hola")
    def moure(self):
        print("Em moc caminant")
    def quisoc(self):
        print("Soc una persona")
class Fiet(Humà):
    def xerrar():
        print("UEE")
    def moure():
        print("Em moc gatejant")
    def quisoc():
        print("Soc un bebé")
class Xou():
    def xerrar(self):
        print("Xou")
    def moure(self):
        print("Em moc fent xou")
    def quisoc(self):
        print("Soc un xou")

#Programa principal
    
a = [Cavall("Marró", "4"), Dofi("Gris", "10"), Abella("Groga i negra", "0,5"), Centaure("Fiona", "Marrón", "18",), Humà("Sibila", "cristià", "7"), Fiet("Jordi", "Moreno", "9"), Xou()]
