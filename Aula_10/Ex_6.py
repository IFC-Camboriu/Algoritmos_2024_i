# Criar um algoritmo que imprima todos os números de 1 até 100, e a soma de todos eles (intervalo fechado). 


contador = 1 # controla o estrutura de repetição
acumulador = 0 # mantem a soma armazenada

while contador < 101:
    print(contador)
    acumulador = acumulador + contador
    contador = contador + 1

print(f"A soma total é: {acumulador}")