"""Faça um código para ler um vetor de 30 números. Após isto, ler mais
um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor."""
n = 30
vetor = [0]*n
teste = 0
cont = 0

for i in range(n):
    vetor[i] = int(input("insira um numero: "))
print("\n")
teste = int(input("numero teste: "))
for y in range(n):
    if teste == vetor[y]:
        cont = cont+1
print(f"o numero foi repetido {cont} vezes")