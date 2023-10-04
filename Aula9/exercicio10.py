"""Faça um código para ler um valor N qualquer (que será o tamanho dos vetores).
Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um
terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando
as mesmas posições) e escrever o vetor Soma"""

n = int(input("informe o tamanho do seu vetor: "))
vetorA = [0]*n
vetorB = [0]*n
Soma = [0]*n

for x in range(n):
    vetorA[x] = int(input("insira um numero no vetor A: "))
    vetorB[x] = int(input("insira um numero no vetor B: "))
    Soma[x] = vetorA [x] + vetorB [x]
print(Soma)
