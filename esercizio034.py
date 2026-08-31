#esempio di polimorfismo
""" class Forma:
    def area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza=larghezza
        self.altezza=altezza

    def area(self):
        return self.larghezza * self.altezza

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14 * (self.raggio **2) """

# Esercizio 34: Polimorfismo con classi.
#Crea una classe Animale con un metodo suono.
# Crea le sottoclassi Cane e Gatto che ridefiniscono il metodo suono 
#                     per stampare rispettivamente "Woof" e "Meow".
# Crea una istanza di entrambe le classi e chiama il metodo suono.

class Animale:
    def suono(self):
        pass

class Cane(Animale):
    def suono(self):
        return "Woof"   

class Gatto(Animale):
    def suono(self):
        return "Meow"

cane = Cane()
gatto = Gatto()
print("il verso del cane è: " + cane.suono())
print("il verso del gatto è: " + gatto.suono())

