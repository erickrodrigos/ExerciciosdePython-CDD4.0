'''
#somar pedir 10 numeros e soma-los
Soma = 0
for x in range(10):
    Nx = int(input("insira 1 numero: "))
    Soma += Nx
print("soma: ", Soma)

#inserir um número e mostrar a tabuada dele de 0 até 10
Tab = 0
Num = int(input("insira 1 numero: "))
for x in range(1,11):
    Tab = Num*x
    print("Tabuada: ",Tab)

#inserir um número e mostrar todos os numeros impares nesse intervalo
Num = int(input("insira um número: "))
for x in range(1,Num):
    if x%2 != 0:
        # caso queira um numero par apenas tirar o '!'
        print(x)

#pegar 10 numeros com o usuário e somar os impares
Soma = 0
for x in range(1,10):
    Num = int(input("insira um número: "))
    if Num%2 != 0:
        # caso queira um numero par apenas tirar o '!'
        Soma = Soma+Num
print(Soma)
'''
#pegar a quantidade de notas, em seguida armazena-las e por fim calcular a media geral
Soma = 0
NumT = int(input("insira um número de Alunos: "))
for x in range(NumT):
    Nx = float(input("inserir a nota dele:"))
    Soma += Nx
media = Soma/NumT
print("Média: ", media)






