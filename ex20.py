valor1 = int(input("Digite o primeiro valor (entre 1 e 10): "))
valor2 = int(input("Digite o segundo valor (entre 1 e 10): "))

soma = valor1 + valor2

if soma < 8:
    media = (valor1 + valor2) / 2
    print("A média dos números é: ", media)

if soma == 8:
    produto = valor1 * valor2
    print("O produto dos números é: ", produto)

if soma > 8:
    maior = valor1
    menor = valor2
    if valor2 > valor1:
        maior = valor2
        menor = valor1

    divisao = maior / menor
    print("A divisão do maior pelo menor é: ", divisao)