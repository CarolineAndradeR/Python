#Retorna o maior número

def definindo_maior(numero1, numero2):
    if numero1 > numero2:
        maior = numero1
    else:
        maior =  numero2
    return maior

#Programa Principal

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print("O maior número é", definindo_maior(numero1, numero2))