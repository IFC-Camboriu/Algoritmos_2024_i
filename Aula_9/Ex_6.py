'''O Hipermercado X está com uma promoção de carnes que é imperdível. Confira:
 Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 24,90 por Kg          R$ 25,80 por Kg
Alcatra         R$ 35,90 por Kg          R$ 36,80 por Kg
Picanha         R$ 56,90 por Kg          R$ 57,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão X o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

tipo_carne = int(input("Digite o tipo de carne (1 - File Duplo,  2 - Alcatra, 3 - Picanha): "))
quantidade = float(input("Digite a quantidade de carne em Kg: "))

# Solicita o tipo de pagamento
tipo_pagamento = input("A compra será feita no cartão X? (s/n): ")

# Determina o preço por Kg com base na quantidade comprada
if tipo_carne == 1: # File Duplo
    if quantidade <= 5:
        preco_por_kg = 24.90
    else:
        preco_por_kg = 25.80
elif tipo_carne == 2: # Alcatra
    if quantidade <= 5:
        preco_por_kg = 35.90
    else:
        preco_por_kg = 36.80
elif tipo_carne == 3: # Picanha
    if quantidade <= 5:
        preco_por_kg = 56.90
    else:
        preco_por_kg = 57.80
else:
    print("Tipo de carne inválido!")
    # para sair do programa
    exit()

# Calcula o preço total
preco_total = preco_por_kg * quantidade

# Calcula o desconto se o pagamento for no cartão X
if tipo_pagamento.lower() == 's': # lower converte a string de entrada para minúsculo
    desconto = 0.05 * preco_total
else:
    desconto = 0

# Calcula o valor a pagar
valor_a_pagar = preco_total - desconto

# Gera o cupom fiscal
print("\n----- CUPOM FISCAL -----")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço por Kg: R$ {preco_por_kg:.2f}")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {'Cartão X' if tipo_pagamento.lower() == 's' else 'Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")