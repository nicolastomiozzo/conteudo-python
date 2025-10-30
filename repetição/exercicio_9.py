from exercicios.sequencial.exercicio_6 import resultado

numero = int(input("Digite o valor do numero para fazer a tabuada: "))
while numero < 0 or numero > 10:
    print("Valor inválido")
    numero = int(input("Digite o valor do numero para fazer a taubuada : "))

for multiplicador in range(0,11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")