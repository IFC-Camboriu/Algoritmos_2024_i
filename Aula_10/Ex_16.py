"""Os professores da disciplina Algoritmos do IFC- Camboriú necessitam de um programa capaz de calcular as médias de cada aluno. Para cada aluno, a média semestral é calculada por: 

ms = 0.3 x AV1 + 0.3 x AV2 + 0.4 x mt
onde AV1 e AV2 são, respectivamente, a primeira e a segunda avaliação e mt é a média aritmética dos 4 trabalhos, t1, t2, t3 e t4. O número de alunos (N) deve ser lido no início do programa. Caso a média de um aluno seja inferior a 7, informar que o mesmo está em recuperação final, caso contrário mostrar aprovado.
"""

quant_alunos = int(input('Informe a quantidade de alunos: '))
x = 0

while x < quant_alunos:
    av1 = float(input("Informe a nota da avaliação 1: "))
    av2 = float(input("Informe a nota da avaliação 2: "))
    mt = float(input("Informe a média das notas dos trabalhos: "))
 
    media = ((av1 * 0.3) + (av2 * 0.3) + (mt * 0.4))
    if media < 7:
        print("O estudante está em recuperação final!")
    else:
        print("O estudante está aprovado!")
    x = x + 1