#aumento de salário com base no tempo de casa

tempo_casa = int(input("Digite o tempo de casa:"))
valor_salario = float(input("Digite o salário:"))

if tempo_casa < 3:
    aumento = valor_salario * 0.05
else:
    aumento = valor_salario * 0.10
novo_salario = valor_salario + aumento
print("O novo salário é: ", novo_salario)