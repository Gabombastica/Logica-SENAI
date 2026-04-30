# Vamos praticar!
# Atividade 2- Conversor de Temperatura
def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def converter_celsius_para_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin

celsius = float(input("Digite qualquer temperatura em C°: "))
converter_celsius_para_fahrenheit(celsius)
converter_celsius_para_kelvin(celsius)
print(f"A conversão de C° para Fahrenheit é de {converter_celsius_para_fahrenheit(celsius)}")
print(f"A conversão de C° para Kelvin é de {converter_celsius_para_kelvin(celsius)}")
    
