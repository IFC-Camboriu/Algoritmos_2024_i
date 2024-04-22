# 10) A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um 
# algoritmo que receba a idade de um nadador e determine (imprima) a sua categoria segundo a tabela a seguir:
#       Categoria         Idade
#      Infantil A       5 - 7 anos
#      Infantil B       8 - 10 anos
#      Juvenil A       11 - 13 anos
#      Juvenil B       14 - 17 anos
#       Senior      Maiores de 18 anos

idade = int(input("Informe a idade do nadador: "))

if idade >= 5 and idade <=7:
    print(f"Com {idade} anos, O nadador pertence à categoria Infantil A")
if idade >= 8 and idade <= 10:
    print(f"Com {idade} anos, O nadador pertence à categoria Infantil B")
if idade >= 11 and idade <= 13:
    print(f"Com {idade} anos, O nadador pertence à categoria Juvenil A")
if idade >= 14 and idade <= 17:
    print(f"Com {idade} anos, O nadador pertence à categoria Juvenil B")
if idade > 17:
    print(f"Com {idade} anos, O nadador pertence à categoria Senior")