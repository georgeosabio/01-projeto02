# Exercícios
    # Strings (str)
        # 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data no formato dd/mm/aaaa: ")

# Separa a data em partes usando o caractere '/' como delimitador
partes = data.split('/')

# Extrai cada componente
dia = partes[0]
mes = partes[1]
ano = partes[2]

# Imprime os componentes separadamente
print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")
