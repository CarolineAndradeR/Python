#Selecionar o maior número

num = int(input("Digite 5 número: "))
maior = num
for cont in range(1,5,1):
    #mensagem acima
    num = int(input())
    if num > maior:
        maior = num
print("O maior número é: ", maior)