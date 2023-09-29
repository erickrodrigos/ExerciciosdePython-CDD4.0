# Faça um Algoritmo que receba um
#número inteiro e mostre o seu sucessor.

h_inicial = int(input('Digite a hora inteira de INICIO do jogo: '))
h_final = int(input('Digite a hora inteira de FIM do jogo: '))
h_total = h_final - h_inicial

if h_final < h_inicial:
    resto = 24 - h_inicial
    h_total = h_final + resto

print(h_total)