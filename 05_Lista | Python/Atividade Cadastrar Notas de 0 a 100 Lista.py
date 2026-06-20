import time
# Vamos praticar!
# Cadastrar notas de 0 100

opcao = ""
acima = 0
abaixo = 0
igual = 0
lista_notas = []
while opcao != "0":
    print("Olá estudante, seja bem-vindo ao programa para registrar suas notas! Escolha uma opção a seguir: ")
    print("")
    time.sleep(1)
    print("[1] - Cadastrar notas")
    time.sleep(1)
    print("[2] - Mostrar notas cadastradas")
    time.sleep(1)
    print("[3] - Mostrar notas em ordem crescente")
    time.sleep(1)
    print("[4] - Calcular a média das notas")
    time.sleep(1)
    print("[5] - Mostrar a quantidade de notas no total, mostrar notas abaixo da média e mostrar notas acima da média")
    time.sleep(1)
    print("[6] - Maior e menor nota")
    time.sleep(1)
    print("[0] - Sair")
    print("")
    time.sleep(1)
    opcao = input("Digite uma opção: ")
    print("")
    time.sleep(1)
    if opcao == "1":
        n = int(input("Digite sua nota que deseja cadastrar: "))
        time.sleep(1)
        lista_notas.append(n)
        print("Sua nota foi cadastrada com sucesso!")
        print("")
        time.sleep(1)
    elif opcao == "2":
        print(f"Suas notas cadastradas são {lista_notas}")
        time.sleep(1)
    elif opcao == "3":
            lista_notas.sort()
            print(f" As notas em ordem crescente ficam {lista_notas}")
            time.sleep(1)
    elif opcao == "4":
        soma_notas = sum(lista_notas)
        total_notas = len(lista_notas)
        media = soma_notas / total_notas
        print(f"A média das notas é de {media}")
        time.sleep(1)
    elif opcao == "5":
        soma_notas = sum(lista_notas)
        total_notas = len(lista_notas)
        media = soma_notas / total_notas
        print(f"O número de notas no total é de {total_notas}")
        time.sleep(1)
        for lista_nota in lista_notas:
            if lista_nota > media:
                acima += 1
            elif lista_nota < media:
                abaixo += 1
            elif lista_nota == media:
                igual += 1
        print("")
        print(f"Você tem {acima} nota(s) acima da média!")
        print("")
        time.sleep(1)
        print(f"Você tem {abaixo} nota(s) abaixo da média!")
        print("")
        time.sleep(1)
        print(f"E você tem {igual} nota(s) igual(is) a média!")
        print("")
        time.sleep(1)
    elif opcao == "6":
         maior_nota = max(lista_notas)
         menor_nota = min(lista_notas)
         print(f"A sua maior nota é {maior_nota} e a sua menor nota é {menor_nota}!")
         print("")
         time.sleep(1)
    elif opcao == "0":
        print("Até mais!")
        break
    else:
        print("Opção inválida")
        
                
        
    
        
        
        
        
            
            

