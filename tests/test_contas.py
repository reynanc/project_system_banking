import unittest
from conta_bancaria.conta_corrente import ContaCorrente
from conta_bancaria.conta_poupanca import ContaPoupanca
from exceptions import SaldoInsuficienteError, ValorInvalidoError

class TestContas(unittest.TestCase):
    def test_deposito_valido(self):
        conta = ContaCorrente("Reynan", "0001", "123456", saldo=1000)
        conta.depositar(500)
        self.assertEqual(conta.saldo, 1500)

    def test_deposito_invalido(self):
        conta = ContaCorrente("Reynan", "0001", "123456", saldo=1000)
        with self.assertRaises(ValorInvalidoError):
            conta.depositar(-500)

    def test_saque_valido(self):
        conta = ContaCorrente("Reynan", "0001", "123456", saldo=1000,)
        conta.sacar(500)
        self.assertEqual(conta.saldo, 500)

    def test_saque_saldo_insuficiente(self):
        conta = ContaCorrente("Reynan", "0001", "123456", saldo=1000, limite=0)
        with self.assertRaises(SaldoInsuficienteError):
            conta.sacar(1500)

    def test_transferencia_valida(self):
        conta_origem = ContaCorrente("Reynan", "0001", "123456", saldo=1000)
        conta_destino = ContaCorrente("Laiane", "0001", "654321", saldo=0)
        conta_origem.transferir(500, conta_destino)
        self.assertEqual(conta_origem.saldo, 500)
        self.assertEqual(conta_destino.saldo, 500)

    def test_transferencia_saldo_insuficiente(self):
        conta_origem = ContaCorrente("Reynan", "0001", "123456", saldo=1000)
        conta_destino = ContaCorrente("Laiane", "0001", "654321", saldo=0)
        with self.assertRaises(SaldoInsuficienteError):
            conta_origem.transferir(1500, conta_destino)

    def test_transferencia_entre_contas(self):
        conta_origem = ContaCorrente("Reynan", "0001", "123456", saldo=1000)
        conta_destino = ContaCorrente("Laiane", "0001", "654321", saldo=0)
        conta_origem.transferir(500, conta_destino)
        self.assertEqual(conta_destino.saldo, 500)

if __name__ == "__main__":
    unittest.main()
