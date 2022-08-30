#Caculadora
operador = input("Qual o operador ( + - * / ): ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = numero1 + numero2
    print(f"O valor da soma é {resultado:.2f}")
elif operador == "-":
        resultado = numero1 - numero2
        print(f"O valor da subtração é {resultado:.2f}")
elif operador == "*":
        resultado = numero1 * numero2
        print(f"O valor da multiplicação é {resultado:.2f}")
elif operador == "/":
    if numero2 == 0:
        print("Não existe divisão por zero")
    else:
        resultado = numero1 / numero2
    print(f"O valor da divisão é {resultado:.2f}")
else:
    print("Operador inválido")