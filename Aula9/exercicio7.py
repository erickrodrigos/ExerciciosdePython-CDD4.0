""""Faça um código para ler 5 números e armazenar em um vetor.
Após a leitura total dos 5 números, o código deve escrever esses
 5 números lidos na ordem inversa."""
vetor = [0,0,0,0,0]

for y in range(5):
    vetor[y] = int(input('inserir um  numero: '))

for i in range(4, -1, -1):
    print(vetor[i], end=" ")
