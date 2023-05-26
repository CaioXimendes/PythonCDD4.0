class ContaBancaria:
    def __init__ (self,num_conta,saldo, nome_cliente, tipo_conta, limite,status = False):
        self.num_conta = num_conta
        self.saldo = saldo
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.limite = limite
        self.status = status
    def ativarlimite(self):
        if self.status == True:
            if self.limite == 0:
                print("Seu limite agora está ativado!")
            else:
                print("Você não pode ativar o limite não estando zerado!")
        else:
            print("Não é possível ativar o limite de uma conta desativada!")
    def desativarlimite(self):
        if self.status == True:
            if self.limite != 0:
                print("Não é possivel desativar um limite diferente de 0")
            else:
                print("Seu limite agora está desativado!")
                self.limite = 0
        else:
            print("Não é possível desativar o limite de uma conta desativada!")

    def depositar(self,deposito):
        if self.status == True:
            self.saldo += deposito
        else:
            print("Você não pode depositar em uma conta inativa!")
    def sacar(self,saque):
        if saque > self.saldo:
            novo_saldo = (saque - self.saldo) - (saque - self.limite)
            self.saldo = novo_saldo
            print(f"você sacou R$ {saque}")
    def verificarsaldo (self):
        if self.status == True:
            print(f"Seu saldo atual é de: R${self.saldo}")
        else:
            print(f"Não é possível verificar o saldo de uma conta inativa!")
    def ativarconta(self):
        if self.status == True:
            print("Essa conta já está ativa! Nâo é possível ativar novamente!")
        else:
            self.status = True
            print("Sua conta foi ativada com sucesso!")
    def desativarconta(self):
        if self.status == True:
            if self.saldo == 0:
                print(f"Sua conta foi desativada com sucesso!")
            else:
                print(f"Não é possível desativar sua conta, pois o saldo não está zerado!")
        else:
            print("Não é possível desativar uma conta que já está desativada!")

conta1 = ContaBancaria(123456789,800,"caio","corrente",1000,False)

print(conta1.tipo_conta)
conta1.ativarconta()
conta1.ativarlimite()
conta1.verificarsaldo()
conta1.sacar(1000)
conta1.verificarsaldo()