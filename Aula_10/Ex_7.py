#Criar um algoritmo que imprima todos os números de 1 até 10, e a média geral todos eles (intervalo fechado). 

contador = 1 # controla o estrutura de repetição
acumulador = 0 # mantem a soma armazenada

while contador < 11:
    print(contador)
    acumulador = acumulador + contador
    contador = contador + 1

print(f"A soma total é: {acumulador}")
print(f"A média geral é: {acumulador/(contador - 1)}")