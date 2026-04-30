# Loop infinito
# break interrompe um loop
while True:
    print("Bom dia")
    break

# Loop que para com uma condição
opcao = "0"
while opcao != "0":
    print("Escolha uma opção")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[0] - Sair")
    opcao = input("Digite a opção: ")
    if opcao == "1":
        print("Somei")
    elif opcao == "2":
        print("Subtrai")
        
# Exemplo de contar até 10

n = 0

while n <= 10:
    print(n)
    # n = n + 1 = Incrementa
    # n = n - 1 = Decrementa
    n = n + 1
    