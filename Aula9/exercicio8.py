"""Faça um código para ler 5 números e armazenar em um vetor. Após a leitura
total dos 5 números, o código deve escrever esses 5 números lidos na ordem
inversa"""

Nomes = [0,0,0,0,0]
senhas = [0,0,0,0,0]

for x in range(5):
    Nomes[x] = input("inserir nome: ")
    senhas[x] = input("inserir SENHA: ")

for y in range(5):
    print("Nome: ",Nomes[y],"senha: ",senhas[y],"indice: ", y)