nome = "Carol"
idade = 22
estudo = "Python"

# Forma 1
print("1. O meu nome é", nome, "tenho", idade, "anos e ", "estudo", estudo )

# Forma 2
print("2. O meu nome é {} tenho {} anos e estudo {}".format(nome, idade, estudo))
print("2. O meu nome é {0} tenho {1} anos e estudo {2}".format(nome, idade, estudo))
print("2. O meu nome é {n} tenho {i} anos e estudo {e}".format(n=nome,i=idade,e=estudo))

# Forma 3
print(f"3. O meu nome é {nome} tenho {idade} anos e estudo {estudo}")