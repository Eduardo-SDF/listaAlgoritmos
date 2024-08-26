#Ler um número e informar se ele é positivo, negativo ou neutro (zero).

numero = int(input("digite um numero: "))

if numero == 0:
    print("neutro")
else:
    if numero < 0:
        print("negativo")
    else:
        print("positivo")

