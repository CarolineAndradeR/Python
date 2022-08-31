#Somar de votos de cada participante
hug = 0
zez = 0
lui = 0

print("Digite o voto ou 0 para finalizar")
print("1 – Huguinho")
print("2 – Zezinho")
print("3 – Luizinho")
print("0 – Terminar a votação")

while True:
    voto = int(input("Digite o voto: "))
    if voto == 1:
        hug = hug + 1
    elif voto == 2:
        zez = zez + 1
    elif voto == 3:
        lui = lui + 1
    else:
        if voto != 0:
            print("Voto inválido, digite: 1, 2 ou 3")
    if voto == 0:
        break

print(f"1 – Huguinho: {hug} votos")
print(f"2 – Zezinho: {zez} votos")
print(f"3 – Luizinho: {lui} votos")



