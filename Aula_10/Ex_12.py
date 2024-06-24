#Faça um programa que leia 20 números e imprima a soma dos positivos e o total de números negativos.

contaNeg, somaPos = 0, 0 
c = 0

while c < 20:
    num = float(input(f'Digite um número [{c} de 20]: '))
    if num > 0: 
        somaPos += num 
        print(f'[Número positivo!] Soma = {somaPos}.')
    else: 
        contaNeg += 1 
        print(f'[Número negativo] Qtde Neg = {contaNeg}.')
    c += 1
print(f'A soma total dos positivos foi: {somaPos:.2f}.') 
print(f'Foram digitados {contaNeg} números negativos.') 