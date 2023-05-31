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
        super().__init__(valor)
    def ImprimeValor(self,percentual):
        print(f"O valor do ingresso VIP é: R$ {self.valor+(self.valor*percentual/100)}")

ingressovip = IngressoVip(200)

ingressovip.ImprimeValor(100)