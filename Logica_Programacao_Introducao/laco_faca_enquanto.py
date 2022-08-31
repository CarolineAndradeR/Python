#Fazer a soma até que um número negativo seja digitado

soma = 0

while True:
    num = int(input("Digite um número: "))
    if num >= 0:
        soma = soma + num
    else:
        break

print("O valor da soma é: ", soma)
