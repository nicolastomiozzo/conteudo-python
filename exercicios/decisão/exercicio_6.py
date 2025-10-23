numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segunto número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior é o número",numero1)
elif numero2 > numero3:
    print("O maior é o número",numero2)
else:
    print("O maior é o número",numero3)