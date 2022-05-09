# inicio menu agenda
from typing import Dict, Any
agenda = {}

#salvar em ordem
def ordem():
    for linha in agenda.keys():
        print("{},{},{},{},{}".format(linha,agenda[linha][1],agenda[linha][2],agenda[linha][3],agenda[linha][4]))

#relatótio
def relatorio():
    print("Nome\t""\t", "Numero\t""\t", "Twiter\t""\t", "Instagram\n")
    for linha in agenda:
        print(agenda)

#editar contatos
def editarContato():
    print(agenda.keys())
    editar = str(input("Qual contato voçê quer editar? "))
    print("1:Telefone\n","2:Email\n","3:Twiter\n","4:Instagram")
    editarInfo = int(input("Quer alterar qual informação? "))
    if editarInfo == 1:
        telefone = input("Informe o telefone a ser alterado: ")
        agenda[editar][0] = telefone
    elif editarInfo == 2:
        email = input("Informe o email a ser alterado: ")
        agenda[editar][1] = email
    elif editarInfo == 3:
        twiter = input("Informe a conta do twiter a ser alterada: ")
        agenda[editar][2] = twiter
    elif editarInfo == 4:
        instagram = input("Informe a conta do instagram a ser alterada: ")
        agenda[editar][3] = instagram
    print(editar, agenda.get(editar))
    print("\n")
    menu()

#remover contato
def removerContato():
    print(agenda.keys())
    remover = input("Qual contato voçê quer remover? ")
    del agenda[remover]
    print(agenda.keys())
    menu()

#buscar contato
def recuperarContato():
    buscarContato = str(input("Digite o nome do contato: "))
    if buscarContato in agenda:
        print(agenda.get(buscarContato))
    else:
        print("\nContato não encontrado\n")
    menu()

# função que adiciona contato
def adicionarContato(nome, numero, email, twiter, instagram, qtd):
    agenda[nome] = [numero, email, twiter, instagram]
    while qtd <= 0:
        print(agenda)
        menu()

# função que recebe a entrada do usuario
def ent():
    entrada = int(input("Digite uma opção: "))

    # novo contato
    if entrada == 1:
        qtd = int(input("Quantos contatos quer adicionar? "))
        while qtd > 0:
            nomeNovoContato = (input('Nome: '))
            numeroNovoContato = (input('Numero: '))
            emailNovoContato = (input('Email: '))
            twiterNovoContato = (input('Twiter: '))
            instagramNovoContato = (input('Instagram: '))
            qtd -=1
            adicionarContato(nomeNovoContato, numeroNovoContato, emailNovoContato, twiterNovoContato, instagramNovoContato, qtd)

    # sair
    elif entrada == 0:
        def sair():
            sair = 0
    # pesquisar contato
    elif entrada == 2:
        recuperarContato()
    elif entrada == 3:
        removerContato()
    elif entrada == 4:
        editarContato()
    elif entrada == 5:
        relatorio()

# menu de opcoes
def menu():
    print(" 1:Inserir novo contato\n", "2:Pesquisar contato\n", "3:Remover contato\n", "4:Editar contato\n", "5:Relatório\n", "6:Mostrar em ordem\n", "0:Sair")
    ent()
menu()



