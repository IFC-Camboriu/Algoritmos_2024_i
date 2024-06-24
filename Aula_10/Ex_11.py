#Faça um programa que receba 15 números e imprima quantos números maiores que 30 foram digitados. 

quantidade = 0
c = 1
while c <= 15:
    n= float(input(f'Digite o {c} valor: '))
    c = c + 1
    if n > 30:
        quantidade += 1
        print(n)
print(f' Dos 15 Numeros {quantidade} sao maiores que 30. ')