
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
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
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
tamanho = 0

def revelarPalavra(palavra, palavraFinal, letra):
    novaPalavra = ''
    for i in range(len(palavra)):
        if palavra[i] == letra:
            novaPalavra += letra
        else:
            novaPalavra += palavraFinal[i]

    return novaPalavra

palavra = input("informe qual palavra será adivinhada: ")
tamanho = len(palavra)
palavraFinal = '_' * tamanho
dica = input(" Ajude seus amigos, informe uma Dica ;)  - ")

print("")
print("   BEM VINDO AO JOGO DA FORCA \n")
desenhaForca(0)
print(f"a dica é: {dica}")
print(f"a palavra com {tamanho} letras é: {palavraFinal}")

while palavraRevelada != palavra:
    letra = input("   Digite uma letra: ").lower()

    if letra in letrasDitas:
        print("Você já tentou essa letra antes.")
        continue
#adicionar asa palavras ditas em uma lista para evitar repetições
    letrasDitas.append(letra)

    if len(letra) != 1 or not letra.isalpha(): #isalpha é uma função que identifica caracteres especiais e numericos
        print("Por favor, digite uma única letra válida ou caracter válido.")
        continue

    if letra in palavra:
        palavraRevelada = revelarPalavra(palavra, palavraFinal, letra)
        palavraFinal = palavraRevelada
        print("Palavra revelada:", palavraFinal)
    else:
        erros += 1
        print(f"Letra não encontrada na palavra oculta. Ainda resta {7 - erros} tentativas")
        desenhaForca(erros)

    tentativa = input("deseja chutar a palavra?  \n 1 - Digite S\n 2 - Caso NÃO, digite qualquer letra\n    ").lower()

    if tentativa == 's':
        chute = input(" qual o seu palpite ?  ")
        if chute == palavra:
            palavraRevelada = chute
        else:
            erros += 1
            print("   ERROU !!!!")
            desenhaForca(erros)
    else:
        continue

    if erros >= 6:
        print(f"Você perdeu! A palavra era {palavra}:")
        desenhaForca(erros)
        break

if palavraRevelada == palavra:
    print(f"        Parabéns! Você acertou a palavra  *{palavra}*")

