atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite o ano de nascimento: "))

idade = atual - nascimento

if idade <= 3:
    print("bb")
else:
    if idade <= 11:
        print("criança")
    else:
        if idade <= 17:
            print("adolescente")
        else:
            if idade <= 64:
                print("adulto")
            else:
                print("idoso")