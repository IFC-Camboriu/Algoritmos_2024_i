# Deseja-se estudar o perfil dos consumidores de energia elétrica de uma cidade, para um dado mês do ano. Para tanto, deverão ser lidos os seguintes dados para cada um dos n consumidores de uma amostragem (n deve ser solicitado ao usuário no início do programa):
#   ● consumo do mês, em kWh;
#   ● código do tipo de consumidor (1 para residencial, 2 para comercial e 3 para industrial);
# Antes de ler os dados dos consumidores, o preço do kWh deve ser fornecido ao programa. 
# Escrever  um que leia os dados indicados acima, calcule e imprima:
#   ● Para cada consumidor, o total a pagar;
#   ● O maior consumo verificado na amostra de consumidores;
#   ● O menor consumo verificado na amostra de consumidores;
#   ● O total do consumo para cada um dos três tipos de consumidores;

# Deseja-se estudar o perfil dos consumidores de energia elétrica de uma cidade, para um dado mês do ano. Para tanto, deverão ser lidos os seguintes dados para cada um dos n consumidores de uma amostragem (n deve ser solicitado ao usuário no início do programa):
#   ● consumo do mês, em kWh;
#   ● código do tipo de consumidor (1 para residencial, 2 para comercial e 3 para industrial);
# Antes de ler os dados dos consumidores, o preço do kWh deve ser fornecido ao programa. Escrever
# um que leia os dados indicados acima, calcule e imprima:
#   ● Para cada consumidor, o total a pagar;
#   ● O maior consumo verificado na amostra de consumidores;
#   ● O menor consumo verificado na amostra de consumidores;
#   ● O total do consumo para cada um dos três tipos de consumidores;

consu_t1 = 0
consu_t2 = 0
consu_t3 = 0
x = 1
preco = float(input("Insira o preço do kWh R$ "))
n = int(input("Quantos consumidores serão analisados? "))
print("")

if n <= 0:
    print("Dados digitados INVÁLIDOS!")
else:    
    # inicio
    while x <= n:
        consumo = float(input("Insira o consumo do mês (kWh): "))
        tipo = int(input("Insria o tipo de consumidor: (1) Residencial (2) Comercial (3) Industrial "))
        print("Consumidor ",x,"- consumo de ",consumo,"kWh")
        total = preco * consumo
        print("Total a pagar: R$ {:.2f}".format(total))
        print("")
        if x == 1:
            maior = consumo
            menor = consumo
        # Determinando maior consumo
        if consumo > maior:
            maior = consumo
        # Determinando menor consumo
        if consumo < menor:
            menor = consumo
        # Determinado total consumo por tipo
        if tipo == 1:
            consu_t1 = consu_t1 + consumo
        elif tipo == 2:
            consu_t2 = consu_t2 + consumo
        elif tipo == 3:
            consu_t3 = consu_t3 + consumo
        else:
            print("Tipo do consumidor INVÁLIDO!")
            continue
        x += 1
    # fim
    if tipo >= 1 and tipo <= 3:
        print("O menor consumo foi de: ",menor,"(kWh)")
        print("O maior consumo foi de: ",maior,"(kWh)")
        print("O total de consumo Residencial foi de: ",consu_t1,"kWh")
        print("O total de consumo Comercial foi de: ",consu_t2,"kWh")
        print("O total de consumo Industrial foi de: ",consu_t3,"kWh")
    else:
        print("Dados digitados INVÁLIDOS!")