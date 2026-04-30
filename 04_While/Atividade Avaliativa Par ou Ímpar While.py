import random
import time

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
    lado_jogador = str(input("Escolha uma opção: "))
    if lado_jogador == "1":
        print("Boa, agora você é oficialmente Par!") 
        time.sleep(1)
    elif lado_jogador == "2":
        print("Boa, agora você é oficialmente Ímpar!")
        time.sleep(1)
    elif lado_jogador == "0":
        print("Você saiu do jogo:(")
        break
    numero_jogador = int(input("Digite um número: "))
    print(num_sorteado)
    soma = numero_jogador + num_sorteado
    divisao = soma % 2
    if divisao == 0 and lado_jogador == "1":
        print("Parabéns, você ganhouu!")
    elif divisao != 0 and lado_jogador == "1":
        print("Oh que pena, você perdeuu!")
    elif divisao == 0 and lado_jogador == "2":
        print("Oh que pena, você perdeuu!")
    elif divisao != 0 and lado_jogador == "2":
        print("Parabéns, você ganhouu!")
    time.sleep(1)
    print("")
    print("Deseja começar uma nova rodada?")
    
    
    
        
        
    
