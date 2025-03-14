# Exercícios
    # Booleanos (bool)
        # 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# Solicita o valor booleano ao usuário
entrada = input("Digite um valor booleano (True/False): ")

# Converte a entrada para valor booleano
# Aceita variações como 'True', 'true', 'T', 't'
valor_booleano = entrada.lower() in ['true', 't', '1', 'sim', 's', 'yes', 'y']

# Inverte o valor booleano usando o operador 'not'
valor_invertido = not valor_booleano

# Exibe os resultados
print(f"\nValor original: {valor_booleano}")
print(f"Valor invertido: {valor_invertido}")