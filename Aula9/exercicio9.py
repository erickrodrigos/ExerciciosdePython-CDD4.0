"""Faça um código para ler 5 nomes de usuários e suas respectivas senhas,
 e armazenar cada lista em um array diferente, após completar a digitação,
imprimir , nome, senha e posição dos dados no array"""
Nomes = [0,0,0,0,0]
senhas = [0,0,0,0,0]
n = 5
cont = 0
repNome = True
obterSenha = False
indice = 0
rep = 0
repsenha = 0
SenhaLogin =  0

for x in range(n):
    Nomes[x] = input("inserir nome: ")
    senhas[x] = input("inserir SENHA: ")
print("\n")

#nome e analisar

while repNome == True:
    NomeLogin = input("inserir o nome para o LOGIN: ")
    cont = 0
    for y in range(n):
        if NomeLogin == Nomes[y]:
            obterSenha = True
            repNome = False
            indice = y
        else:
            cont +=1

        if cont == n:
            rep = rep + 1
            print("nome inválido !!!!\n informe Novamente abaixo")

    if rep == 3:
        repNome = False
        print("       tentativas encerradas")

while obterSenha == True:
    SenhaLogin = input("inserir a Senha do LOGIN: ")
    if SenhaLogin == senhas[indice]:
        print("senha e nome correto !!!!")
        break
    else:
        repsenha = repsenha + 1
    if repsenha < 4:
        print("Senha inválido !!!!\n informe Novamente abaixo")
    if repsenha == 4:
        obterSenha = False
        print("       tentativas encerradas \n")