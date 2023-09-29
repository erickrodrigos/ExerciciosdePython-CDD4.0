# Faça um código que receba 4
#números e realize a soma deles e a
#média entre eles. e mostre os resultados.


Soma = 0
Media = 0
Num = 0
quant = 0

"""
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
num1 = float(input("informe o primeiro numero: "))
num2 = float(input("informe o segundo numero: "))
num3 = float(input("informe o terceiro numero: "))
num4 = float(input("informe o quarto numero: "))

Soma = num1+num2+Num3+Num4
print(f"A Soma é  {Soma}")
Media = Soma/4
print(f"A Média é {Media}")
"""

quant = int(input("informe quantos numeros serão inseridos: "))
while quant == 0:
    quant = int(input("informe um numero válido: "))

for x in range(quant):
    num = float(input("informe um numero: "))
    Soma+= num

print(f"A Soma é  {Soma}")
Media = Soma/quant
print(f"A Média é {Media}")

