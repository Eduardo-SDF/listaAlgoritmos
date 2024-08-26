#Ler um número inteiro e testar se o valor lido termina com 0 (divisível por 10). Em caso positivo,
# exiba a metade deste número. Caso contrário, exibir a mensagem "O número digitado não termina com 0".

numero = int(input("Digite um numero: "))

metade = numero / 2

if (numero % 10) == 0:
    print(metade)
else:
    print("O numero digitado nao termina em 0")