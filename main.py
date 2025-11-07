# ... existing code ...
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from exceptions import SaldoInsuficienteError, ContaInexistenteError, ValorInvalidoError

# Registro simples de contas em memória
CONTAS = {}  # chave: numero (str) -> valor: instancia de conta

def prompt_str(msg):
    valor = input(msg).strip()
    while not valor:
        print("Entrada vazia. Tente novamente.")
        valor = input(msg).strip()
    return valor

def prompt_float(msg, positivo=False):
    while True:
        try:
            valor = float(input(msg).strip())
            if positivo and valor <= 0:
                print("Valor deve ser positivo.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite um número.")

def prompt_numero_conta(msg):
    numero = input(msg).strip()
    while not numero:
        print("Número da conta não pode ser vazio.")
        numero = input(msg).strip()
    return numero

def listar_contas():
    if not CONTAS:
        print("Nenhuma conta cadastrada.")
        return
    print("\nContas cadastradas:")
    for numero, conta in CONTAS.items():
        tipo = conta.__class__.__name__
        saldo = getattr(conta, "saldo", 0.0)
        info_extra = ""
        if isinstance(conta, ContaCorrente):
            info_extra = f" | limite: R${conta.limite:.2f}"
        print(f"- {tipo} #{numero} | cliente: {conta.cliente} | agência: {conta.agencia} | saldo: R${saldo:.2f}{info_extra}")
    print()

def criar_conta_corrente():
    print("\nCriar Conta Corrente")
    cliente = prompt_str("Nome do cliente: ")
    agencia = prompt_str("Agência: ")
    numero = prompt_numero_conta("Número da conta: ")
    if numero in CONTAS:
        print("Já existe uma conta com esse número.")
        return
    saldo_inicial = prompt_float("Saldo inicial: ", positivo=False)
    limite = prompt_float("Limite do cheque especial: ", positivo=False)
    conta = ContaCorrente(cliente, agencia, numero, saldo=saldo_inicial, limite=limite)
    CONTAS[numero] = conta
    print(f"ContaCorrente criada com sucesso. Número: {numero}\n")

def criar_conta_poupanca():
    print("\nCriar Conta Poupança")
    cliente = prompt_str("Nome do cliente: ")
    agencia = prompt_str("Agência: ")
    numero = prompt_numero_conta("Número da conta: ")
    if numero in CONTAS:
        print("Já existe uma conta com esse número.")
        return
    saldo_inicial = prompt_float("Saldo inicial: ", positivo=False)
    conta = ContaPoupanca(cliente, agencia, numero, saldo=saldo_inicial)
    CONTAS[numero] = conta
    print(f"ContaPoupanca criada com sucesso. Número: {numero}\n")

def obter_conta(numero):
    conta = CONTAS.get(numero)
    if not conta:
        raise ContaInexistenteError("Conta inexistente.")
    return conta

def depositar():
    print("\nDepósito")
    numero = prompt_numero_conta("Número da conta: ")
    try:
        conta = obter_conta(numero)
        valor = prompt_float("Valor do depósito: ", positivo=True)
        conta.depositar(valor)
    except ContaInexistenteError as e:
        print(f"Erro: {e}")
    except ValorInvalidoError as e:
        print(f"Erro: {e}")

def sacar():
    print("\nSaque")
    numero = prompt_numero_conta("Número da conta: ")
    try:
        conta = obter_conta(numero)
        valor = prompt_float("Valor do saque: ", positivo=True)
        conta.sacar(valor)
    except ContaInexistenteError as e:
        print(f"Erro: {e}")
    except ValorInvalidoError as e:
        print(f"Erro: {e}")
    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")

def transferir():
    print("\nTransferência")
    numero_origem = prompt_numero_conta("Número da conta origem: ")
    numero_destino = prompt_numero_conta("Número da conta destino: ")
    try:
        origem = obter_conta(numero_origem)
        destino = obter_conta(numero_destino)  # garante que a conta existe
        valor = prompt_float("Valor da transferência: ", positivo=True)
        origem.transferir(valor, destino)
    except ContaInexistenteError as e:
        print(f"Erro: {e}")
    except ValorInvalidoError as e:
        print(f"Erro: {e}")
    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")

def verificar_saldo():
    print("\nVerificar Saldo")
    numero = prompt_numero_conta("Número da conta: ")
    try:
        conta = obter_conta(numero)
        conta.verificar_saldo()
    except ContaInexistenteError as e:
        print(f"Erro: {e}")

def ajustar_limite():
    print("\nAjustar Limite (Conta Corrente)")
    numero = prompt_numero_conta("Número da conta: ")
    try:
        conta = obter_conta(numero)
        if not isinstance(conta, ContaCorrente):
            print("Ajuste de limite disponível apenas para ContaCorrente.")
            return
        novo_limite = prompt_float("Novo limite: ", positivo=False)
        conta.limite = novo_limite
        print(f"Limite atualizado para R${conta.limite:.2f}")
    except ContaInexistenteError as e:
        print(f"Erro: {e}")
    except ValorInvalidoError as e:
        print(f"Erro: {e}")

def menu():
    opcoes = {
        "1": ("Criar Conta Corrente", criar_conta_corrente),
        "2": ("Criar Conta Poupança", criar_conta_poupanca),
        "3": ("Depositar", depositar),
        "4": ("Sacar", sacar),
        "5": ("Transferir", transferir),
        "6": ("Verificar Saldo", verificar_saldo),
        "7": ("Listar Contas", listar_contas),
        "8": ("Ajustar Limite (Conta Corrente)", ajustar_limite),
        "9": ("Sair", None),
    }
    while True:
        print("\n=== Sistema Bancário ===")
        for k, (titulo, _) in opcoes.items():
            print(f"{k}. {titulo}")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "9":
            print("Encerrando. Até mais!")
            break
        acao = opcoes.get(escolha)
        if not acao:
            print("Opção inválida.")
            continue
        _, func = acao
        func()

if __name__ == "__main__":
    menu()