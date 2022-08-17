# TUPLAS

#valores 
tupla = (-3,-2,-1,0,1,2,3)
#quando possui um unico elemento, colocar virgula ao final
#tupla = (1,) 

#acesso por posicao
print(tupla[0])

#fatiamento em tuplas/listas

#acessar valor da posicao 1 ate a posicao final -1
print(tupla[1:-1])

#acessar primeiro valor até a posição final -2
print(tupla[:-2])

#acessar todos os valores com incremento a posição valendo 2
print(tupla[::2])

#operacoes/funcoes basicas

valor = ('A', 'B', 'C')
#iteração
for v in valor:
    print(f'{v}')

for cont in range(0, len(valor)):
    print(f'{valor[cont]}')

#número de elementos da tupla
print(len(valor))

#apresentação da tupla ordenada
print(sorted(valor))

#quantidade de elementos com o valor A
print(valor.count('A'))

#posição do elemento A
print(valor.index('A'))

#verificar se elemento está na tupla
resultado = 'B' in valor

