# Crie uma classe chamada Forma, que possui os atributos area e perímetro.
# Implemente as subclasses Retângulo e Triangulo, que devem conter os métodos calculaArea e
# calcula Perímetro.
# A classe Triangulo deve ter também o atributo altura.
# No código de teste crie um objeto da classe Triangulo e outro da Classe Retângulo.
# Verifique se os dois são mesmo instancias de Forma (use instanceof), e calcule a área de cada um.

class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def CalculaArea(self,base,altura):
        self.area = base * altura
        print(f"A área do retângulo é: {self.area}")
    def CalculaPerimetro(self,base,altura):
        self.perimetro = 2*(base + altura)
        print(f"O perímetro do retângulo é: {self.perimetro}")
class Triangulo(Forma):
    def __init__(self):
        super().__init__()
    def CalculaArea(self,base,altura):
        self.area = (base * altura)/2
        print(f"A área do triângulo é: {self.area}")
    def CalculaPerimetro(self,lado1,lado2,lado3):
        self.perimetro = lado1 + lado2 + lado3
        print(f"O perimetro do triangulo é: {self.perimetro}")

retangulo1 = Retangulo()
triangulo1 = Triangulo()

if isinstance(retangulo1,Retangulo):
    retangulo1.CalculaArea(2,5)
    retangulo1.CalculaPerimetro(2,5)

if isinstance(triangulo1,Triangulo):
    triangulo1.CalculaArea(2,5)
    triangulo1.CalculaPerimetro(2,2,2)