#Listas pode ter vários tipos na mesma lista

#         0   1    2    3
lista = [ 2, True, 4.5, "a"]
print(lista)

#Adicionar itens a lista
lista.append(45)
print(lista)

#Editando/inserindo um elemento existente
lista.insert(0,"b")
print(lista)

#Remover o último elemento da lista
lista.pop()
print(lista)

#Remover todos os elementos da lista
lista.clear()
print(lista)

#Adicionar dados a uma lista
lista = []
for cont in range(0,5,1):
     x = float(input("Digite um elemento: "))
     lista.append(x)
print(lista)

#Exibir valores da lista 1
#for i in range(0,5,1):
    #print(lista[i])

#Exibir valores da lista 2
for elem in lista:
    print(elem)

#Somando valores da lista
soma = 0
for elem in lista:
    soma += elem
print("\nsoma = ", soma)  #\n pula uma linha