Media = 0
Soma = 0
while :
    Num = int(input("insira um número: "))
    if Num%2 != 0:
        # caso queira um numero par apenas tirar o '!'
        Soma = Soma+Num
print(Soma)