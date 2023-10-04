"""Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar
em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A
multiplicado pelo valor X. Logo após, imprimir o vetor M"""
A = [0,0,0,0,0,0,0,0,0,0]
M = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    A[i] = float(input("adicione: "))

x = float(input("qual o numero multiplicador: "))
for j in range(10):
    M[j] = x*A[j]
print(M)