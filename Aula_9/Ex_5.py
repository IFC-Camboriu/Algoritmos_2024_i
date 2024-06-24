'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

valor = int(input("Informe o valor a ser resgatado:"))

if(valor > 600 or valor < 10):
    print("Valor inválido para resgate!")
else:
    cont_100 = valor // 100
    resto = valor % 100
    cont_50 = resto // 50
    resto = resto % 50
    cont_10 = resto // 10
    resto = resto % 10
    cont_5 = resto // 5
    resto = resto % 5
    cont_1 = resto // 1
    print(f"Você resgatará:\n{cont_100} notas de 100,\n{cont_50} notas de 50,\n{cont_10} notas de 10,\n{cont_5} notas de 5,\n{cont_1} notas de 1")
    