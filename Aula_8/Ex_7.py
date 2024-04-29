''' 7) Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual 
e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir:
         Código         Cargo       Percentual de Aumento
           1         Escrituário            50%
           2         Secretário             35%
           3            Caixa               20%
           4           Gerente              10%
           5           Diretor        Não tem aumento'''

codigo = int(input("Informe o código do cargo: "))

salario = float(input("Informe o salário do cargo: "))

if codigo == 1:
    print(f"O salário de um escrituário é: {salario}")
    aumento = 0.5 * salario
    print(f"O salário do funcionário teve um aumento de: {aumento} reais")
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário passou a ser {novo_salario}")

if codigo == 2:
    print(f"O salário de um secretário é: {salario}")
    aumento = 0.35 * salario
    print(f"O salário do funcionário teve um aumento de: {aumento} reais")
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário passou a ser {novo_salario}")

if codigo == 3:
    print(f"O salário de um caixa é: {salario}")
    aumento = 0.2 * salario
    print(f"O salário do funcionário teve um aumento de: {aumento} reais")
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário passou a ser {novo_salario}")

if codigo == 4:
    print(f"O salário de um gerente é: {salario}")
    aumento = 0.1 * salario
    print(f"O salário do funcionário teve um aumento de: {aumento} reais")
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário passou a ser {novo_salario}")
    
if codigo == 5:
    print(f"O salário de um diretor é: {salario}")
    aumento = 0.0 * salario
    print(f"O salário do funcionário teve um aumento de: {aumento} reais")
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário passou a ser {novo_salario}")

if(codigo < 1 or codigo > 5):
    print("Codigo informado inválido!")