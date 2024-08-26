nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 9:
    print("Nota: A")
else:
    if nota >= 7:
        print("Nota: B")
    else:
        if nota >= 5:
            print("Nota: C")
        else:
            print("Nota: D")