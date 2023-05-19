class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, falando = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def comer (self, comida):
       if self.comendo == True:
           print(f"{self.nome} já foi comer e não precisa comer novamente")
       else:
           self.comida = comida
           print(f"{self.nome} foi comer {self.comida}")
    def parardecomer(self,comida):
        if self.comendo == True:
            self.comida = comida
            self.comendo = False
            print(f"{self.nome} estava comendo {self.comida} e parou de comer")
        else:
            print(f"{self.nome} não estava comendo")
    def falar(self):
        if self.falando == True:
            if self.comendo == False:
                print(f"{self.nome} já está falando e não pode falar novamente")
            else:
                self.falando = False
                print(f"{self.nome} não pode falar pois já está comendo!")
        else:
            if self.comendo == True:
                print(f"{self.nome} não esta falando e não pode falar enquanto come")
            else:
                self.falando = True
                print(f"{self.nome} não esta falando e nem comendo e começou a falar")
    def parardefalar(self):
        if self.falando == True:
            if self.comendo == True:
                self.falando = False
                print(f"{self.nome} não está falando pois ainda está comendo ")
            else:
                print(f"{self.nome} parou de falar e não estava comendo")
        else:
            if self.comendo == True:
                self.falando = False
                print(f"{self.nome} Não está falando e está comendo")
            else:
                print(f"{self.nome} Parou de falar e também não estava comendo")

p1 = Pessoa("Joao", 80 , 23)
p2 = Pessoa("maria",54,19, True)
# print(p1.nome)
# print(vars(p1))
# print(vars(p2))
p1.comer("banana")
p2.comer("maça")
p1.parardecomer("banana")
p2.parardecomer("banana")
p1.falar()
p2.falar()
p1.parardefalar()
p2.parardefalar()