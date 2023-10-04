"""altere o exercício anterior e mostre na tela, ao final, o nome de cada
aluno e sua respectiva posição no array"""

N = 0
Lista = []
Nome = 0
N = int(input("quantos alunos tem na sala: "))

for n in range(N):
    Nome = (input("adicione: "))
    Lista.append(Nome)
for x in range(N):
    print(Lista[x],'-',x+1)