
    # Questão 12 - Lista 2

#   Elabore um algoritmo que leia o nome e o ano de
#   nascimento de uma pessoa e mostre qual é a sua
#   idade atual. 

nome = input("Digite seu nome: ")
dt_nasc = int(input("Digite seu ano de nascimento: "))

idade = 2024 - dt_nasc

print(f' {nome} você tem {idade} anos')
