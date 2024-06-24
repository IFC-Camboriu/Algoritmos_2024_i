"""Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e seu somatório. 
Suponha que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor é menor que o segundo. """

inf = int(input('Informe o limite inferior:'))
sup = int(input('Informe o limite superior:'))
soma_par = 0
inf = inf + 1 # intervalo aberto não inclui os valores informados

while inf < sup:
    if inf % 2 == 0:
        print(inf)
        soma_par = soma_par + inf
    inf = inf + 1

print(f'A soma de todos os valores pares é {soma_par}')
