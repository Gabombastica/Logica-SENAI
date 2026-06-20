# Hora de praticar!
# Calculadora de Despesas

opcao = ""
valor_total = 0
quantidade_despesas = 0

while opcao != "0":
    print("")
    print("Escolha uma opção a seguir: ")
    print("")
    print("[0] - Sair")
    print("[1] - Adicione o valor da sua despesa: ")
    print("[2] - Mostrar a quantidade de despesas e o valor total")
    print("[3] - Dividir com mais pessoas")
    print("")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
       valor_despesas = float(input("Digite o valor da sua despesa: "))
       valor_total = valor_total + valor_despesas
       quantidade_despesas = quantidade_despesas + 1
    elif opcao == "2":
        if quantidade_despesas == 1:
            print(f"A sua quantidade de despesa é de {quantidade_despesas} e o valor total da sua despesa é de R$ {valor_total}")
        else:
            print(f" A sua quantidade de despesas é de {quantidade_despesas} e o valor total das suas despesas é de R$ {valor_total}")
    elif opcao == "3":
        if quantidade_despesas == 1:
            pessoas_divisao = float(input("Você deseja dividir sua despesa com quantas pessoas?: "))
        else:
            pessoas_divisao = float(input("Você deseja dividir suas despesas com quantas pessoas?: "))
        despesas_divididas = valor_total / pessoas_divisao
        if quantidade_despesas == 1:
            print(f"O valor total da sua despesa a ser paga se você dividir com mais alguém será de R$ {despesas_divididas}")
        else:
            print(f" O valor total das suas despesas a ser paga se você dividir com mais alguém será de R$ {despesas_divididas}")
    elif opcao == "0":
        print("Você terminou o programa, tchau!!")
    
    
    

    


