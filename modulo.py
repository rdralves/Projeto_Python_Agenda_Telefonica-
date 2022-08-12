# Todos os métodos estarão aqui

class bd:
    def criaBD(self):
        arquivo = open("bancoDados.txt", "w")
        arquivo.close()


def menuPrincipal():
    print("Agenda Telefonica\n")
    print('Qual serviço deseja realizar.\n\n1.) Cadastrar Contato\n2.) Consultar Contato.\n3.) Sair ')
    op = int(input("\n> "))

    if op == 1:
        cadastrarContato()
    elif op == 2:
        consultaContato()
    elif op == 3:
        sair = int(input("Deseja Sair da Agenda?\n1.) Sim.\n2.) Não."))
        if sair == 1:
            print("Obrigado...\nFinalizando..\n")
        elif sair == 2:
            menuPrincipal()


def cadastrarContato():
    nome = input("Entre com o seu Nome:...\n")
    telefone = input("Digite o telefone a ser salvo:.\n")

    with open("bancoDados.txt", "a") as arquivo:
        arquivo.write(nome.title() + ", ")
        arquivo.write(telefone)
        arquivo.write("\n")

        menuPrincipal()


def consultaContato():
    decisao = int(input("Qual consulta?\n1.) Completa\n2.) Única\n> "))

    if (decisao == 1):
        arquivo = open("bancoDados.txt").readlines()
        arquivo = [str(x).rstrip() for x in arquivo]
        for linha in arquivo:
            print(linha)
        menuPrincipal()
    # Listagem unica do bd de contatos
    if (decisao == 2):
        nomeContatoConsulta = input("Qual nome? ").title()

        arquivo = open("bancoDados.txt").readlines()

        arquivo = [str(x).rstrip() for x in arquivo]
        for linha in arquivo:
            lista = linha.split(",")

            if nomeContatoConsulta.title() in lista:
                print("Contato Encontrado.")
                print(f"Nome: {lista[0]}\nTelefone: {lista[1]}\n")

                op = int(input("Fazer outra Consulta:."))

                if op == 1:
                    consultaContato()
                if op == 2:
                    menuPrincipal()
            else:
                print("Contato não encontrado.\nDeseja cadastrar\n1.) Sim.\n2.) Não.\n ")
                op = int(input(">"))
                if op == 1:
                    cadastrarContato()
                    break
                else:
                    menuPrincipal()
                    break
