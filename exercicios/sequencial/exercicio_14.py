limite_peso = 50
multa_por_kg = 4

peso_peixe = float(input("Informe o peso total: "))

if peso_peixe > limite_peso:
    excedente = peso_peixe - limite_peso
    multa = excedente * multa_por_kg

    print("Houveram",excedente,"Kg de peixe a mais do permitido")
    print("O valor da multa é R$",multa)
else:
    print("Não foi maior que o permitido")
print("Fora da identação")