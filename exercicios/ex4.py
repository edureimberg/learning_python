salario = int(input("Informe o valor do salario: "))
aumento = int(input("Informe o valor do aumento em porcentagem: "))

print("O valor do salário é:", salario)
print("O valor do aumento é:", aumento)
print("O novo valor do salário é:", ((aumento / 100) + 1) * salario)
