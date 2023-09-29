"""As maçãs custam R$ 1,30 cada se forem compradas menos de
uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva
um programa que leia o número de maçãs compradas, calcule e
escreva o custo total da compra"""

reco = 0
custo = 0
quantidadeMacas = 0

quantidadeMacas = int(input("Digite quantidade de maças: "))

if quantidadeMacas < 12:
    preco = 1.30
else:
    preco = 1.0

custo = preco * quantidadeMacas
print(f"Cada maça custou {preco} reais e o custo total da compra foi de {custo} ")