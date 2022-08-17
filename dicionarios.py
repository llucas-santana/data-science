#DICIONARIOS

#chaves e valores
agenda = {
    "Maria" : [998547845, 985745784],
    "João" : [986574587],
    "Paula" : [998578457, 996254785, 998235678]
}

#dicionário vazio
#agenda = {}

#acessando valores
#print(agenda["Maria"])
agenda["Maria"][0]

#diferente de listas, em dicionários um valor pode
#ser adicionado sem que a posição exista previamente
agenda["Solange"] = 985745874
#print(agenda)

#copiar dicionário
agenda2 = agenda.copy()
print(agenda2)

#remover todos os elementos do dicionário
agenda.clear()


