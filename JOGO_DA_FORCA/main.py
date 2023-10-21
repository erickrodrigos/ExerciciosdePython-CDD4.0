def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



palavra = []
dica = ''
palavraFinal = ''
novaPalavra = ''
erros = 0
palavraRevelada = []
letrasDitas = []
tentativa = 0


def revelarPalavra(palavra, palavraFinal, letra):
    novaPalavra = ''
    for i in range(len(palavra)):
        if palavra[i] == letra:
            novaPalavra += letra
        else:
            novaPalavra += palavraFinal[i]

    return novaPalavra



palavra = input("informe qual palavra será adivinhada: ")
palavraFinal = '_' * len(palavra)
dica = input(" Ajude seus amigos, informe uma Dica ;)  - ")

print("")
print("")
print("")

print("   BEM VINDO AO JOGO DA FORCA \n")
desenhaForca(0)
print("a dica é: ", dica)
print("a palavra é: ", palavraFinal)

while palavraRevelada != palavra:
    letra = input("   Digite uma letra: ").lower()

    if letra in letrasDitas:
        print("Você já tentou essa letra antes.")
        continue

    letrasDitas.append(letra)

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite uma única letra válida ou caracter válido.")
        continue

    if letra in palavra:
        palavraRevelada = revelarPalavra(palavra, palavraFinal, letra)
        palavraFinal = palavraRevelada
        print("Palavra revelada:", palavraFinal)
    else:
        erros += 1
        print("Letra não encontrada na palavra oculta. Tentativas restantes:", 7 - erros)
        desenhaForca(erros)

    tentativa = int(input("deseja chutar a palavra?  \n 1-  SIM\n 2 - NÃO\n    "))

    if tentativa == 1:
        chute = input(" qual o seu palpite ? ")
        if chute == palavra:
            palavraRevelada = chute
        else:
            erros += 1
            print("   ERROU !!!!")
            desenhaForca(erros)


    if erros >= 7:
        print("Você perdeu! A palavra oculta era:", palavra)
        desenhaForca(erros)
        break

if palavraRevelada == palavra:
    print("Parabéns! Você acertou a palavra oculta:", palavra)




