diario_classe = {}
lista_notas = []
nome = input("Informe o nome do aluno: ")

while nome != '0':
    lista_notas.append(int(input("Informe a 1° nota: ")))
    lista_notas.append(int(input("Informe a 2° nota: ")))
    diario_classe[nome] = lista_notas[:]
    lista_notas.clear()
    nome = input("Informe o nome do aluno: ")

nome = input("Informe o nome do aluno para visualizar as notas: ")

if nome in diario_classe:
    print(diario_classe[nome])
else:
    print("Nome informado invalido")