#LISTAS

#Sequência de valore mutáveis
#Indexação por números inteiros

#diferença entre tupla e lista
tupla = (1, 2, 3)
lista = [1, 2, 3]

#inserir elemento no final da lista
lista.append(4)
print(lista)

#excluir último elemento da lista
lista.pop()
print(lista)

#inserir elemento em determinada posição
lista.insert(2, 10)
print(lista)

#excluir elemento de determinada posição
lista.pop(2)
print(lista)

#excluir elementos pelo valor
lista.remove(4)
print(lista)

#concatenar listas
lista2 = [5, 6, 7]
lista = lista + lista2

#ordernar lista em ordem crescente
lista.sort()

#ordernar lista em ordem decrescente
lista.reverse()

#cópia de listas – deve-se copiar o conteúdo,
#do contrário será feito referência ao mesmo
#endereço de memória
lista2 = lista[:]

