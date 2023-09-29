#receber a quantidades de alunos e adicione o nome deles.
"""N = 0
Lista = []
Nome = 0
N = int(input("quantos alunos tem na sala: "))

for n in range(N):
    Nome = (input("adicione: "))
    Lista.append(Nome)
print(Lista)


#receber a quantidades de alunos e adicione o nome deles e mostrar sua posição na lista
N = 0
Lista = []
Nome = 0
N = int(input("quantos alunos tem na sala: "))

for n in range(N):
    Nome = (input("adicione: "))
    Lista.append(Nome)
for x in range(N):
  =  print(x+1, '-',Lista[x])



#Receba o nomes de 5 alunos e suas notas, em seguida calcular a media da turma e dizer quantas notas estão abaixo da média
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
print("acima da media: {top}")

 """
A = [0,0,0,0,0,0,0,0,0,0]
M = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    A[i] = float(input("adicione: "))

x = float(input("qual o numero multiplicador: "))
for j in range(10):
    M[j] = x*A[j]
print(M)
