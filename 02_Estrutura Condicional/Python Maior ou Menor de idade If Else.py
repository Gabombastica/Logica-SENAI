# Atividade Prática Fluxograma
# Maior ou Menor de Idade

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento

# Verificar a Maioridade
if idade >= 18:
    print("Parabéns, você já é adulto!")
    
else:
    print("Oh que pena, você ainda é uma kid :(")