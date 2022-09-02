#Exibir os multiplos até 10

n = int(input("Digite um número: "))

mult = 1
i = 1

while i <= 10:
    mult = n * i
    print(f"{n} X {i} = {mult}")
    i = i + 1
