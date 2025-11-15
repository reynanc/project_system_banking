from conta_bancaria.conta import Conta
from exceptions import SaldoInsuficienteError, ContaInexistenteError, ValorInvalidoError

class ContaCorrente(Conta):
    def __init__(self, cliente, agencia, numero, saldo=0, limite=0):
        super().__init__(cliente, agencia, numero, saldo)
        self._limite = float(limite)

    # Retorna o limite da conta corrente
    @property
    def limite(self):
        return self._limite

    # Define um novo limite de crédito
    @limite.setter
    def limite(self, valor):
        if valor < 0:
            raise ValorInvalidoError("Limite não pode ser negativo.")
        self._limite = float(valor)

    # Realiza depósito verificando valor positivo
    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do depósito deve ser positivo.")
        self._creditar(float(valor))
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    # Realiza transferência para outra conta
    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Conta):
            raise ContaInexistenteError("Conta de destino inexistente.")
        if valor <= 0:
            raise ValorInvalidoError("O valor da transferência deve ser positivo.")
        if valor > self.saldo + self.limite:
            raise SaldoInsuficienteError("Saldo insuficiente para transferência.")
        self._debitar(float(valor))
        conta_destino.depositar(float(valor))
        print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero} realizada. Novo saldo: R${self.saldo:.2f}")

    # Realiza saque permitindo uso do limite
    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do saque deve ser positivo.")
        if valor > self.saldo + self.limite:
            raise SaldoInsuficienteError("Saldo insuficiente para saque.")
        self._debitar(float(valor))
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    # Exibe o saldo atual
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
    