# Uma padaria vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pão custa R$ 0,50 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). Faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

nr_paes = int(input("Informe a quantidade de paes vendidos no dia: "))
nr_broas = int(input("Informe a quantidade de broas vendidas no dia: "))

valor_paes = nr_paes * 0.50
valor_broas = nr_broas * 1.50

valor_total = valor_paes + valor_broas

poupanca = valor_total * 0.10

print(f"Valor total arrecadado no dia: {valor_total}")
print(f"Valor a ser guardado: {poupanca}")