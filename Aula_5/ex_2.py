# Faça um programa que receba o valor de um depósito e o valor da taxa de juros anual, calcule e mostre o valor do rendimento e o valor total depois do rendimento (após 1 ano);

valor_deposito = float(input("Informe o valor de depósito: "))
valor_juros_anual = float(input("Informe a taxa de juros anual em porcentagem: "))

rendimento = valor_deposito * (valor_juros_anual/100)

print(f"O valor do rendimento é:{rendimento}")
print("O valor do rendimento é:", rendimento)
print(f"O valor total após 1 ano será de: {valor_deposito + rendimento}")