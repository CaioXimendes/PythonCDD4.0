import datetime

arquivo = open("extrato.txt", "a")

class ContaBancaria:
    def __init__(self, num_conta, saldo, nome_cliente, tipo_conta,limite,status=False):
        self.num_conta = num_conta
        self.saldo = saldo
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.limite = limite
        self.extrato = False
        self.data_atual = datetime.datetime.now()
        self.deposito = 0
        self.saque = 0
        self.status = status
    def consultarextrato(self):
        if self.status:
            if self.extrato:
                print(f"Número da conta: {self.num_conta}, depósito de R$ {self.deposito} ocorrido em: {self.data_atual}")
            else:
                print(f"Número da conta: {self.num_conta}, saque de R$ {self.saque} ocorrido em: {self.data_atual}")
        else:
            print("Não é possível consultar o extrato de uma conta desativada!")
    def ativarlimite(self):
        if self.status:
            if self.limite == 0:
                print("Seu limite agora está ativado!")
            else:
                print("Você não pode ativar o limite não estando zerado!")
        else:
            print("Não é possível ativar o limite de uma conta desativada!")
    def desativarlimite(self):
        if self.status:
            if self.limite != 0:
                print("Não é possivel desativar um limite diferente de 0")
            else:
                self.limite = 0
                print("Seu limite agora está desativado!")
        else:
            print("Não é possível desativar o limite de uma conta desativada!")

    def depositar(self, deposito):
        if self.status:
            if self.limite != 0:
                if self.saldo <= 0:
                    valor_depositado_no_limite = deposito + self.saldo
                    self.saldo = 0
                    valor_depositado_no_saldo = valor_depositado_no_limite + self.saldo
                    self.saldo = valor_depositado_no_saldo
                    print(f"Você depositou R${deposito}")
                    self.extrato = True
                    self.deposito = deposito
                    arquivo.write(f"Número da conta: {self.num_conta}, depósito de R$ {self.deposito} ocorrido em: {self.data_atual}\n")
                else:
                    self.saldo += deposito
                    print(f"Você depositou R${deposito}")
                    self.extrato = True
                    self.deposito = deposito
                    arquivo.write(f"Número da conta: {self.num_conta}, depósito de R$ {self.deposito} ocorrido em: {self.data_atual}\n")
            else:
                self.saldo += deposito
                print(f"Você depositou R${deposito}")
                self.extrato = True
                self.deposito = deposito
                arquivo.write(f"Número da conta: {self.num_conta}, depósito de R$ {self.deposito} ocorrido em: {self.data_atual}\n")
        else:
            print("Você não pode depositar em uma conta inativa!")
    def sacar(self,saque):
        if self.status:
            if self.limite != 0:
                if saque > self.saldo:
                    valor_retirado = saque - self.saldo
                    valor_retirado_do_limite = self.limite - valor_retirado
                    self.saldo = valor_retirado_do_limite - self.limite
                    print(f"você sacou R$ {saque}")
                    self.extrato = False
                    self.saque = saque
                    arquivo.write(f"Número da conta: {self.num_conta}, saque de R$ {self.saque} ocorrido em: {self.data_atual}\n")
                else:
                    self.saldo -= saque
                    print(f"você sacou R$ {saque}")
                    self.extrato = False
                    self.saque = saque
                    arquivo.write(f"Número da conta: {self.num_conta}, saque de R$ {self.saque} ocorrido em: {self.data_atual}\n")

            elif self.limite == 0 and saque > self.saldo:
                valor_retirado_do_saldo = saque - self.saldo
                valor_sacado_sem_limite = saque - valor_retirado_do_saldo
                self.saldo -= valor_sacado_sem_limite
                print(f"você sacou R$ {valor_sacado_sem_limite} e o valor que queria sacar {saque}")
                self.extrato = False
                self.saque = saque
                arquivo.write(f"Número da conta: {self.num_conta}, saque de R$ {self.saque} ocorrido em: {self.data_atual}\n")

            elif self.limite == 0 and self.saldo > saque:
                self.saldo -= saque
                print(f"você sacou R$ {saque}")
                self.extrato = False
                self.saque = saque
                arquivo.write(f"Número da conta: {self.num_conta}, saque de R$ {self.saque} ocorrido em: {self.data_atual}\n")

            elif self.limite == 0 and self.saldo == saque:
                valor_retirado_do_saldo = self.saldo - saque
                valor_sacado_sem_limite = saque - valor_retirado_do_saldo
                self.saldo -= valor_sacado_sem_limite
                print(f"você sacou R$ {valor_sacado_sem_limite}")
                self.extrato = False
                self.saque = saque
                arquivo.write(f"Número da conta: {self.num_conta}, saque de R$ {self.saque} ocorrido em: {self.data_atual}\n")
        else:
            print("Você não pode sacar em uma conta desativada!")

    def verificarsaldo (self):
        if self.status:
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

conta1 = ContaBancaria(123456789,4,"caio","corrente",0,False)

#print(conta1.tipo_conta)
conta1.ativarconta()
conta1.desativarlimite()
conta1.verificarsaldo()
conta1.sacar(3)
conta1.verificarsaldo()
conta1.depositar(450)
conta1.sacar(1)
conta1.verificarsaldo()
conta1.depositar(5000)
conta1.sacar(5450)
conta1.verificarsaldo()
conta1.consultarextrato()
