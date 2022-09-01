#Fazer a soma de 10 números

soma = 0
print("Digite 10 números: ")

for cont in range(1,11,1):
    n = float(input())
    soma = soma + n
print("A soma é: ", soma)