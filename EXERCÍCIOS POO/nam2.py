'''Crie um sistema para um aplicativo bancário, que possui a Classe
ContaBancaria com as seguintes características:
○ Atributos: titular, saldo, numero_conta e tipo_conta.
○ Métodos: depositar, sacar, transferir e verificar_saldo.
OBS: Após cada alteração no saldo, exiba o novo valor na tela.'''

class ContaBancaria:
    def _init_(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        self.verificar_saldo()

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")
        self.verificar_saldo()

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso.")
        else:
            print("Saldo insuficiente para realizar a transferência.")
        self.verificar_saldo()

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta1 = ContaBancaria("Débora", 1000.00, "123456", "Corrente")
conta2 = ContaBancaria("Carlos", 500.00, "654321", "Poupança")

conta1.depositar(200) 
conta1.sacar(150)             
conta1.transferir(300, conta2) 
conta1.verificar_saldo()      
conta2.verificar_saldo()      