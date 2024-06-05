menu = '''---MENU----
   Digite o número da opção desejada:
   OP1 - DEPOSITAR
   OP2 - SACAR
   OP3 - EXTRATO
   OP4 - SAIR
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

while True:
    try:
        op = int(input(menu))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número correspondente à opção desejada.")
        continue
    
    if op == 1:
        try:
            deposito = float(input("Digite o valor que você deseja depositar: "))
            if deposito <= 0:
                print("O valor de depósito deve ser positivo!")
                continue
            saldo += deposito
            print("Depósito concluído com sucesso!")
            extrato += f"Depósito de R$ {deposito:.2f}\n"
        except ValueError:
            print("Entrada inválida! Por favor, digite um valor numérico válido.")
    
    elif op == 2:
        if numero_saques >= LIMITE_SAQUES_DIARIO:
            print("Você atingiu o limite diário de saques!")
            continue
        try:
            sacar = float(input("Digite o valor que você quer sacar: "))
            if sacar <= 0:
                print("O valor de saque deve ser positivo!")
                continue
            if sacar > limite:
                print("Não é possível sacar esse valor, pois ultrapassa o limite de R$ 500,00")
            elif sacar > saldo:
                print("Não há saldo suficiente para realizar o saque!")
            else:
                saldo -= sacar
                numero_saques += 1
                print("Saque concluído com sucesso!")
                extrato += f"Saque de R$ {sacar:.2f}\n"
        except ValueError:
            print("Entrada inválida! Por favor, digite um valor numérico válido.")
    
    elif op == 3:
        print("\n---EXTRATO---")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo: R$ {saldo:.2f}")
    
    elif op == 4:
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Tente novamente!")