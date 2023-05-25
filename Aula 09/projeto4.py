# Crie uma classe chamada Forma, que possui os atributos area e perímetro.
# Implemente as subclasses Retângulo e Triangulo, que devem conter os métodos calculaArea e
# calcula Perímetro.
# A classe Triangulo deve ter também o atributo altura.
# No código de teste crie um objeto da classe Triangulo e outro da Classe Retângulo.
# Verifique se os dois são mesmo instancias de Forma (use instanceof), e calcule a área de cada um.

class Forma:
    def __init__(self,area,perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, base, altura, area, perimetro):
        super().__init__(area, perimetro)
        self.base = base
        self.altura = altura
    def CalculaArea(self):
        self.area = self.base * self.altura
        return self.area
    def CalculaPerimetro(self):
        self.perimetro = 2*(self.base + self.altura)
        return self.perimetro
class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3, area, perimetro):
        super().__init__(area, perimetro)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def CalculaArea(self):
        self.area = (self.base * self.altura)/2
        return self.area
    def CalculaPerimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return self.perimetro

retangulo1 = Retangulo(2, 5, 0, 0)

if isinstance(retangulo1, Retangulo): #verifica se o objeto retangulo1 está estanciado na classe Retangulo
    print(retangulo1.CalculaArea())
    print(retangulo1.CalculaPerimetro())

triangulo1 = Triangulo(2, 5, 1, 2, 3, 0, 0)

if isinstance(triangulo1, Triangulo): #verifica se o objeto triangulo1 está estanciado na classe Triangulo
    print(triangulo1.CalculaArea())
    print(triangulo1.CalculaPerimetro())