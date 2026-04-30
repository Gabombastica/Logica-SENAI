import time

celular1 = {}
celular1["modelo"] = input("Digite o modelo do seu celular: ")
celular1["marca"] = input("Digite a marca dele: ")
celular1["processador"] = input("Digite o processador: ")
celular1["taxa_de_atualização"] = input("Digite a taxa de atualização: ")
celular1["android"] = input("Digite o android do seu celular: ")

# Exibir os dados do Dicionário em forma de lista
print("")
for chave, valor in celular1.items():
    print(f"{chave} - {valor}")
    time.sleep(1)
    