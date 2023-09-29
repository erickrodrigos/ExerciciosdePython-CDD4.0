"""""
#pedir 2 notas e calcular a média
NOTA1 = 0
NOTA2 = 0
Media = 0
NOTA1 = float(input("informe a primeira nota: "))
NOTA2 = float(input("informe a segunda nota: "))

Media = (NOTA1+NOTA2)/2
print("A media é: ", Media)

if Media >= 7:
    print("Aluno Aprovado Com honras !!")
elif Media >=4:
    print("Aluno em Recuperação !!")
else:
    print("Aluno Reprovado, tirar foto com o prof Hahahahahah !!")

#jeito do prof
if Media < 7:
    if Media <= 4:
        print("Aluno em Recuperação !!")
    else:
        print("Aluno Reprovado, tirar foto com o prof Hahahahahah !!")
else:
    print("Aluno Aprovado Com honras !!")"""

# Solicitar se o usuario deseja fazer um novo calculo

Refazer = 1
while Refazer == 1:
    NOTA1 = 0
    NOTA2 = 0
    Media = 0

    NOTA1 = float(input("informe a primeira nota: "))
    NOTA2 = float(input("informe a segunda nota: "))

    Media = (NOTA1+NOTA2)/2
    print("A media é: ", Media)

    if Media >= 7:
        print("Aluno Aprovado Com honras !!")
    elif Media >=4:
        print("Aluno em Recuperação !!")
    else:
        print("Aluno Reprovado, tirar foto com o prof Hahahahahah !!")

    Refazer = int(input("Deseja refazer uma nova média, Digite 1:  "))
