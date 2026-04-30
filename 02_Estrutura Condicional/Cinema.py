# Vamos praticar!
# Cinema

ano_nascimento = int(input("Digite seu ano de nascimento: "))
estuda = str(input("Você está em alguma instituição de ensino?: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento

if idade >= 60 or estuda == "Sim" or estuda == "sim":
    print("Você pagará meia entrada, parabéns!")
    
else:
    print("Você pagará entrada inteira, que triste :(")
    
