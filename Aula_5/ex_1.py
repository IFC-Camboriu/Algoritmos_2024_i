
#  Questao 1 - lista

#  Faça um programa que receba o salário base de um funcionário, calcule e mostre
#  o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre
#  o salário base e paga 7% de imposto também sobre o salário base;


salario_base = float(input("Informe o salario base do funcionário: "))

gratificacao = salario_base*(5/100)   # ou salario_base * 0,05
imposto = salario_base*(7/100)        # ou salario_base * 0,07

print(f'O salario final do funcionário é {salario_base + gratificacao - imposto}')
