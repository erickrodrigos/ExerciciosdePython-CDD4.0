"""Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um
vetor. A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no vetor;
(2) o menor e o maior valor existente no vetor;
(3) quantos dos valores do vetor são maiores que a média desses valores"""
n = 5
vetor = [0]*n
teste = 0
cont = n
x = 0
Soma = 0
Media = 0
contM = n

for i in range(n):
    vetor[i] = int(input("insira um numero: "))
    Soma = Soma + vetor[i]
print("\n")

Media = Soma/n

for y in range(n):
    if vetor[y]%2:
        cont = cont-1
maior = vetor[0]
menor = vetor[0]
for x in range(n):
    if maior < vetor[x]:
        maior = vetor[x]
    if menor > vetor[x]:
        menor = vetor[x]
    if vetor[x] < Media:
        contM -= 1

print(f"existem {cont} numeros pares no vetor \n"
      f" o maior numero é {maior} e o MENOR numero é {menor} \n "
      f"a Media é de {Media}, e os numeros que estão acima da média foram {contM} ao total")





































































































