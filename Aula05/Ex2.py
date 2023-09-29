'''
#EXERCICIO 2
for x in range (101,111):
    print(x)

i = 101
while i < 111:
  print(i)
  i += 1


#EXERCIO 3
N = int(input("me de um numero maior que zero: "))
if (N>0):
    for x in range (1,N+1):
         print(x)

elif(print("numero inválido")):


NN = 0
NX=0
for X in range (0,10):
    NX = int(input("me de um numero: "))
    if NX < 0:
       NN += 1
print(NN)



#EXERCICIO 4
N_Negativo = 0
N_Positivo = 0
NX=0
for X in range (0,10):
    NX = int(input("me de um numero: "))
    if(NX >= 10 and NX <= 20):
       N_Negativo += 1
N_Positivo = 10 - N_Negativo
if N_Negativo<0:
    N_Negativo = -1*N_Negativo
print("Numeros dentro: ",N_Negativo,"os que estão fora:",N_Positivo)


#exercicio de while
cont = 0
Soma = 0
Media = 0
while cont<10:
    N = int(input("Insira uma nota: "))
    Soma = Soma +N
    cont = cont +1
    Media = Soma/cont
print("A media é: ",Media)

'''
#EXERCICO 5
cont = 0
Soma = 0
Media = 0

N = int(input("me de um numero de alunos: "))

while cont<N:
    N = int(input("Insira uma nota: "))
    Soma = Soma +N
    cont = cont +1
    Media = Soma/cont
print("A media é: ",Media)



