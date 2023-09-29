#Escreva um algoritmo para ler as dimensões de um retângulo
# (base e altura), calcular e escrever a área do retângulo.
base = 0
Alt = 0

base = float(input("Informe a base do seu Retangulo: "))
while base <= 0:
    base = float(input("\n VALOR INCORRETO !!!!\n Informe a base do seu Retangulo diferente de zero: "))

Alt = float(input("Informe a Altura do seu Retangulo: "))
while Alt <= 0:
    Alt = float(input("\n VALOR INCORRETO !!!!\n Informe a Altura do seu Retangulo diferente de zero: "))

Area = base*Alt
print(f"A area é {Area} m^2")