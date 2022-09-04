#Função com parâmetro
#Definir a média

def nota_valida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False

#Programa Principal

nota1 = float(input("Digite a primeira nota: "))
if (nota_valida(nota1)):
    nota2 = float(input("Digite a segunda nota: "))
    if (nota_valida(nota2)):
        media = (nota1 + nota2) / 2
        print("A média das notas {0} e {1} é de {2}".format(nota1, nota2, media))
    else:
        print("A nota 2 = {0} é inválida".format(nota2))
else:
    print("A nota 1 = {0} é inválida".format(nota1))

