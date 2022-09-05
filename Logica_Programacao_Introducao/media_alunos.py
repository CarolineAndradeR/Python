#Calcular a média semestral dos alunos, considerando as 2 maiores notas para calcular a média

#Verifica se a nota esta entre 0 e 10
def nota_valida(nota):
    if nota >= 0 and nota <=10:
        return True
    else:
        return False

#Valida qual a menor nota
def menor_nota (n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

#Definição da Média
def media (n1,n2,n3):
    menor = menor_nota(n1,n2,n3)
    return (n1 + n2 + n3 - menor) / 2

#Mensagem da Média do semestre
def msg_semestral(m):
    print(f"A sua Média Semestral é {m:.1f}")

#Média de 2 números
def media2n(n1, n2):
    return (n1 + n2) / 2

#Mensagem de aprovado ou nao no exame
def msg_aprovado_exame(m):
    if m < 5:
        return "Reprovado em exame com média " + str(m)
    else:
        return "Aprovado em exame com média " + str(m)


#Programa Principal
nota1 = float(input("Nota 1: "))
if nota_valida(nota1):
    nota2 = float(input("Nota 2: "))
    if nota_valida(nota2):
        nota3 = float(input("Nota 3: "))
        if nota_valida(nota3):
            media_semestral = media(nota1,nota2,nota3)
            msg_semestral(media_semestral)
            if media_semestral < 4:
                print("Você reprovou direto !")
            elif media_semestral >=7:
                print("Você foi aprovado direto !")
            else:
                print("Você está de exame !")
                nota_exame = float(input("Digite a nota do exame: "))
                if nota_valida(nota_exame):
                    media_exame = media2n(media_semestral,nota_exame)
                    print(msg_aprovado_exame(media_exame))
                else:
                    print(f"Nota Exame {nota_exame} inválida")
        else:
            print(f"Nota 3: {nota3} - É inválida!")
    else:
        print(f"Nota 2: {nota2} - É inválida!")
else:
    print(f"Nota 1: {nota1} - É inválida!")