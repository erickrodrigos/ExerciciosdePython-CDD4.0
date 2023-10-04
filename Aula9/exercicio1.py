"""Perguntar ao usuário quantos alunos tem na sala e criar um array,
 unidimensional (Vetor) com o nome de todos os alunos da sala"""
N = 0
Lista = []
Nome = 0
N = int(input("quantos alunos tem na sala: "))

for n in range(N):
    Nome = (input("adicione: "))
    Lista.append(Nome)
print(Lista)