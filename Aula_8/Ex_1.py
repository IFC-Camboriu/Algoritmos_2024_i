''' 1) Faça um programa que receba três notas, calcule e mostre a média ponderada dessas notas, considerando peso 3 
para a primeira nota, peso 2 para a segunda nota e peso 5 para a terceira nota.'''

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
peso1 = 3
peso2 = 2
peso3 = 5

media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"As notas são:{nota1}, {nota2} e {nota3}")
print(f"A média ponderada é: {media_ponderada:.2f}")