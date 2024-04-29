''' 8) Construa um algoritmo para determinar a situação (APROVADO/EXAME/REPROVADO) de um aluno, dado a sua 
 frequência (FREQ) (porcentagem de 0 a 100%) e sua nota (NOTA) (nota de 0.0 a 10.0), sendo que:
                      Condição                                   Situação
                Frequência até 75%                              Reprovado
      Frequência entre 75% e 100% e Nota até 3.0                Reprovado
      Frequência entre 75% e 100% e Nota de 3.0 até 7.0           Exame
      Frequência entre 75% e 100% e Nota entre 7.0 e 10.0        Aprovado
'''

nota = float(input("Informe a nota do aluno: "))
frequencia = int(input("Informe a frequência do aluno: "))

if frequencia < 75:
    print("O aluno foi reprovado por ter uma frequência menor que 75%")
if (frequencia >= 75 and frequencia <= 100) and nota < 3.0:
    print("O aluno foi reprovado por ter uma nota menor que 3.0")
if (frequencia >= 75 and frequencia <= 100) and (nota >= 3.0 and nota < 7.0):
    print("O aluno ficou em exame por ter uma nota menor que 7.0")
if (frequencia >= 75 and frequencia <= 100) and (nota >= 7.0 and nota <= 10.0):
    print("O aluno foi aprovado")

if(frequencia > 100 or nota > 10.0):
    print("Informe valores válidos de entrada")