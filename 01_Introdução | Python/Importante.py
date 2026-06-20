# 1- Como salvar dados/ informações
# Usando variáveis
nome = "Gaby"
salario = 1500.50

# 2- Como solicitar informações
# Usando input
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

# 3- Como exibir informações
# Usando o print
print(f"Seu nome é {nome} e seu salário é {salario}")

# 4- Como fazer verificações
# Usando o If Else
if salario > 1600:
    print("Salário maior que o mínimo")
else:
    print("Salário menor que o mínimo")
    
# 5- Como solicitar informações complexas
# Usando um menu

print("Escolha seu sexo")
print("1- Masculino")
print("2- Feminino")
sexo_escolha = input("Digite a opção: ")

if sexo_escolha == "1":
    sexo = "Masculino"
elif sexo_escolha == "2":
    sexo = "Feminino"
else:
    print("Opção inválida")