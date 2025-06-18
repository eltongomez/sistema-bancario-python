import datetime

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
numero_transacoes = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        if numero_transacoes < 10:
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y')} - Depósito: - R${valor:.2f}\n"
                numero_transacoes += 1
            else:
                print("O valor informado é inválido.")
        else:
            print("""Você não pode realizar a transação. O limite de transações diária foi atingido. 
                                    Por favor, tente de novo amanhã!"""
            )
            break

    elif opcao == "s":
        if numero_transacoes < 10:
            valor = float(input("Informe o valor do saque: "))

            if valor > saldo:
                print("Saldo suficiente.")
            elif valor > limite:
                print("O valor do saque excede o limite de R$ 500,00.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Quantidade se saques diário excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y')} - Saque: - R${valor:.2f}\n"
                numero_saques += 1
                numero_transacoes += 1
            else:
                print("O valor informado é inválido.")
        else:
            print("""Você não pode realizar a transação. O limite de transações diária foi atingido. 
                                                Por favor, tente de novo amanhã!"""
            )
            break

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        break

    elif opcao == "q":
        break

    else:
        print("""              Operação inválida. 
              Por favor, escolha uma das opções apresentadas na tela.""")
