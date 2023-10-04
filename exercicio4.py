"""Faça um código para ler um valor N qualquer (que será o tamanho dos
vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois
armazenar em um terceiro vetor Soma a soma dos elementos do vetor A
com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma."""

n = 0
soma = 0
n = int(input("informe o tamanho do seu vetor: "))
vetorA = [0]*n
vetorB = [0]*n
soma = [0]*n

for i in range(n):
    vetorA[i] = int(input("inserir numero na lista A: "))
    vetorB[i] = int(input("inserir numero na lista B: "))
    soma[i] = vetorA[i]+vetorB[i]
print(soma)