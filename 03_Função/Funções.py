from datetime import datetime

def horario(batata):
    if datetime.now().hour <= 5:
        print(f"Boa madrugada, {batata}!")
    elif datetime.now().hour > 5 and datetime.now().hour <= 12:
        print(f"Bom dia, {batata}!")
    elif datetime.now().hour > 12 and datetime.now().hour <= 19:
        print(f"Boa tarde, {batata}!")
    elif datetime.now().hour > 19 and datetime.now().hour <= 24:
        print(f"Boa noite, {batata}!")