nota = float(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("Valor inválido, digite um valor válido")
    nota = float(input("Digite uma nota  entre 0 e 10: "))