# Vamos praticar!
# Atividade 1- Mensagem automática
from datetime import datetime

def exibir_horario(nome):
    if datetime.now().hour <= 5:
        print(f"Boa madrugada, {nome}!")
    elif datetime.now().hour > 5 and datetime.now().hour <= 12:
        print(f"Bom dia, {nome}!")
    elif datetime.now().hour > 12 and datetime.now().hour <= 19:
        print(f"Boa tarde, {nome}!")
    elif datetime.now().hour > 19 and datetime.now().hour <= 24:
        print(f"Boa noite, {nome}!")


nome = input("Digite seu nome: ")
exibir_horario(nome)
