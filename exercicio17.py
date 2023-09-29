preco = 0
quantidadeMacas = float(input("Digite quantidade de maças: "))

if quantidadeMacas > 12:
    preco = 1.30
else:
    preco = 1.0
custo = preco * quantidadeMacas
print("O custo de maças compradas foi: {}".format(custo))