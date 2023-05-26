# Crie uma Classe, Animal, com nome e cor
# como atributos e com um método Comer(),
# quando o método comer foi chamado, deverá
# printar na tela que o animal, foi comer.

class Animal:
    def __init__(self, nome, cor, comendo=False):
        self.nome = nome
        self.cor = cor
        self.comendo = comendo
    def comer(self):
        if self.comendo == False:
            self.comendo = True
            print(f"O {self.nome} foi comer!")
        else:
            self.comendo = True
            print(f"O animal já está comendo e não pode comer novamente!")
    def emitirsom(self):
        print(f"O {self.nome} está emitindo som!")
# animal1 = Animal("gato","branco",False)
# animal1.comer()

class Gato(Animal):
    def __init__(self,nome,cor,comendo=False):
        super().__init__ (nome, cor,comendo)
    def emitirsom(self):
        print(f"O {self.nome} começou a miar!")
    def comer(self):
        print(f"O {self.nome} foi comer!")

class Cachorro(Animal):
    def __init__(self,nome,cor,comendo=False):
        super().__init__ (nome, cor,comendo)
    def emitirsom(self):
        print(f"O {self.nome} começou a latir!")
    def comer(self):
        print(f"O {self.nome} foi comer!")

class Coelho(Animal):
    def __init__(self,nome,cor,comendo=False):
        super().__init__ (nome, cor,comendo)
    def emitirsom(self):
        print(f"O {self.nome} começou a chiar!")
    def comer(self):
        print(f"O {self.nome} foi comer!")

class Vaca(Animal):
    def __init__(self,nome,cor,comendo=False):
        super().__init__ (nome, cor,comendo)


gato1 = Gato("gato","branco", False)
gato1.emitirsom()
gato1.comer()
vaca1 = Vaca("Vaca","Branca",False)
vaca1.emitirsom()
