# 10) A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um 
# algoritmo que receba a idade de um nadador e determine (imprima) a sua categoria segundo a tabela a seguir:
#       Categoria         Idade
#      Infantil A       5 - 7 anos
#      Infantil B       8 - 10 anos
#      Juvenil A       11 - 13 anos
#      Juvenil B       14 - 17 anos
#       Senior      Maiores de 18 anos

idade = int(input("Informe a idade do nadador: "))

if idade < 5:
    print("Idade inválida para a competição")
if(idade >= 5 and idade < 8):
    print("Infantil A")
if(idade >= 8 and idade < 11):
    print("Infantil B")
if(idade >= 11 and idade < 14):
    print("Juvenil A")
if(idade >= 14 and idade < 18):
    print("Juvenil B")
if(idade >= 18 ):
    print("Senior")