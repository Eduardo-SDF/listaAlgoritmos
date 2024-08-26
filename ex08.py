#Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade.
# A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos),
# adolescente (12 a 17 anos), adulta (18 a 64 anos) ou idosa (65 anos em diante).

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