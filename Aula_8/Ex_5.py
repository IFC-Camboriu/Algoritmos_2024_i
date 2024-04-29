''' 5) João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar
 multa  de 2% sobre cada conta. Faça um programa que lê o valor do salário, das duas contas e calcule e 
 mostre quanto restará do salário de João.'''

multa = 0.02

salario = float(input("Informe o salário de João: "))
print(f"João recebe {salario} reais!")

conta1 = float(input("Informe o valor da primeira conta a pagar: "))

conta2 = float(input("Informe o valor da segunda conta a pagar: "))

resto_salario = salario - ((conta1 + (multa * conta1)) + (conta2 + (multa * conta2)))
print(f"Após pagar as contas sobrará: {resto_salario:.2f} reais ")