# 5) Crie um algoritmo que leia um número, verifique e mostre se o número lido é par.

numero = int(input("Informe o número: "))

if (numero % 2 == 0):
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")