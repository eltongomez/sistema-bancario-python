import datetime

def menu():
    menu = """
    ----------------------- ATM SUZANO -----------------------
    =======================++++++++++++=======================

    Escolha uma Opção:

    [u] Novo Usuário
    [c] Nova Conta
    [l] Listar Contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (Apenas os Números): ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe um usuário com o CPF informado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def buscar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado. Cadastre um usuário antes de criar uma conta.")

def imprimir_contas(contas):
    for conta in contas:
        registro = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("-" * 60)
        print(registro)

def depositar(saldo, valor, extrato, numero_transacoes, /):
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y')} - Depósito: - R${valor:.2f}\n"
        numero_transacoes += 1
    else:
        print("O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES, numero_transacoes):
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
    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_transacoes = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            if numero_transacoes < 10:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato, numero_transacoes)
            else:
                print("""Você não pode realizar a transação. O limite de transações diária foi atingido. 
                                            Por favor, tente de novo amanhã!"""
                      )
                break
        elif opcao == "s":
            if numero_transacoes < 10:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, numero_transacoes=numero_transacoes)
            else:
                print("""Você não pode realizar a transação. O limite de transações diária foi atingido. 
                                            Por favor, tente de novo amanhã!"""
                      )
                break
        elif opcao == "e":
            imprimir_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            break
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "l":
            imprimir_contas(contas)
        else:
            print("""              Operação inválida. 
                  Por favor, escolha uma das opções apresentadas na tela.""")

main()