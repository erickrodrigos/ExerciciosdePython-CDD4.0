
palavra = []
dica = ''
palavraFinal = ''
erros = 0
letrasDitas = []
tamanho = 0
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
        print(" |   foi ENFORCADO !!!   ")

    print(" |            ")
    print("_|___    ")
    print()

def venceu(palvra):
    print(f"\n     Parabéns! Você acertou a palavra  ~* {palavra} *~")
    print("              _______ ")
    print("  PARABÉNS   |/      | ")
    print(" ESTÁ LIVRE  |         ")
    print("      (_)    |         ")
    print("      \|/    |         ")
    print("       |     |         ")
    print("      / \   _|___      ")
    print()

def revelarPalavra(palavra, palavraFinal, letra):
    novaPalavra = ''
    for i in range(len(palavra)):
        if palavra[i] == letra:
            novaPalavra += letra
        else:
            novaPalavra += palavraFinal[i]

    return novaPalavra

palavra = input("informe qual palavra será adivinhada: ").lower()
tamanho = len(palavra)
palavraFinal = '_' * tamanho
dica = input(" Ajude seus amigos, informe uma Dica ;)  - ")

print("")
print("   BEM VINDO AO JOGO DA FORCA \n")
desenhaForca(0)
print(f"a dica é: {dica}")
print(f"a palavra com {tamanho} letras é: {palavraFinal}")

while palavraFinal != palavra:
    letra = input("   Digite uma letra: ").lower()

    if letra in letrasDitas:
        print("\n     Você já tentou essa letra antes.")
        continue
#adicionar asa palavras ditas em uma lista para evitar repetições
    letrasDitas.append(letra)

    if len(letra) != 1 or not letra.isalpha(): #isalpha é uma função que identifica caracteres especiais e numericos
        print("\n Por favor, digite uma única letra válida ou caracter válido.")
        continue

    if letra in palavra:
        palavraFinal = revelarPalavra(palavra, palavraFinal, letra)
        #palavraFinal = palavraRevelada
        print("\n      Palavra:", palavraFinal, "      ",dica)

        tentativa = input(
            "\n deseja chutar a palavra?  \n 1 - Digite S ou 1"
            "\n 2 - Caso NÃO, digite qualquer letra\n    ").lower()

        if tentativa == 's' or tentativa == '1':
            chute = input(" qual o seu palpite ?  ")
            if chute == palavra:
                palavraFinal = chute
            else:
                erros += 1
                print("   ERROU !!!!")
                desenhaForca(erros)
        else:
            continue

    else:
        erros += 1
        print(f"\n       Letra não encontrada na palavra. Ainda resta {7 - erros} tentativas")
        desenhaForca(erros)

    if erros >= 6:
        print(f"Você perdeu! A palavra era {palavra}:")
        desenhaForca(erros)
        break

if palavraFinal == palavra:
    venceu(palavra)