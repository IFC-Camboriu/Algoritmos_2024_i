# 6) Faça um programa que leia três valores inteiros fornecidos pelo usuário e exiba o maior e o menor dos valores lidos. Supor que não  sejam iguais.

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe um segundo número: "))
numero3 = int(input("Informe um terceiro número: ")) 

if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} é o maior entre os listados")
if numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é o maior entre os listados")
if numero3 > numero1 and numero3 > numero2:
    print(f"O número {numero3} é o maior entre os listados")

if numero1 < numero2 and numero1 < numero3:
    print(f"O número {numero1} é o menor entre os listados")
if numero2 < numero1 and numero2 < numero3:
    print(f"O número {numero2} é o menor entre os listados")
if numero3 < numero1 and numero3 < numero2:
    print(f"O número {numero3} é o menor entre os listados")