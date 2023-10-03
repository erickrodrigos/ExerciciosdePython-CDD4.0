num1 = 0
num2 = 0
num3 = 0
maior =0
num1 = int(input(" Digite um numero: "))
num2 = int(input(" Digite um numero: "))
num3 = int(input(" Digite um numero: "))

"""if num1 > num2:
    if num1 > num3:
        print(" o numero mair foi: ", num1)
    else:
        print(" o numero mair foi: ", num3)
else:
    if num3 > num2:
        print(" o numero mair foi: ", num3)
    else:
        print(" o numero mair foi: ", num2)"""

# Como feito por vitor
maior = num1

if maior < num2:
    maior = num2
if maior <num3:
    maior = num3
print(" o numero mair foi: ",maior)