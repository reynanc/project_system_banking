# 📘 Simulador de Transações Bancárias

Projeto desenvolvido como parte do **Módulo 3 — Programação Orientada a Objetos**.

---

## 🎯 Objetivo

Criar um sistema bancário simples em linha de comando (CLI), com foco em:

- Programação Orientada a Objetos (POO)
- Segurança e tratamento de exceções
- Encapsulamento
- Testes unitários
- Princípio LSP (Liskov Substitution Principle)

---

## 🏗️ Arquitetura do Projeto

project_system_banking/
│
├── conta_bancaria/
│ ├── conta.py
│ ├── conta_corrente.py
│ └── conta_poupanca.py
│
├── exceptions.py
├── main.py
│
└── tests/
└── test_contas.py

---

## 🧩 Estrutura de Classes

### 🔹 **Conta** (Classe Abstrata)
Atributos:
- `cliente`
- `agencia`
- `numero`
- `saldo` (encapsulado)

Métodos abstratos:
- `depositar()`
- `sacar()`
- `transferir()`
- `verificar_saldo()`

---

### 🔹 **ContaCorrente**
- Possui atributo `limite`
- Permite saque utilizando saldo + limite
- Permite transferência utilizando limite
- Segue o princípio LSP permitindo transferência para qualquer tipo de `Conta`

---

### 🔹 **ContaPoupanca**
- Não possui limite
- Saques e transferências só podem ocorrer se houver saldo suficiente
- Implementação simples e segura

---

## 🧪 Testes Unitários

### ✔️ Como executar os testes

No terminal:

```bash
python -m unittest discover -s tests -p "test*.py" -v
```

Os testes cobrem:

✔️ Depósitos válidos e inválidos

✔️ Saques válidos e inválidos

✔️ Transferências

✔️ Exceções personalizadas

✔️ Princípio LSP (ContaCorrente → ContaPoupança)

## ▶️ Como rodar o sistema
- No terminal:
```bash
  python main.py
```