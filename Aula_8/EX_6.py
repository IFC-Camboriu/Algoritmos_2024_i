''' 6) Faça um programa que receba o valor dos catetos de um triângulo,
 calcule e mostre o valor da hipotenusa.'''

cateto1 = int(input("Informe o valor do cateto 1: "))
cateto2 = int(input("Informe o valor do cateto 2: "))

hipotenusa = ((cateto1**2) + (cateto2**2))**0.5
print(f"O valor da hipotenusa é {hipotenusa:.2f}")