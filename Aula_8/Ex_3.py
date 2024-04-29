'''3) O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro 
do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço 
de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, 
calcule e mostre:
 a) O valor correspondente ao lucro do distribuidor;
 b) O valor correspondente aos impostos;
 c) O preço final do veículo;'''

preço_fabrica = float(input("Informe o preço de fábrica em reais: "))
lucro = float(input("Informe o percentual de lucro (Apenas números): "))
imposto = float(input("Informe o percentual de impostos (Apenas números): "))

lucro_parcial = (preço_fabrica * lucro) / 100
print(f"O lucro do distribuidor é de {lucro_parcial:.2f} reais")

imposto_parcial = (preço_fabrica * imposto) / 100
print(f"O valor dos impostos é de {imposto_parcial:.2f} reais")

preço_final = preço_fabrica + imposto_parcial + lucro_parcial
print(f"O preço final do veículo é de: {preço_final:.2f} reais")
