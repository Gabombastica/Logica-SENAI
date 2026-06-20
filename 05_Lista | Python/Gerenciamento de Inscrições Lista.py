# Atividade Gerenciamento de Inscrições
import time

lista_nomes = []
 
opcao = ""
while opcao != "0":
    print("Olá estudante, seja bem-vindo ao programa para registrar suas inscrições para o evento escolar! Escolha uma opção a seguir: ")
    time.sleep(1.5)
    print("")
    print("[1] - Cadastrar nomes")
    time.sleep(0.5)
    print("[2] - Total de inscritos")
    time.sleep(0.5)
    print("[3] - Lista de nomes em ordem alfabética")
    time.sleep(0.5)
    print("[4] - Consulta de um nome")
    time.sleep(0.5)
    print("[0] - Sair")
    time.sleep(0.5)
    print("")
    
    opcao = input("Digite uma opção: ")
    time.sleep(0.5)
    if opcao == "1":
        while True:
            nome = input("Digite o nome que deseja cadastrar: ")
            time.sleep(0.5)
            if nome in lista_nomes:
                print("Esse nome já está na lista! Adicione outro nome, ou finalize o cadastro")
                time.sleep(0.5)
            else:
                lista_nomes.append(nome)
                print("O nome foi cadastrado com sucesso!")
                break
                print("")
    elif opcao == "2":
        print(f"Os nomes inscritos são {len(lista_nomes)}")
        time.sleep(0.5)
        print("")
    elif opcao == "3":
        lista_nomes.sort()
        print(f"Os nomes em ordem alfabética são: ")
        time.sleep(0.5)
        for lista_nome in lista_nomes:
            print(lista_nome)
            print("")
    elif opcao == "4":
        nome_desejado = input("Digite o nome que deseja consultar: ")
        time.sleep(0.5)
        if nome_desejado in lista_nomes:
            n = input("Nome encontrado! Deseja removê-lo? (s/n): ")
            time.sleep(0.5)
            if n == "s" or n == "S":
                lista_nomes.remove(nome_desejado)
                print(f"O nome {nome_desejado} foi removido com sucesso!")
                time.sleep(0.5)
            elif n == "n" or n == "N":
                print(f"O nome {nome_desejado} não foi removido")
                time.sleep(0.5)
        elif nome_desejado not in lista_nomes:
            n = input("Nome não encontrado. Deseja adicioná-lo? (s/n): ")
            time.sleep(0.5)
            if n == "s" or n == "S":
                lista_nomes.append(nome_desejado)
                print(f"O nome {nome_desejado} foi adicionado com sucesso!")
                time.sleep(0.5)
            elif n == "n" or n == "N":
                print(f"O nome {nome_desejado} não foi adicionado")
                time.sleep(0.5)
    elif opcao == "0":
        print("Você saiu do programa, até mais!")
        break
    else:
        print("Opção inválida")
        
            
        

