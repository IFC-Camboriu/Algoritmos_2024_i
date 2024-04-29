
'''8) Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação. 
Utilize a seguinte tabela como referência:
         Código                    Classificação
           1                   Alimento não-perecível
       2, 3 ou 4                 Alimento Perecível
         5 ou 6                      Vestuário
           7                      Higiene Pessoal
        8 até 15           Limpeza e Utensílios Domésticos
  Qualquer outro código              Inválido'''

codigo = int(input("Informe o código dos alimentos: "))

if codigo == 1:
    print("O produto é classificado como: Alimento não-perecível")
if codigo == 2 or codigo == 3 or codigo == 4:
    print("O produto é classificado como: Alimento Perecível")
if codigo == 5 or codigo == 6:
    print("O produto é classificado como: Vestuário")
if codigo == 7:
    print("O produto é classificado como: Higiene Pessoal")
if codigo >= 8 and codigo <= 15:
    print("O produto é classificado como: Limpeza e Utensílios Domésticos")
if codigo < 1 or codigo > 15:
    print("Código fornecido é inválido")