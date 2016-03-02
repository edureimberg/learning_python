preco_inicial = int(input("Digite o valor do produto: "))
desconto = int(input("Digite o valor do desconto: "))

print("O valor do produto é:", preco_inicial)
print("O valor do desconto é:", desconto,"%")
print("O valor do produto com desconto é: ", preco_inicial * ((100 - desconto) / 100))
