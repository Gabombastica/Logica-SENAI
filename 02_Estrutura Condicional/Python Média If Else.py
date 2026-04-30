# Atividade Prática Fluxograma
# Média das Notas

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))
soma_das_notas = nota1 + nota2
media_das_notas = soma_das_notas / 2

# Verificar se o aluno irá ser aprovado ou reprovado
if media_das_notas >= 70:
    print(" Você foi aprovado!")
    
else:
    print("Você foi reprovado!")