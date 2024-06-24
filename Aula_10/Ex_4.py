#Escreva um algoritmo que leia dez números do usuário e imprima a metade de cada número. 

contador = 0 # controla o estrutura de repetição

while contador < 10:
    n = int(input(f'Digite um número: '))
    print(f"A metade do valor informado é: {n/2}")
    contador = contador + 1