class Atleta:
    def __init__(self,aposentado,peso):
        self.aposentado = aposentado
        self.peso = peso
    def Aposentar(self):
        if self.aposentado == True:
            print("O atleta já está aposentado! Não pode aposentar novamente!")
        else:
            print("O atleta se aposentou!")
    def Aquecer(self):
        if self.aposentado == True:
            print("O atleta não pode se aquecer, pois está aposentado!")
        else:
            print("O atleta está aquecendo!")

class Corredor(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)
    def Correr(self):
        if self.aposentado == True:
            print("O Corredor não pode correr, pois está aposentado")
        else:
            print("O Corredor começou a correr!")
class Nadador(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)
    def Nadar(self):
        if self.aposentado == True:
            print("O Nadador não pode nadar, pois está aposentado!")
        else:
            print("O Nadador começou a nadar!")
class Ciclista(Atleta):
    def __init__(self,aposentado,peso):
        super().__init__(aposentado,peso)
    def Pedalar(self):
        if self.aposentado == True:
            print("O Ciclista não pode pedalar, pois está aposentado!")
        else:
            print("O Ciclista começou a pedalar!")

class Triatleta(Corredor,Nadador,Ciclista):
    def __init__ (self, aposentado,peso):
        super().__init__(aposentado,peso)

triatleta1 = Triatleta(True,60)
triatleta1.Correr()

triatleta2 = Triatleta(False,80)
triatleta2.Pedalar()