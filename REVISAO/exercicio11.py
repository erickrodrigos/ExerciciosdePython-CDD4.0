#1. Faça um algoritmo que leia a idade de
#uma pessoa expressa em anos, meses e dias
#e escreva a idade dessa pessoa expressa
#apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

Dia = 0
Mes = 0
Id = 0
AnoAtual = 2023
MesAtual = 9
DiaAtual = 28
Dias = 0
Meses = 0
print("  Vamos calcular os seus dias  ")
Id = int(input("informe a sua Idade: "))
Dia = int(input("informe o dia de nascimento: "))
Mes = int(input("informe o Mes de nascimento: "))

"""print("  Agora é necessário informar sobre a data atual  ")
DiaAtual = int(input("informe o dia Atual: "))
MesAtual = int(input("informe o Mes de Atual: "))
AnoAtual = int(input("informe o Ano Atual: "))
"""
Meses = MesAtual - Mes
if Meses < 0:
    Meses = Meses*(-1)
DiaAtual = DiaAtual-Dia
if DiaAtual <0:
    DiaAtual = DiaAtual*(-1)

Dias = Id*365 + Meses*30 + DiaAtual

print(f"o seus dias vivos são: {Dias}")
