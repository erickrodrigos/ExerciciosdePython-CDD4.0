palavra = []
dica = ''
palavraFinal = ''
erros = 0
letrasDitas = []
tamanho = 0
t = 0
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
        print(" | VOCÊ FOI ENFORCADO !!!   ")
    if erros == 10:
        print(" |  PARABÉNS !       (_)   ")
        print(" | VOCE VENCEU       \|/   ")
        print(" | SOBREVIVEU         |    ")
        print(" |                   / \   ")


    print(" |            ")
    print("_|___    ")

def revelarPalavra(palavra, palavraFinal, letra):
    novaPalavra = ''
    for i in range(len(palavra)):
        if palavra[i] == letra:
            novaPalavra += letra
        else:
            novaPalavra += palavraFinal[i]
    return novaPalavra

def tentativa(palavra,erros):
    chute = input(" qual o seu palpite ?  ")
    if chute == palavra:
        return 1
    else:
        print("   ERROU !!!!")
        return 0

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
    letrasDitas += letra

    if len(letra) != 1:
        print("\n Por favor, digite uma única letra.")
        continue

    if letra in palavra:
        palavraFinal = revelarPalavra(palavra, palavraFinal, letra)
        print("\n      Palavra:", palavraFinal, "      ","Dica: ",dica)

        tentativas = input(
            "\n deseja chutar a palavra?  \n 1 - Digite S ou 1"
            "\n 2 - Caso NÃO, digite qualquer letra\n    ").lower()

        if tentativas == 's' or tentativas == '1':
           t = tentativa(palavra,erros)
        else:
            continue
        if t == 1:
            break
        else:
            erros += 1
            desenhaForca(erros)

    else:
        erros += 1
        print(f"\n       Letra não encontrada na palavra. Ainda resta {7 - erros} tentativas")
        desenhaForca(erros)

    if erros >= 6:
        print(f"Você perdeu! A palavra era {palavra}:")
        desenhaForca(erros)
        break

if palavraFinal == palavra or t == 1:
    desenhaForca(10)