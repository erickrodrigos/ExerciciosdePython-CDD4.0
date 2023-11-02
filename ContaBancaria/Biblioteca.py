class ContaBancaria:
    def __init__(self, Numero, Saldo, nome, tipo, Limite, Status=False):
        self.Numero = Numero
        self.Saldo = Saldo
        self.nome = nome
        self.tipo = tipo
        self.Limite = Limite
        self.Status = Status

    def Ativarconta(self,Status):
        if Status == True:
            print("Conta ativada")
        else:
            print("Essa conta já está ativada")
    def VerificarSaldo(self):
        print(f"Saldo: R$ {self.Saldo}")

    def Depositar(self, valor_deposito):
        self.Saldo += valor_deposito
        print(f'Depositado um valor de: R$ {valor_deposito}')
        self.VerificarSaldo()
    def Sacar(self, valor_saque):
        if valor_saque > self.Limite:
            print(f"O valor do saque de R$ {valor_saque} é maior que seu limite de R$ {self.Limite}")
        if valor_saque > self.Saldo:
            print("Saldo insuficiente")
        else:
            self.Saldo -= valor_saque
            print(f'Sacado um valor de: R$ {valor_saque}')
            self.VerificarSaldo()
    def Emprestimo(self,ValorEmprestimo):
        print(f"  vi que deseja solicitar um Emprestimo de Valor {ValorEmprestimo}  ")
        if self.Limite >= ValorEmprestimo:
            self.Saldo += ValorEmprestimo
            print(f"emprestimo concebido: o seu novo Saldo em conta é {self.Saldo}")
        else:
            print(" voce não tem limite para isso. ")

    def SolicitarLimite(self,ValorLimite):
        print(f" vi que deseja aumentar o seu limite para {ValorLimite} LHE FOI CONCEBIDO UM NOVO LIMITE PARABÉNS !!!!!!")
        self.Limite = ValorLimite * -1
        print(f'Adicionado limite de R${self.limite * -1}')