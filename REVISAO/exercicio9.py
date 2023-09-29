#Faça um código que receba um número inteiro e mostre o seu antecessor.
num = 0
resp = 0
resp = int(input("     Olá escolha qual operação deseja realizar:\n "
                 "     Escolha entre 1, 2 ou 3 \n"
                 " 1 - calcular o antessesor\n "
                 "2 - calcule o sucessor \n "
                 "3- deseja encerrar\n       a opção é a  "))
while resp > 3 or resp < 1:
    resp = int(input("     NUMERO INVÁLIDO !!!!!!!:\n "
                     "     Escolha entre 1, 2 ou 3 \n"
                     " 1 - calcular o antessesor\n "
                     "2 - calcule o sucessor \n "
                     "3- deseja encerrar\n a opção é a  "))
while resp != 3:

    if resp == 1:
        num = int(input("informe um número: "))
        num-=1
        print(f"O numero anterior é {num}")
    elif resp == 2:
        num = int(input("informe um número: "))
        num += 1
        print(f"O numero Sucessor é {num}")

    resp = int(input("     Olá escolha qual operação deseja realizar:\n "
                 "     Escolha entre 1, 2 ou 3 \n"
                 " 1 - calcular o antessesor\n "
                 "2 - calcule o sucessor \n "
                 "3- deseja encerrar\n     a opção é a  "))