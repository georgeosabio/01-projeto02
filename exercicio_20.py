# Exercícios
   # Booleanos (bool)
        # 20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os números
sao_diferentes = numero1 != numero2

# Exibe o resultado
if sao_diferentes:
    print(f"Os números {numero1} e {numero2} são diferentes.")
else:
    print(f"Os números {numero1} e {numero2} são iguais.")