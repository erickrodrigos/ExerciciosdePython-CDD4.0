"""Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a
 lista desses nomes na tela. Após exibir essa lista, o programa deve mostrar também
 os nomes na ordem inversa em que o usuário os digitou, um por linha."""
nome = [0,0,0,0,0]
n = 5
indice = 0

for x in range(n):
    nome[x] = input("insira Nome: ")
print(nome)

for i in range(n):
    indice = n - i -1
    print(nome[indice], end="\n")
