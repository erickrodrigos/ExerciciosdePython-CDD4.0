#. Faça um código que receba o valor da
#base e da altura de um triângulo e
#calcule sua área. usando a fórmula A = (base x Altura ) /2
base = 0
Alt =0

base = float(input("Informe a base do seu triangulo: "))
while base <= 0:
    base = float(input("Informe a base do seu triangulo diferente de zero: "))

Alt = float(input("Informe a Altura do seu triangulo: "))
while Alt <= 0:
    Alt = float(input("Informe a Altura do seu triangulo diferente de zero: "))

Area = (base*Alt)/2
print(f"A area é {Area} m^2")

