# Exercícios
    # Números de Ponto Flutuante (float)
        # 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Example usage
radius = float(input("Insira o raio do circulo: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")