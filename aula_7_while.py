valor = 10
while valor > 0:
    print(valor)
    valor = valor - 1

saque = -1
while saque <= 0 or saque > 600:
    print("Digite um valor entre 0 e 600: ")
    saque = int(input("Digite o valor a ser sacado: "))