# Atividade Cadastro Dicionário

lista_celular = []
opcao = ""
celular = {}

while opcao != "0":
    print("")
    print("Olá, bem-vindo ao programa para registrar informações de celulares!")
    print("[1] - Adicione algumas informações")
    print("[2] - Listar todas as informações adicionadas")
    print("[3] - Ver a quantidade total de informações")
    print("[0] - Sair")
    
    opcao = input("Digite uma opção a seguir: ")
    
    if opcao == "1":
        celular["modelo"] = input("Digite o modelo do celular: ")
        celular["marca"] = input("Digite a marca dele: ")
        celular["processador"] = input("Digite o processador: ")
        celular["taxa_de_atualização"] = input("Digite a taxa de atualização: ")
        celular["android"] = input("Digite o android do celular: ")
        lista_celular.append(celular)
        celular = {}
        print("Suas informações foram adicionadas com sucesso!")
    elif opcao == "2":
        print("")
        for celular in lista_celular:
            for chave, valor in celular.items():
                print(f"{chave} - {valor}")
    elif opcao == "3":
        quantidade = len(lista_celular)
        print(f"A quantidade total de informações é {quantidade}")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida..")
        
        
        
    
    