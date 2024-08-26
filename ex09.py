#Informar o número do mês do ano e mostrar o nome do mês por extenso.
# Caso o número do mês não exista, exibir a mensagem "Mês inválido".

mes = int(input("Digite o número do mês do ano: "))

if mes == 1:
    print("janeiro")
else:
    if mes == 2:
        print("fevereiro")
    else:
        if mes == 3:
            print("março")
        else:
            if mes == 4:
                print("abril")
            else:
                if mes == 5:
                    print("maio")
                else:
                    if mes == 6:
                        print("junho")
                    else:
                        if mes == 7:
                            print("julho")
                        else:
                            if mes == 8:
                                print("agosto")
                            else:
                                if mes == 9:
                                    print("setembro")
                                else:
                                    if mes == 10:
                                        print("outubro")
                                    else:
                                        if mes == 11:
                                            print("novembro")
                                        else:
                                            if mes == 12:
                                                print("dezembro")
                                            else:
                                                print("Mês inválido")