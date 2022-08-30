#Rodízio de placas de carro

num_placa = int(input("Digite o número da placa: "))
final_placa = num_placa % 10

if final_placa in (1,2):
    print("Segunda-Feira")
elif final_placa in (3,4):
    print("Terça-Feira")
elif final_placa in (5,6):
    print("Quarta-Feira")
elif final_placa in (7,8):
    print("Quinta-Feira")
else:
    print("Sexta-feira")