#Calculo do valor líquido do salário com base no imposto de renda

salario = float(input("Qual o salário: "))
if salario <= 1900:
    ir = 0
else:
    if salario <= 2800:
        ir = salario * 0.15
    else:
        ir = salario * 0.275
sal_liq = salario - ir
print(f"IR: {ir:.2f}")
print(f"Salário líquido: {sal_liq:.2f}")