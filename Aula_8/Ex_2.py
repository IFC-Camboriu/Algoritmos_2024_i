'''2) Faça um programa que receba o ano de nascimento de uma pessoa, calcule e mostre:
 a) Se ele já tem idade para votar (16 anos ou mais);
 b) E para conseguir carteira de habilitação (18 anos ou mais);'''

ano_nasc = int(input("Informe o ano de nascimento: "))
idade = 2024 - ano_nasc 

if idade >= 16:
    print("Você já pode votar")
else:
    print("Você não pode votar")

if idade >= 18:
    print("Você já pode ter habilitação")
else:
    print("Você não pode ter habilitação")
    