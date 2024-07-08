'''Faça um algoritmo que imprima os 10 primeiros números primos.'''
conta_primos = 0
k = 0 

while conta_primos < 10:
    cont = 0  # flag de números não primos
    k += 1
    for i in range(2,k): # essa repetição irá verificar se há numeros entre 2 e k que o resto da divisão é 0, se houver ao menos 1 ocorrencia o número não é primo
        if(k % i == 0):
            cont =  1
            break
    if(cont == 0): #se o contador estiver zerado é por que o número é primo
        conta_primos = conta_primos + 1         
        print(f"Primos:{k} ")
    