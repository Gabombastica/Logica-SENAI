# Como criar uma função
# Estrutura
# def nome():

def exibir_saudacao():
    print("Bom dia")

def solicitar_nome():
    nome = input("Digite seu nome: ")
    return nome 
 
# Vamos usar o return quando precisar utilizar aquela informação
def somar():
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = num1 + num2
    return resultado

# Não preciso usar o return quando preciso/ quero só informar
def exibir_soma():
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = num1 + num2
    print(f"O resultado da soma é {resultado}")
    
# Usamos parâmetros para informar valores externos
# Usamos a vírgula para separar os parâmetros
def somar(num1, num2):
    resultado = num1 + num2
    return resultado
      
print(somar(500089, 6789))
