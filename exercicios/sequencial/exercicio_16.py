import math

area = float(input("Informe a area a ser pintada: "))

cob_por_metro = 3
qtd_tinta_lata = 18
valor_lata = 80

litros_necessarios = area / cob_por_metro
print("São necessarios",litros_necessarios,"l de tinta")

qtd_latas = litros_necessarios / qtd_tinta_lata
print("São necessarios",qtd_latas,"latas de tinta")

print("### Com o valor exato ###")
valor = qtd_latas * valor_lata
print("O valor necessario de tinta, é R$",round(valor,2))

print("### Com quantidades inteiras de latas ###")
qtd_latas = math.ceil(qtd_latas)
print("São necessarios",qtd_latas,"latas de tinta")
valor = qtd_latas * valor_lata
print("O valor necessario de tinta, é R$",valor)