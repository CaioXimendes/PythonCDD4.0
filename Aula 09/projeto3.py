# Crie uma classe chamada Ingresso, que
# possui um valor em reais e um método
# imprimeValor()
# Crie uma classe VIP, que herda de Ingresso e
# possui um valor adicional. Crie um método que
# retorne o valor do ingresso VIP (com o adicional incluído)

class Ingresso:
    def __init__(self,valor):
        self.valor = valor
    def ImprimeValor(self):
        print(f"O valor do ingresso é: R$ {self.valor}")
class IngressoVip(Ingresso):
    def __init__(self,valor):
        super.__init__(self,valor)
    def RetornarValorVip(self):
        return self.valor*1.3 # aumento de 30%