# Faça um programa que leia dez números inteiros e imprima o maior e o menor número.

n = int(input('Digite um número:'))

contador = 1
maior = n
menor = n

while contador < 10:
    n = int(input('Digite um número: '))
    
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    contador += 1

print(f'O maior eh {maior}')
print(f'O menor eh {menor}')