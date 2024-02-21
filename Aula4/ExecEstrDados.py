# Manipulação de Listas:
# Crie uma lista de números inteiros e ordene-a em ordem crescente.
# Adicione o número 10 ao final da lista.
# Remova o elemento de valor 5 da lista.
listNum1 =[1,2,3,4,5,6,7,8,9]
listNum1.append(10)
listNum1.remove(5)
print(str(listNum1))

# Slicing e Operações:
# Crie uma lista com os primeiros 10 números inteiros.
# Utilize o slicing para criar uma sublista com os números pares.
# Inverta a ordem da sublista criada.
listNum2 = [1,2,3,4,5,6,7,8,9,10]
sublista = listNum2[1::2]
sublistaInvertida = sublista[::-1]
print(str(sublistaInvertida))
    
# Listas Aninhadas:
# Crie uma lista aninhada contendo duas sublistas: uma com nomes de cores e outra com códigos hexadecimais correspondentes.
# Acesse e imprima o código hexadecimal da cor "verde".
listCor = ["Vermelho", "Amarelo", "Verde"]
listHexa = ["FF0000", "ffff00", "008000"]
list3 = [listCor, listHexa]
print(list3[0][2],list3[1][2])

# Tuplas:
# Operações com Tuplas:
# Crie uma tupla com os meses do ano.
# Acesse os meses de janeiro a junho.
# Tente adicionar um novo mês à tupla e observe o resultado.
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses_do_ano[0], meses_do_ano[5])
# meses_do_ano.append("novoMes")

# Tuplas como Chaves de Dicionários:
# Crie um dicionário onde as chaves são tuplas representando coordenadas (latitude, longitude) e os valores são nomes de cidades.
# Acesse e imprima o nome da cidade correspondente à coordenada (40.7128, -74.0060).
coordenadas_cidades = {
    (40.7128, -74.0060): "Nova Iorque",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago",
    (37.7749, -122.4194): "São Francisco",
    (51.5074, -0.1278): "Londres"
}
print(coordenadas_cidades[(40.7128, -74.0060)])

# Conjuntos:
# Operações de Conjuntos:
# Crie dois conjuntos com números inteiros.
# Realize a união, interseção e diferença entre esses conjuntos.
conj1 = {1,2,3,4,5}
conj2 = {5,6,7,8,9}
uniNum = conj1.union(conj2)
insNum = uniNum.intersection({7,8,9,10})
difNum = uniNum.difference({5,6,7})
print(str(uniNum)+"\n"+str(insNum)+"\n"+str(difNum))
# Remoção de Duplicatas:
# Crie uma lista com elementos duplicados.
# Converta a lista para um conjunto para remover as duplicatas.
listDupli = [1,0,1,2,3,2,1,2,1]
listRemoveDupli = set(listDupli)
print(listRemoveDupli)

# Dicionários:
# Manipulação de Dicionários:
# Crie um dicionário representando informações sobre um livro (título, autor, ano de publicação).
# Adicione uma nova chave-valor ao dicionário representando a quantidade de páginas do livro.
dicLivro = {'titulo': 'O filho de netuno', 'autor': 'Rick Riordan', 'ano de publicacao': '2012'}
dicLivro['quantidade de paginas'] = '432'
print(dicLivro)
# Iteração e Impressão:
# Crie um dicionário com nomes de países e suas respectivas capitais.
# Utilize um loop para imprimir cada país e sua capital.
dicCapitais = {
    'Brasil': 'Brasília',
    'EUA': 'Washington D.C.',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Índia': 'Nova Delhi'
}
for pais, capital in dicCapitais.items():
   print("Pais: "+str(pais)+" capital: "+str(capital))
# Remoção de Itens:
# Crie um dicionário com pares chave-valor representando um inventário de produtos.
# Remova um item do inventário utilizando sua chave.
inventario_produtos = {
    'produto1': {'nome': 'Camiseta', 'quantidade': 50, 'preco_unitario': 20.00},
    'produto2': {'nome': 'Calça Jeans', 'quantidade': 30, 'preco_unitario': 50.00},
    'produto3': {'nome': 'Tênis', 'quantidade': 20, 'preco_unitario': 80.00},

}
del inventario_produtos['produto2']
print(inventario_produtos)