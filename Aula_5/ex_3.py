# Sabe-se que:
# 1 Pé =12 polegadas
# 1 jarda = 3 pés
# 1 milha = 1.760 jardas
# Faça um programa que receba uma medida em pés, faça as conversões e a seguir mostre os resultados em:
# Polegadas
# Jardas
# Milhas

#entrada
pes = float(input("Infome o valor em pés:"))

#processamento
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

#saída
print(f"O valor em polegadas é: {polegadas}")
print(f"O valor em jardas é: {jardas:.3f}")
print(f"O valor em milhas é: {milhas:.2f}")