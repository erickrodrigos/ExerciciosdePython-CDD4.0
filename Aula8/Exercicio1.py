#indice = posição da informação dentro do array, se inicia com o 0
#EX: B[3] = "ERICK" - insere na posição 7 a informação ERICK

#adicionar um item ao final de uma lista = .append()
#inserir um valor a uma posiçãop especifica = .insert()
#Del = remover um iten de uma lista
#remove o conteudo do indice da lista = .remove[]
#
# indice (-1) informa que conteudo do penultimo item de qualquer lista
item = 0
listaCompras = ['banana', 'laranja','maça']
for i in listaCompras:
    print(i)
print("adicionar 1 item: \n")
listaCompras.append('carro')
for i in listaCompras:
    print(i)
print("inseir em uma posição 2: \n")
listaCompras.insert(1,'carro')
for i in listaCompras:
    print(i)
"""print("Excluir um item: \n")
listaCompras.remove('banana')
for i in listaCompras:
    print(i)"""
del listaCompras[3]
print("\n",listaCompras,"\n")
item = listaCompras.pop(2)
print(item)

