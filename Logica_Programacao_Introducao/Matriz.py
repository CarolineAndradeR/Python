#Manipulando matrizes

matriz = [ [0,0], [0,0], [0,0], [0,0]]

#Preenchimento dos dados da matriz
for l in range(4):
    for c in range(2):
        matriz[l][c] = int(input(f"Matriz[{l}][{c}]= "))

#Exibir dos dados da matriz
print("\nExibindo a Matriz...")
for l in range(4):
    for c in range(2):
        print(f"{matriz[l][c]}\t", end = "") #\t tabulação

#Somando os valores
soma = 0
for l in range(4):
    for c in range(2):
        soma += matriz[l][c]
print("\nSoma = ", soma)
