import time

numero = int(input("Digite um número qualquer: "))
while numero >= 0:
    print(numero)
    time.sleep(0.5)
    numero = numero - 1
    time.sleep(0.5)
print("A contagem chegou ao final!")