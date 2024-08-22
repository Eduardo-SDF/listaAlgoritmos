salario = float(input("Digite o salario atual: "))
tempo = int(input("Digite o tempo de serviço: "))

if tempo <= 1:
    aumento = 1.1
else:
    aumento = 1.2

reajuste = salario * aumento

print("Salario reajustado: ", reajuste)