
continuar = True
lista_contatos = []

while continuar:
    opcao = input('''
        - MENU da agenda:
          Informe a ação que deseja:
          1 - Cadastrar
          2 - Listar
          3 - Editar
          4 - Excluir
          5 - Sair
    ''')

    if opcao == '1':
        contato = {}
        contato['nome'] = input('Informe um nome: ')
        contato['telefone'] = input('Informe um telefone: ')
        lista_contatos.append(contato)

    elif opcao == '2':
        for item in lista_contatos:
            print('Nome: ', item['nome'])
            print('Telefone: ', item['telefone'])
            print('=========================')
    elif opcao == '3':
        pesquisa = input('Informe um nome para editar: ')
        for item in lista_contatos:
            if item['nome'] == pesquisa:
                item['nome'] = input('Informe um novo nome: ')
                item['telefone'] = input('Informe um novo telefone: ')
    elif opcao == '4':
        pesquisa = input('Informe um nome para excluir: ')
        for item in lista_contatos:
            if item['nome'] == pesquisa:
                lista_contatos.remove(item)

    elif opcao == '5':
        print('Saindo')
        continuar = False
    else:
        print('Opção inválida')

