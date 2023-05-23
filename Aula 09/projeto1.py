class ContaBancaria:
    def __init__ (self,num_conta,saldo, nome_cliente, tipo_conta, status = False):
        self.num_conta = num_conta
        self.saldo = saldo
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.status = status
    def depositar(self,deposito):
        if self.status == True:
            self.saldo += deposito
        else:
            print("Você não pode depositar em uma conta inativa!")
    def sacar(self,saque):
        if self.status == True:
            if saque > self.saldo:
                print("Você não pode sacar uma quantia maior que o saldo!")
            else:
                self.saldo -= saque
                print(f"Você sacou {saque} R$ da sua conta!")
        else:
            print("Você não pode sacar em uma conta inativa!")
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

conta1 = ContaBancaria(123456789,0,"caio","corrente",True)

conta1.desativarconta()
print(conta1.tipo_conta)