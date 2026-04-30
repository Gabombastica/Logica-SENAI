from datetime import datetime

def calcular_idade():
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    idade = datetime.now().year - ano_nascimento
    return idade

def calcular_idade_try():
    while True:
        try:
            ano_atual = datetime.now().year
            ano_nascimento = int(input("Digite o ano do seu nascimento: "))
            
            if ano_nascimento > ano_atual:
                raise Exception
            else: 
                idade = datetime.now().year - ano_nascimento
                return idade
        except ValueError:
            print("Digite apenas números. Ex: 1980")
        except Exception:
            print("Digite um ano menor do que o atual")

