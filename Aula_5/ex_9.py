# Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um algoritmo para ler uma temperatura Celsius e imprimi-la em Fahrenheit (pesquise como fazer este tipo de conversão).

graus_c = float(input("Informe a temperatura em graus celsius: "))

graus_f = (graus_c * 9/5) + 32

print(graus_f)