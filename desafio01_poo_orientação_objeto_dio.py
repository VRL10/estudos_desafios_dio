from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
          transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data = data_nascimento
        self.cpf = cpf
        super().__init__(endereco)

class Conta:
    def __init__(self, numero: int, cliente: str):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = '001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_conta(cls, cliente_destino: str, numero_id: int):
        return cls(numero_id, cliente_destino)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def saque(self, valor):
        if valor > self._saldo:
            print("O valor de saque é superior ao saldo!")
            return False
        elif valor <= 0:
            print("O valor de saque tem que ser maior que R$ 0,00 .")
            return False
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("O valor do deposito tem que ser superior a R$ 0,00 .")
            return False

class Conta_Corrente(Conta):
    def __init__(self, cliente, numero, limite_saque = 3, valor_limite = 500):
        super().__init__(numero, cliente)
        self._limite_saques = limite_saque
        self._valor_limite = valor_limite
        self._saques_realizados = 0

    def sacar(self, valor):
        numero_transacoes = 0
        for transacao in self.historico.transacao:
            if "Saque" in transacao:
                numero_transacoes += 1

        if numero_transacoes >= self._limite_saques:
            print(f"Essa conta já exerceu o limite máximo de {self._limite_saques} saques")
        elif valor > self._valor_limite:
            print(f"Não é possível sacar esse valor. Pois, o limite disponível é {self._valor_limite}")

        else:
            if super().saque(valor):
                self.historico.adicionar_transacao(f"Saque de R${valor:.2f}")

class Historico:
    def __init__(self):
        self.transacao = []

    def adicionar_transacao(self, transacao):
        self.transacao.append(transacao)

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    @abstractmethod
    def registrar(self,conta):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        saque_sucesso = conta.saque(self.valor)
        if saque_sucesso:
            conta.historico.adicionar_transacao(f"Saque de R${self.valor:.2f}")

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        deposito_sucesso = conta.depositar(self.valor)
        if deposito_sucesso:
            conta.historico.adicionar_transacao(f"Deposito de {self.valor:.2f} ")

# Função para exibir o menu e processar a escolha do usuário
def exibir_menu():
    print("=== Menu ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Saldo")
    print("4. Sair")
    print()

    escolha = input("Escolha uma opção (1/2/3/4): ")
    return escolha


# Criando um cliente pessoa física
cliente1 = Pessoa_Fisica("João", "1990-01-01", "123.456.789-00", "Rua A, 123")

# Criando uma conta corrente para o cliente
conta1 = Conta_Corrente(cliente1.nome, 1)

while True:
    opcao = exibir_menu()

    if opcao == '1':
        valor_deposito = float(input("Digite o valor para depósito: "))
        transacao = Deposito(valor_deposito)
        cliente1.realizar_transacao(conta1, transacao)
    elif opcao == '2':
        valor_saque = float(input("Digite o valor para saque: "))
        transacao = Saque(valor_saque)
        cliente1.realizar_transacao(conta1, transacao)
    elif opcao == '3':
        print(f"Saldo da conta de {cliente1.nome}: R${conta1.saldo:.2f}")
    elif opcao == '4':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")

    print()

# Exibindo o histórico de transações da conta ao final
print(f"Histórico de transações da conta de {cliente1.nome}:")
for transacao in conta1.historico.transacao:
    print(transacao)