''' 4) Pedro comprou um saco de ração, com peso em quilos. Ele possui dois gatos, para os quais fornece a 
quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma.
Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, 
calcule e mostre quanto restará de ração no saco após 5 dias de consumo.'''

peso = float(input("Informe o peso do saco da ração (em quilos): "))
racao = float(input("Informe a quantidade de ração diária que cada gato consome (em gramas): "))

# convertendo gramas em quilos, considerando os cinco dias
consumo = (5 * ((2 * racao)/1000))
resto_racao = peso - consumo
print(input(f"Após cinco dias sobrou {resto_racao:.2f} quilos de ração."))