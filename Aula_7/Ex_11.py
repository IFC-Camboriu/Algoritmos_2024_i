# 11) Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir, construa um algoritmo que 
# leia o valor da compra e informe ao comerciante qual o lucro obtido sobre aquela compra.
#           Valor da Compra                 Valor da Venda
#           Valor < R$ 10,00                 Lucro de 70%
#      R$ 10,00 <= Valor < R$ 30,00          Lucro de 50%
#      R$ 30,00 <= Valor < R$ 50,00          Lucro de 40%
#           Valor >= R$ 50,00                Lucro de 30%

valor = float(input("Informe o valor da compra: "))

if valor < 10:
    print(f"Com o valor da compra em {valor} reais, o comerciante arrecadou um lucro de 70%")
    print(f"O valor do lucro é:{ (valor * 0.7) }")
if valor >= 10 and valor < 30:
    print(f"Com o valor da compra em {valor} reais, o comerciante arrecadou um lucro de 50%")
    print(f"O valor do lucro é:{ (valor * 0.5) }")
if valor >= 30 and valor < 50:
    print(f"Com o valor da compra em {valor} reais, o comerciante arrecadou um lucro de 40%")
    print(f"O valor do lucro é:{ (valor * 0.4) }")
if valor >= 50:
    print(f"Com o valor da compra em {valor} reais, o comerciante arrecadou um lucro de 30%")
    print(f"O valor do lucro é:{ (valor * 0.3) }")