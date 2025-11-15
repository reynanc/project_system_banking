from conta_bancaria.conta import Conta
from exceptions import SaldoInsuficienteError, ContaInexistenteError, ValorInvalidoError

class ContaPoupanca(Conta):

    # Realiza depósito verificando valor positivo
    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("Valor de depósito deve ser positivo.")
        self._creditar(float(valor))
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    # Realiza transferência para qualquer conta derivada de Conta
    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Conta):
            raise ContaInexistenteError("Conta de destino inexistente.")
        if valor <= 0:
            raise ValorInvalidoError("Valor de transferência deve ser positivo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para transferência.")
        self._debitar(float(valor))
        conta_destino.depositar(float(valor))
        print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero} realizada. Novo saldo: R${self.saldo:.2f}")

    # Realiza saque sem utilizar limite (apenas saldo próprio)
    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("Valor de saque deve ser positivo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para saque.")
        self._debitar(float(valor))
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    # Exibe o saldo atual
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")