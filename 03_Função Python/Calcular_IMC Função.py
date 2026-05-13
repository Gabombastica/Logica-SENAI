# Vamos praticar!
# Atividade 3- Calcular IMC (Índice de Massa Corporal)

def calcular_imc():
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura * altura)
    if imc <= 18.5:
        print(f"Você está na classificação 'Magro'!")
    elif imc > 18.5 and imc <= 24.9:
        print(f"Você está na classificação 'Normal'!")
    elif imc >= 25 and imc <= 29.9:
        print(f"Você está na classificação 'Sobrepeso'!")
    elif imc >= 30:
        print(f"Você está na classificação 'Obesidade'!")
        
calcular_imc()
     
