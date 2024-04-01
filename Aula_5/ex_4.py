# Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.

saldo = 0
saldo = float(input("Informe o valor de deposito: "))
cpmf = 0.38/100
cheque_1 = float(input("Informe o valor do cheque_1: "))
cheque_2 = float(input("Informe o valor do cheque_2: "))

saldo_atual = saldo - (cheque_1 * cpmf) -(cheque_2 * cpmf)
saldo_atual = saldo_atual - cheque_1 - cheque_2

print(f"{saldo_atual:.2f}")