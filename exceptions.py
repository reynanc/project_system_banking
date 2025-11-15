# Exceção lançada quando o saldo não é suficiente
class SaldoInsuficienteError(Exception):
    pass

# Exceção lançada quando a conta não existe
class ContaInexistenteError(Exception):
    pass

# Exceção lançada quando um valor inválido é informado
class ValorInvalidoError(Exception):
    pass