num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

codigo = int(input("Digite o código de seleção (1 para adição, 2 para multiplicação, 3 para divisão): "))

if codigo == 1:
    print(num1 + num2)
else:
    if codigo == 2:
        print(num1 * num2)
    else:
        if codigo == 3:
            print(num1 / num2)
        else:
            print("Código inválido.")