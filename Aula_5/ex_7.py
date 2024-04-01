
#  Questão 7 - lista

#  Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um
#  algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e
#  exibir quantos litros ele conseguiu colocar no tanque.

valor_gasolina = float(input("Informe o valor da gasolina: "))
valor_pagamento = float(input("Informe o valor do pagamento: "))

abastecimento = valor_pagamento / valor_gasolina

print(f'O motorista conseguiu abastecer {abastecimento:.2f} litros')