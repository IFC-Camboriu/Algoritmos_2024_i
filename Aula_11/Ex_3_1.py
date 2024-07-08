fatorial = 1

numero = int(input("Informe um valor para ser calculado o fatorial "))

for i in range(numero, 1, -1):
    print(f"I = {i}")
    fatorial = fatorial * i

print(f"O valor do fatorial é: {fatorial}")