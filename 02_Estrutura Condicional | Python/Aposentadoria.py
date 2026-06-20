# Vamos praticar!
# Aposentadoria

# Para importar funções externas precisamos usar o import
# from arquivo import nome_das_funcoes
from funcoes import calcular_idade_try

idade = calcular_idade_try()
genero = input("Digite seu sexo masculino ou feminino: ")


if genero == "homem" and idade >= 65:
    print("Você já pode se aposentar com sucesso!")
    
elif genero == "mulher" and idade >= 62:
    print("Você já pode se aposentar com sucesso!")

# Esse Else serve tanto para o homem ou mulher
else:
    print("Oh que pena, você ainda não atingiu a idade para a sua aposentadoria!")


