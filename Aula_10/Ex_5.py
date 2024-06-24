#Escreva um algoritmo que receba cinco números do usuário e imprima o cubo de cada número. 

contador = 0

while contador < 5:
    n = int(input(f'Digite um número: '))
    print(f"O cubo do valor informado é: {n ** 3}")
    contador = contador + 1