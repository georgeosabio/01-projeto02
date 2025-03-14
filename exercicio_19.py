# Exercícios
    # Booleanos (bool)
        # 19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os números
sao_iguais = numero1 == numero2

# Exibe o resultado
if sao_iguais:
    print(f"Os números {numero1} e {numero2} são iguais.")
else:
    print(f"Os números {numero1} e {numero2} são diferentes.")
