
    # Questão 15 - Lista 2


#   Faça um programa que leia o nome de um aluno e duas notas, 
#   calcule e mostre a média ponderada dessas notas, considerando
#   peso 2 para a primeira nota e peso 3 para a segunda nota.

nome = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a nota 1 (peso 2): "))
nota_2 = float(input("Digite a nota 2 (peso 3): "))
peso1 = 2
peso2 = 3

media = ((nota_1 * peso1) + (nota_2 * peso2)) / (peso1 + peso2)

print(f'A media ponderada do aluno {nome} é {media}')
