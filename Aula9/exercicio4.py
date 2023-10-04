"""Escreva um código que permita a leitura das notas de uma turma de 5 alunos e
guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram
nota acima desta média calculada Escrever a média da turma e o resultado
da contagem"""

N = 0
ListaNotas = []
ListaNomes = []
Notas = 0
Soma = 0
N = 5
media = 0
soma = 0
top = 0
for n in range(N):
    Nomes = input("adicione nome: ")
    Notas = int(input("adicione a nota: "))
    ListaNotas.append(Notas)
    ListaNomes.append(Nomes)

for i in range(N):
    Soma +=ListaNotas[i]
media = Soma/N
print("media: ",media)

for j in range(N):
    if float(ListaNotas[j]) >= media:
        top+=1
print(f"acima da media: {top}")
