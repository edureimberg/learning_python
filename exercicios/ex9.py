dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = int(input("Digite a quilometragem percorrida: "))

preco_total = (60 * dias) + float(0.15 * km)

print("O total a ser pago pelo aluguel do carro é:", preco_total)
