tempo = float(input("Tempo em anos que os fundos foram mantidos em depósito: "))

if tempo >= 5:
    print("0,95")
else:
    if tempo >= 4:
        print("0,90")
    else:
        if tempo >= 3:
            print("0,85")
        else:
            if tempo >= 2:
                print("0,75")
            else:
                if tempo >= 1:
                    print("0,65")
                else:
                    print("0,55")