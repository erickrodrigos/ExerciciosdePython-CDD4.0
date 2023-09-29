'''
#exercicio 2
cont = 1
Soma = 0
Media = 0
Notas = 0
N = float(input("Quantas notas serão adicionados: "))

while cont <= N:
    Notas = int(input("Insira uma nota: "))
    Soma = Soma + Notas
    cont = cont +1
Media = Soma/(cont-1)
print("A media é: ",Media)

#EXERCICIO 3 - FEITO DE UM JEITO DIFICIL
cont = 1
Soma = 0
Media = 0
Notas = 0

while cont <= 2:
    Notas = float(input("Insira uma nota: "))
    if Notas > 0 and Notas < 11:
        Soma = Soma + Notas
        cont = cont + 1
        Media = Soma/(cont-1)
    else:
        print("Numero inválido: ",Notas)
        print("Digite 1 caso queira reiniciar :  ", Notas)

        break

print("A media é: ",Media)


#COMO O PROF FEZ

cont = 1
Soma = 0
Media = 0
Nota1 = 0
Nota2 = 0
teste = 0

while teste == 0:

    Nota1 = float(input("Insira a primeira nota: "))
    while  Nota1 < 0 or Nota1 > 10:
        Nota1 = float(input("nota Inválida!!! Insira uma nota: "))

    Nota2 = float(input("Insira a segunda nota: "))
    while  Nota2 > 10 or Nota2 < 0:
        Nota2 = float(input("nota Inválida!!! Insira uma nota: "))

    Media = (Nota2+Nota1)/2

    print("A media é: ",Media)

    teste = input("Deseja refazer uma nova média, digite 1: ")


#mostrar um numero erepetir o seu
N = 0
cont = 0
NX = 0

N = int(input("Insira um numero: "))

for X in range(1,N+1):
print(x*str(X), end= "")


#mostrar um numero e repetir o seu só que na ordem um abaixo do outro
N = 0
cont = 0
NX = 0

N = int(input("Insira um numero: "))

for X in range(1,N+1):
    print(X*str(X))
'''
#mostrar um numero e mostrar a ordem dele
N = 0
cont = 0
NX = 0

N = int(input("Insira um numero: "))

for A in range(1,N+1):
    for X in range (1,A+1):
        print(X*str(X))
