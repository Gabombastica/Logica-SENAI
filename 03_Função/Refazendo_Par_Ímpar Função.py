# Hora de Praticar!
# Refazendo atividade Par ou Ímpar usando o Try e Except
import random
import time

def solicitar_lado():
    while True:
        try:
            lado_jogador = int(input("Escolha uma opção: "))
            
            # Regras
            if lado_jogador >= 0 and lado_jogador <= 2: 
                return lado_jogador
            else:
                raise Exception
        # Erro de Conversão
        except ValueError:
            print("Digite apenas números")
        # Erro de Lógica
        except Exception:
            print("Digite apenas um número de 0 a 2")
            

def solicitar_numero():
    while True:
        try:
            numero_jogador = int(input("Digite um número: "))
            if numero_jogador >= 0 and numero_jogador <= 10:
                return numero_jogador
            else:
                raise Exception
        except ValueError:
            print("Digite somente números")
        except Exception:
            print("Digite um número de 0 a 10")

num_sorteado = random.randint(0, 10)

print("PALÁCIO PAR OU ÍMPAR")
time.sleep(1)
print("Seja bem-vindo(a) ao PALÁCIO PAR OU ÍMPAR!")
time.sleep(1.2)
print("Olá jogador, que bom ver você por aqui, espero que goste do nosso jogo! Para jogar é simples, você deverá escolher par ou ímpar e logo depois deverá escolher um número de 0 a 10. Sem mais demora, vamos começar a batalha!!!")
time.sleep(8)
lado_jogador = ""

while lado_jogador != "0":
    print("")
    print("Escolha uma opção a seguir: ")
    time.sleep(1)
    print("")
    print("[1] - Escolha par")
    time.sleep(1)
    print("[2] - Escolha ímpar")
    time.sleep(1)
    print("[0] - Sair")
    time.sleep(1)
    print("")
    
    lado_jogador = solicitar_lado()
            
    if lado_jogador == 1:
        print("Boa, agora você é oficialmente Par!")
    elif lado_jogador == 2:
        print("Boa, agora você é oficialmente Ímpar!")
        time.sleep(1)
    elif lado_jogador == 0:
        print("Você saiu do jogo:(")
        break
    
    numero_jogador = solicitar_numero()
    
    print(num_sorteado)
    soma = numero_jogador + num_sorteado
    divisao = soma % 2
    if divisao == 0 and lado_jogador == 1:
        print("Parabéns, você ganhouu!")
    elif divisao != 0 and lado_jogador == 1:
        print("Oh que pena, você perdeuu!")
    elif divisao == 0 and lado_jogador == 2:
        print("Oh que pena, você perdeuu!")
    elif divisao != 0 and lado_jogador == 2:
        print("Parabéns, você ganhouu!")
    time.sleep(1)
    print("")
    print("Deseja começar uma nova rodada?")