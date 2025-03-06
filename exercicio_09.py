# Exercícios
    # Números de Ponto Flutuante (float)
        # 09 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temp = float(input("Digite a temperatura em graus celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")