# 9) Construa um algoritmo para determinar se o indivíduo está com um peso favorável. Essa situação é 
# determinada através do IMC (Índice de Massa Corpórea), que é definida como sendo a relação entre o 
# peso (PESO) e o quadrado da Altura (ALTURA) do indivíduo. Ou seja,
# IMC = PESO/ALTURA²
# e a situação do peso é determinada pela tabela abaixo:
#         Condição             Situação
#      IMC abaixo de 20     Abaixo do peso
#      IMC de 20 até 25      Peso Normal
#      IMC de 25 até 30       Sobrepeso
#      IMC de 30 até 40         Obeso
#      IMC de 40 e acima     Obeso Mórbido

peso = float(input("Informe o peso da pessoa em quilos: "))
altura = float(input("Informe a altura da pessoa em metros: "))
imc = peso / altura**2
print(f"O IMC da pessoa é {imc:.2f}")

if imc < 20:
    print(f"Com IMC de {imc:.2f}, A pessoa está abaixo do peso")
if imc >= 20 and imc < 25:
    print(f"Com IMC de {imc:.2f}, A pessoa está com peso normal")
if imc >= 25 and imc < 30:
    print(f"Com IMC de {imc:.2f}, A pessoa está com sobrepeso")
if imc >= 30 and imc < 40:
    print(f"Com IMC de {imc:.2f}, A pessoa está com obesidade")
if imc >= 40:
    print(f"Com IMC de {imc:.2f}, A pessoa está com obesidade mórbida")
