'''Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas. 
Exemplo: Nome = RAFAEL
Resultado gerado pelo programa: 
R
RA
RAF
RAFA
RAFAE
RAFAEL '''

nome = input("Informe seu nome: ")
nome = nome.upper()

for x in range(0, len(nome)+1, 1):
    print(nome[0:x:1])