# Exercícios
    # Booleanos (bool)
        # 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

expressao1_texto = input("Digite a primeira expressão booleana (True/False): ")
expressao2_texto = input("Digite a segunda expressão booleana (True/False): ")

# Converte as entradas do usuário para valores booleanos
# Considera 'True', 'true', 'T', 't' como verdadeiro
expressao1 = expressao1_texto.lower() in ['true', 't']
expressao2 = expressao2_texto.lower() in ['true', 't']

# Realiza a operação AND
resultado = expressao1 or expressao2

# Exibe o resultado
print(f"\nExpressão 1: {expressao1}")
print(f"Expressão 2: {expressao2}")
print(f"Resultado de {expressao1} OR {expressao2}: {resultado}")