#Escolhendo sim ou não

opcao: str = input("Digite [S]im ou [N]ão: ")

while opcao != 'S' and opcao != 's' and opcao != 'n' and opcao != 'N':
    print("Você digitou", opcao, "escolha S ou N")
    opcao = input("Digite [S]im ou [N]ão: ")
print("Você digitou" , opcao)