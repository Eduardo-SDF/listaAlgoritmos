#Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado.
# Funcionários com até 1 ano de empresa, receberão aumento de 10%.
# Funcionários com mais de um ano de tempo de serviço, receberão aumento de 20%.

salario = float(input("Digite o salario atual: "))
tempo = int(input("Digite o tempo de serviço: "))

if tempo <= 1:
    aumento = 1.1
else:
    aumento = 1.2

reajuste = salario * aumento

print("Salario reajustado: ", reajuste)