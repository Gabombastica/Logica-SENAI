# Criar um Dicionário

aluno = { 
    "nome": "Gabriely",
    "idade": 15,
    "ano_escolar": 2,
    "genero": "Feminino"
    }

# Adicionar um campo/ característica
aluno["altura"] = 1.60

#Editar um valor
aluno["idade"] = 16

# Exibir os dados do Dicionário em forma de lista
for chave, valor in aluno.items():
    print(f"{chave} - {valor}")
    
print(aluno)
