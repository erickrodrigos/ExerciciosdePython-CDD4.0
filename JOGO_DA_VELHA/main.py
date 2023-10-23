j1 = ''
j2 = ''
matrix = [['A','B','C'],['D','E','F'],['G','H','I']]
cont = 0
JogadasFeitas = []
def preencherMatrixJ1(J):
    for x in range(3):
        for y in range(3):
            elemento = matrix[x][y]
            if J == elemento:
                matrix[x][y] = 'X'
    return matrix


def preencherMatrixJ2(J):
    for x in range(3):
        for y in range(3):
            elemento = matrix[x][y]
            if J == elemento:
                matrix[x][y] = '0'
    return matrix

def analisarJogo(matrix):
    for y in range(3):
        elemento = matrix[y][y]
        if elemento == 3:
            print("O JOGADOR VENCEU !!!")
            return 10
        else:
            continue


    #analisa se alguem venceu baseado na posição

print("    BEM VINDO AO JOGO DA VELHA !!!!!!!\n    "
      "Abaixo voçê tem um tabuleiro  onde cada letra representa uma posição dentro da Grade\n     "
      "Vocês terá que escolher cada uma das opçoes  onde será preenchido com o seu simbolo\n\n"
      "     O jogador 1 ficará com o X e o Jogador 2 com o 0 ")
print('\n',matrix[0],'\n',matrix[1],'\n',matrix[2])

while cont < 9:
    Fim = analisarJogo(matrix)

    j1 = input("\n  Jogador 1 escolha a letra que representa a posição na grade: ").upper()
    preencherMatrixJ1(j1)

    print('\n', matrix[0], '\n', matrix[1], '\n', matrix[2])
    JogadasFeitas += j1

    j2 = input("\n Jogador 2 escolha a letra que representa a posição na grade: ").upper()
    preencherMatrixJ2(j2)

    print('\n',matrix[0],'\n',matrix[1],'\n',matrix[2])

    JogadasFeitas += j2

    if j1 in JogadasFeitas or j2 in JogadasFeitas:
        print("\n   jogada Inválida, encontre um campo não preenchido, PERDEU A VEZ ")

    cont+=1
    if Fim == 10:
       print(f"o jogador  venceu !!!!")

