from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, cliente, agencia, numero, saldo=0):
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self._saldo = float(saldo)

    # Retorna o saldo atual (encapsulamento protegido)
    @property
    def saldo(self):
        return self._saldo

    # Credita um valor ao saldo (uso interno da classe)
    def _creditar(self, valor):
        self._saldo += float(valor)

    # Debita um valor do saldo (uso interno da classe)
    def _debitar(self, valor):
        self._saldo -= float(valor)

    # Método abstrato para depósito
    @abstractmethod
    def depositar(self, valor):
        pass

    # Método abstrato para transferência
    @abstractmethod
    def transferir(self, valor, conta_destino):
        pass

    # Método abstrato para saque
    @abstractmethod
    def sacar(self, valor):
        pass

    # Método abstrato para exibir o saldo
    @abstractmethod
    def verificar_saldo(self):
        pass

