#Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho
# (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado,
# reprovado ou se fará prova final. O aluno será reprovado se faltou mais de 15 aulas.
# Será aprovado se não for reprovado por falta e sua média for maior ou igual a 6,0.
# Caso tenha média menor, deverá fazer prova final.
# O cálculo da média deve ser feito com peso 3 para a primeira prova, 5 para a segunda prova e 2 para o trabalho.

nome = input("Nome do aluno: ")
prova1 = float(input("Prova 1: "))
prova2 = float(input("Prova 2: "))
trabalho = float(input("Trabalho: "))
frequencia = int(input("Faltas: "))

if frequencia > 15:
    print("Reprovado")
else:
    media = (prova1 * 3 + prova2 * 5 + trabalho * 2) / 10

    if media >= 6:
        print("Aprovado")
    else:
        print("Prova final")
