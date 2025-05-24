menu = """
----------------------- ATM SUZANO -----------------------
=======================++++++++++++=======================

Escolha uma Opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Saldo suficiente.")

        elif valor > limite:
            print("O valor do saque excede o limite de R$ 500,00.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Quantidade se saques diário excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "q":
        break

    else:
        print("""              Operação inválida. 
              Por favor, escolha uma das opções apresentadas na tela.""")