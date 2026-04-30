import time
# Hora de Praticar!
# Refazendo a atividade do Cadastramento de Notas de 0 a 100, usando o Try Except

def solicitar_opcao():
    while True:
        try:
            # Linha que eu quero repetir
            opcao = int(input("Digite uma opção: "))
            
            if opcao > 6:
                raise Exception
            else:
                return opcao
        # Erro de Conversão
        except ValueError:
            print("Digite apenas números e que sejam de 0 a 6: ")
        # Erro de lógica
        except Exception:
            print("Digite apenas números e que sejam de 0 a 6: ")
            
def solicitar_nota():
    while True:
            try:
                n = int(input("Digite sua nota que deseja cadastrar: "))
                if n > 100:
                    raise Exception
                else:
                    print("Sua nota foi cadastrada com sucesso!")
                break
            except Exception:
                print("Digite notas somente de 0 a 100")


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
    
    opcao = solicitar_opcao()
    
    if opcao == 1:
        n = solicitar_nota()
        lista_notas.append(n)
        
    elif opcao == 2:
        print(f"Suas notas cadastradas são {lista_notas}")
    elif opcao == 3:
            lista_notas.sort()
            print(f" As notas em ordem crescente ficam {lista_notas}")
    elif opcao == 4:
        soma_notas = sum(lista_notas)
        total_notas = len(lista_notas)
        media = soma_notas / total_notas
        print(f"A média das notas é de {media}")
    elif opcao == 5:
        soma_notas = sum(lista_notas)
        total_notas = len(lista_notas)
        media = soma_notas / total_notas
        print(f"O número de notas no total é de {total_notas}")
        for lista_nota in lista_notas:
            if lista_nota > media:
                acima += 1
            elif lista_nota < media:
                abaixo += 1
            elif lista_nota == media:
                igual += 1
        print(f"Você tem {acima} nota(s) acima da média!")
        print(f"Você tem {abaixo} nota(s) abaixo da média!")
        print(f"E você tem {igual} nota(s) igual(is) a média!")
    elif opcao == 6:
         maior_nota = max(lista_notas)
         menor_nota = min(lista_notas)
         print(f"A sua maior nota é {maior_nota} e a sua menor nota é {menor_nota}!")
    elif opcao == 0:
        print("Até mais!")
        break
    else:
        print("Opção inválida")