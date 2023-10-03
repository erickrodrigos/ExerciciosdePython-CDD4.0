"""Escreva um algoritmo para ler dois valores (considere que não
serão lidos valores iguais) e escrevê-los em ordem crescente"""
num1 = 0
num2 = 0
num1 = int(input(" Digite um numero: "))
num2 = int(input(" Digite outro numero, diferente do anterior: "))

while num1 == num2:
    num1 = int(input("\n Numeros Iguais !!!\n "
                     "Digite novamente um numero: "))
    num2 = int(input(" Digite outro numero,\n"
                     " diferente do anterior: "))

if num1 > num2:
    print(f"na ordem crescente: {num1}, {num2}")
else:
    print(f"na ordem crescente: {num2}, {num1}")



"""Escreva um algoritmo para ler dois valores (considere que não
serão lidos valores iguais) e escrevê-los todos os que tem dentro em ordem crescente

if num1 > num2:
    for x in range(num2+1,num1):
        print(x, end =" ")
else:
    for x in range(num1+1,num2):
        print(x, end =" ")

"""