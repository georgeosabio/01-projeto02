# Exercícios
    # Strings (str)
        # 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

texto = str(input("Insira o texto: "))
text_after = texto.strip()
print(text_after)