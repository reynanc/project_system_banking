from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self, cliente, agencia, numero, saldo=0):
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self._saldo = float(saldo)

    # Métodos protegidos para manipular o saldo internamente
    @property
    def saldo(self):
        return self._saldo

    def _creditar(self, valor):
        self._saldo += float(valor)

    def _debitar(self, valor):
        self._saldo -= float(valor)

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def transferir(self, valor, conta_destino):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def verificar_saldo(self):
        pass

