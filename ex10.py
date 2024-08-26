#Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido.
# Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa,
# o algoritmo deverá escrever "Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado".

salario = float(input("Digite o valor do salario: "))
financiamento = float(input("Valor da solicitação financiamento: "))

solicitacao = salario * 5

if financiamento <= solicitacao:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")