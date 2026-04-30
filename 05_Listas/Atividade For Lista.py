import time
# Atividade Prática: For

# 1- Crie uma lista com os nomes de 5 objetos
objetos = ["Lápis", "Lapiseira", "Grifa-texto", "Corretivo", "Borracha"]
print(f"Foi criada uma lista com 5 objetos: {objetos}")
print("")
time.sleep(1)

# 2- Adicione mais um objeto ao final da lista
#obj = input("Digite um objeto: ")
#objetos.append(obj)
#print(f"Foi eliminado o objeto {obj}")
objetos.append("Tesoura")
print('O objeto "Tesoura" foi adicionado na lista')
print("")
time.sleep(1)

# 3- Acesse o objeto que está na 2° posição e exiba-o
objetos[1]
print(f"O objeto da 2° posição é {objetos[1]}")
print("")
time.sleep(1)

# 4- Remova um objeto da lista e exiba-o
#obj2 = input("Digite um objeto: ")
#objetos.remove(obj2)
#print(f"Foi eliminado o objeto {obj2}")
objetos.remove("Grifa-texto")
print(f"O objeto removido foi o Grifa-texto")
print("")
time.sleep(1)

# 5- Exiba o tamanho da lista
print(f"O número de objetos na lista é de {len(objetos)}")
print("")
time.sleep(1)

# 6- Mostre todos os itens com o for
for objeto in objetos:
    time.sleep(1)
    print(objeto)
print("")
time.sleep(1)

# 7- Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione
print("Foi adicionado mais um objeto na lista: ")
print("")
time.sleep(1)
if "Cadeira" in objetos:
    objetos.remove("Cadeira")
else:
    objetos.append("Cadeira")
    
# 8- Ordene a lista em ordem alfabética, exiba o antes e o depois
for objeto in objetos:
    time.sleep(1)
    print(objeto)
print("")
time.sleep(1)
objetos.sort()
print(f"Os objetos em ordem alfabética são {objetos}")
print("")
time.sleep(1)

# 9- Acesse o primeiro e o último objeto e exiba eles
print(f"O primeiro objeto é {objetos[0]} e o último é {objetos[5]}.")
print("")
time.sleep(1)

# 10- Limpe toda a lista
objetos.clear()
print("A lista foi esvaziada")
print(objetos)


# Lista de números
idades = [5, 18, 1, 64]
maior_idade = max(idades)
print(f"Maior idade {max(idades)}")
print(f"Menor idade {min(idades)}")
print(f"Somas das idades {sum(idades)}")


