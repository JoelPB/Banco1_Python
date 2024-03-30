menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("\033[32m" + "Informe o valor do depósito: " + "\033[0;0m"))
        if valor > 0:
            saldo += valor
            extrato += "\033[32m" + f"Depósito: R$ {valor:.2f}\n" + "\033[0;0m"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("\033[31m" + "Informe o valor do saque: " + "\033[0;0m"))
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor de saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += "\033[31m" + f"Saque: R$ {valor:.2f}\n" + "\033[0;0m"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=========== EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\033[30;1;43m" + f"\nSaldo: R$ {saldo:.2f}\n" + "\033[0;0m")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
