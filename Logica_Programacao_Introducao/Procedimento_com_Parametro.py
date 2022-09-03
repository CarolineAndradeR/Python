#Subalgoritmo

def saudacao(usuario, hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print("Olá "+ usuario +", "+ msg +" você está logado")

#Algoritmo Principal

saudacao("Carol", 8)