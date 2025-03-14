# Exercícios
    # Booleanos (bool)
        # 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expressao1_texto = input("Digite a primeira expressão booleana (True/False): ")
expressao2_texto = input("Digite a segunda expressão booleana (True/False): ")

# Converte as entradas do usuário para valores booleanos
# Considera 'True', 'true', 'T', 't' como verdadeiro
expressao1 = expressao1_texto.lower() in ['true', 't']
expressao2 = expressao2_texto.lower() in ['true', 't']

# Realiza a operação AND
resultado = expressao1 and expressao2

# Exibe o resultado
print(f"\nExpressão 1: {expressao1}")
print(f"Expressão 2: {expressao2}")
print(f"Resultado de {expressao1} AND {expressao2}: {resultado}")