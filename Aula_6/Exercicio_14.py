
    # Questão 14 - Lista 2

#   A granja Frangotech possui um controle automatizado
#   de cada frango da sua produção. No pé direito do 
#   frango há um anel com um chip de identificação; no 
#   pé esquerdo são dois anéis para indicar o tipo de
#   alimento que ele deve consumir. Sabendo que o anel
#   com chip custa R$4,00 e o anel de alimento custa 
#   R$3,50 cada, faça um algoritmo para calcular o gasto
#   total da granja para marcar todos os seus frangos.

quant_frango = int(input("Digite a quantidade de frango: "))
VALOR_CHIP = 4.00
VALOR_COMIDA = 3.50

custo = (VALOR_CHIP +(VALOR_COMIDA * 2)) * quant_frango

print(f'O valor das total das pulseiras para {quant_frango} frangos é {custo}')
