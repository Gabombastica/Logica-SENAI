# Hora de praticar!
# Menu

opcao = ""
while opcao != "0":
    print("")
    print("Escolha uma opção a seguir: ")
    print("")
    print("[1] - Raiz Quadrada")
    print("[2] - Quadrado")
    print("[3] - Cubo")
    print("[4] - Tabuada")
    print("[0] - Sair")
    print("")
    opcao = input("Digite uma opção: ")
    
    if opcao == "1":
        num1 = float(input("Digite um número para saber a sua Raiz Quadrada: "))
        calculo1 = num1**0.5
        print(f"O resultado da Raiz Quadrada do seu número é de {calculo1}")
    elif opcao == "2":
        num2 = float(input("Digite um número para saber o seu Quadrado: "))
        calculo2 = num2 * num2
        print(f"O resultado do Quadrado do seu número é de {calculo2}")
    elif opcao == "3":
        num3 = float(input("Digite um número para saber o seu Cubo: "))
        calculo3 = num3 * num3 * num3
        print(f"O resultado do Cubo do seu número é de {calculo3}")
    elif opcao == "4":
        num4 = float(input("Digite um número para saber sua Tabuada: "))
        resultado_multiplicacao1 = num4 * 1
        resultado_multiplicacao2 = num4 * 2
        resultado_multiplicacao3 = num4 * 3
        resultado_multiplicacao4 = num4 * 4
        resultado_multiplicacao5 = num4 * 5
        resultado_multiplicacao6 = num4 * 6
        resultado_multiplicacao7 = num4 * 7
        resultado_multiplicacao8 = num4 * 8
        resultado_multiplicacao9 = num4 * 9
        resultado_multiplicacao10 = num4 * 10
        print(f"A tabuada do {num4} é")
        print(f"{num4} x 1 = {resultado_multiplicacao1}")
        print(f"{num4} x 2 = {resultado_multiplicacao2}")
        print(f"{num4} x 3 = {resultado_multiplicacao3}")
        print(f"{num4} x 4 = {resultado_multiplicacao4}")
        print(f"{num4} x 5 = {resultado_multiplicacao5}")
        print(f"{num4} x 6 = {resultado_multiplicacao6}")
        print(f"{num4} x 7 = {resultado_multiplicacao7}")
        print(f"{num4} x 8 = {resultado_multiplicacao8}")
        print(f"{num4} x 9 = {resultado_multiplicacao9}")
        print(f"{num4} x 10 = {resultado_multiplicacao10}")
    else:
        print("Opção inválida, até mais!")
        
    
    
    