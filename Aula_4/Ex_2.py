'''Declare as seguintes variáveis: nome do funcionario, anoNascimento, numero
de filhos, rg, salario, ativo. Atribua valores às respectivas variáveis. A variável
ativo deverá receber um valor lógico. Mostre os dados conforme exemplo abaixo:'''

nome = input("Informe o nome do Funcionário: ")
ano_nasc = int(input("Informe o ano de nascimento do funcionário: "))
numero_filhos = int(input("Informe o número de filhos do funcionário:"))
rg = input("Informe seu RG: ")
salario = float(input("Informe o valor do salário: "))
ativo = bool(input("Infome a situação do funcionário: "))

print(f"O funcionário {nome} com rg {rg} possui {2024 - ano_nasc} anos de vida. \n O salario do funcionario {nome} é de R$ {salario} e possui {numero_filhos} filhos. \n Situação ativo:{ativo}")