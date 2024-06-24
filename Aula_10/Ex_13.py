cont = 0 #contador da estrutura de repetição
soma_alturas = 0 # Acumulador
soma_alt_mulher = 0 # Acumulador
quant_mulher = 0 # contador
while cont < 5:
    altura = float(input("Informe a altura da pessoa: "))
    sexo = int(input("Informe o Sexo 1-M e 2-F"))
    # salvo a soma de todas as alturas informadas
    soma_alturas = soma_alturas + altura
    # inicializando a menor e a menor altura
    if cont == 0:
        maior_altura = altura
        menor_altura = altura
    # obtem a maior altura informada
    if maior_altura < altura:
        maior_altura = altura
    # obtem a menor altura informada    
    if menor_altura > altura:
        menor_altura = altura
    # se mulheres
    if sexo == 2:
        soma_alt_mulher = soma_alt_mulher + altura
        quant_mulher = quant_mulher + 1
    cont = cont + 1

media_turma = soma_alturas/cont
if(quant_mulher > 0):
    media_altura_mulheres = soma_alt_mulher/quant_mulher
else:
    media_altura_mulheres = 0
    
print("A maior altura é:", maior_altura)
print("A menor altura é:", menor_altura)
print("A média da altura da turma é:", media_turma)
print("A média da altura das mulheres é:", media_altura_mulheres)