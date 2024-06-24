"""Um cinema possui capacidade de 20 lugares e está sempre com ocupação total. Certo dia, cada espectador respondeu a um questionário, em que constava: 
sua idade; 
sua opinião em relação ao filme, segundo as seguintes notas: 

Nota Significado
A Ótimo
B Bom
C Regular
D Ruim
E Péssimo

 Elabore um algoritmo que, lendo estes dados, calcule e imprima: 
a quantidade de respostas ótimo; 
a diferença percentual entre respostas bom e regular; 
a média de idade das pessoas que responderam ruim; 
a percentagem de respostas péssimo e a maior idade que utilizou esta opção; 
a diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim. 
"""
x = 0
quant_a = 0
quant_b = 0
quant_c = 0
quant_d = 0
quant_e = 0
soma_idade = 0
maior_p = 0
maior_a = 0
maior_d = 0

while x < 20:
    idade = int(input("Informe a sua idade: "))
    opiniao = input("Informe a sua opiniao sobre o filme: A - Ótimo, B - Bom, C - Regular, D - Ruim, E - Péssimo ")
    
    if opiniao == 'A' or opiniao == 'a':
        quant_a = quant_a + 1
        if maior_a < idade:
            maior_a = idade
    elif opiniao == 'B' or opiniao == 'b':
        quant_b = quant_b + 1
    elif opiniao == 'C' or opiniao == 'c':
        quant_c = quant_c + 1
    elif opiniao == 'D' or opiniao == 'd':
        quant_d = quant_d + 1
        soma_idade = soma_idade + idade
        if maior_d < idade:
            maior_d= idade
    elif opiniao == 'E' or opiniao == 'e':
        quant_e = quant_e + 1
        if maior_p < idade:
            maior_p= idade
        
    else:
        print("Opinião Inválida!")
    x = x + 1

print(f"A quantidade de opiniões ótimo é:{quant_a}")

if quant_b > quant_c:
    perce = (quant_b - quant_c)/(quant_c * 100)
else:
    perce = (quant_c - quant_b)/(quant_b * 100)
print(f"A diferença percentual entre bom e regular é:{perce}")

if quant_d > 0:
    print(f"A média da idade das pessoas que responderam ruim é:{soma_idade/ quant_d}")
else:
    print("Nenhuma avaliação ruim!")

if quant_e > 0:
    print(f"A percentagem de respostas péssimo é :{(quant_e * 100) / 20}")
    print(f"A maior idade de quem optou por péssimo é :{maior_p}")
else:
    print("Nenhuma avaliação Péssimo!")

print(f"A diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim é {maior_a - maior_d} ")