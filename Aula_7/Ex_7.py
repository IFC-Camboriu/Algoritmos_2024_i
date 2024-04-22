''' 7) Escreva um programa que pergunte a que velocidade do carro de um usuário. Caso o valor informado seja 
 maior que 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da 
 multa, cobrando R$ 5,00 por Km acima dos 80 km/h.'''

velocidade = int(input("Informe a velocidade atingida pelo carro do usuário: "))
limite = 80
multa = 5 * (velocidade - limite)

if velocidade > limite:
    print(f"Por atingir {velocidade} km/h, o usuário foi multado no valor de R$ {multa}")
else:
    print("O usuário não foi multado, pois não ultrapassou o limite de velocidade")