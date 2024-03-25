# Faça um algoritmo que realize a leitura de 2 números e ao final mostre a troca entre os dois números :

# A=5 e B=3
# Ao final

# A=3 e B=5

a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))

aux = a
a = b
b = aux

print("A:", a)
print("B:", b)