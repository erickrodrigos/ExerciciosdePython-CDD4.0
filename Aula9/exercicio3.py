N = 0
Lista = []
Nome = 0
procurar = 0

N = int(input("quantos alunos tem na sala: "))

for n in range(N):
    Nome = input("adicione: ")
    Lista.append(Nome)

procurar = input("qual nome deseja saber se está adicionado na lista: ")
for x in range(N):
    if procurar == Lista[x]:
        print('o nome se encotra na lista na posição ', x + 1)

#altere o exercício anterior para permitir achar o nome de um aluno na lista

