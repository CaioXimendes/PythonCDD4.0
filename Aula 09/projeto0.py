class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, falando = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def comer (self, comida):
       if self.comendo == True:
           if self.falando == True:
               self.comendo = False
               print(f"{self.nome} não pode comer e falar ao mesmo tempo!")
           else:
               self.comida = comida
               self.comendo = True
               print(f"{self.nome} começou a comer {self.comida}")
       else:
           self.comendo = True
           self.comida = comida
           print(f"{self.nome} começou a comer {self.comida}")
    def parardecomer(self,comida):
        if self.comendo == True:
            if self.falando == True:
                self.comendo = True
                print(f"{self.nome} não pode parar de comer pois já estava comendo")
            else:
                self.comendo = False
                print(f"{self.nome} estava comendo e parou de comer")
        else:
            self.comendo = False
            print(f"{self.nome} não pode parar de comer pois não esta comendo")
    def falar(self):
        if self.falando == True:
            if self.comendo == True:
                self.falando = False
                print(f"{self.nome} não pode falar enquanto come")
            else:
                self.falando = True
                print(f"{self.nome} começou a falar!")
        else:
            if self.comendo == True:
                self.falando = False
                print(f"{self.nome} não pode falar enquanto come")
            else:
                self.falando = True
                print(f"{self.nome} começou a falar!")
    def parardefalar(self):
        if self.falando == True:
            if self.comendo == True:
                self.falando = False
                print(f"{self.nome} não pode parar de falar pois está comendo e não falando ")
            else:
                self.falando = False
                print(f"{self.nome} parou de falar e não estava comendo")
        else:
            if self.comendo == True:
                self.falando = False
                print(f"{self.nome} Não pode parar de falar pois está comendo e não está falando")
            else:
                print(f"{self.nome} Não precisa parar de falar, pois já estava sem falar e sem comer")

p1 = Pessoa("Joao", 80 , 23)
p2 = Pessoa("maria",54,19, True)
# print(p1.nome)
# print(vars(p1))
# print(vars(p2))
#p1.comer("banana")
p2.comer("maça")
#p1.parardecomer("banana")
p2.parardecomer("banana")
#p1.falar()
p2.falar()
#p1.parardefalar()
p2.parardefalar()