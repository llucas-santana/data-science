agenda = {}

def programa():
    opcao = 1

    while opcao != 0:
        print("1 - Incluir novo nome")
        print("2 - Incluir telefone")
        print("3 - Excluir nome")
        print("4 - Excluir telefone")
        print("5 - Consultar telefone")
        print("0 - Sair")

        opcao = int(input("Informe a opcao: "))

        if opcao == 1:
            nome = input("Informe o nome do contato: ")
            opcao_telefone = 'S'
            telefone = []

            while opcao_telefone == 'S':
                telefone.append(input("Informe o telefone: "))
                opcao_telefone = input("Deseja informar um novo telefone? (S/N) ")

            agenda = incluirTelefone(agenda, nome, telefone)
        
        if opcao == 2:
            nome = input("Informe o nome do contato: ")
            telefone = input("Informe o telefone: ")
            agenda = incluirTelefone(agenda, nome, telefone)
        
        if opcao == 3:
            nome = input("Informe o nome do contato: ")
            telefone = input("Informe o telefone: ")
            agenda = excluirTelefone(agenda, nome, telefone)

        if opcao == 4:
            nome = input("Informe o nome do contato: ")
            consultarTelefone(agenda, nome)

def incluirNovoNome(agenda, nome, telefones):
    if nome in agenda:
        print("Nome ja existe") 
    else:
        agenda[nome] = telefones[:]

    return agenda


def incluirTelefone(agenda, nome, telefones):
    if nome in agenda:
        agenda[nome].append(telefones[:])
    else:
        adicionar = input("Nome nao encontrado! Deseja inserir? S/N")
        if adicionar == 'S':
            incluirNovoNome(agenda, nome, telefones)

    return agenda

def excluirTelefone(agenda, nome, telefone):
    telefones = agenda[nome]
    if len(telefones) == 0:
        agenda.pop(nome)
    else:
        telefones.remove(telefone)
        agenda[nome] = telefones

    return agenda

def excluirNome(nome):
    agenda.pop(nome)   
    return agenda

def consultarTelefone(nome):
    return print(agenda.get(nome))


programa()