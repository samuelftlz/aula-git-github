vendedor = {'samuel': [123456, []]}
logado = ''
nome = ''
cont = 0
modulo = 3
verificar = True
login = False
entrou = False
ja_cadastrado = False

while True:

    if login == False:
        logado = 'não'

    elif login == True:
        logado = ''

    print('\n    Você', logado, 'está atualmente logado')
    modulo = input('''
    =-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=-=
    #  Bem vindo! Escolha uma das opções abaixo ! #
    #  1) Cadastro                                # 
    #  2) Logar                                   # 
    #  3) Deslogar                                #
    #  4) Listar usuários                         #   
    #  0) Sair                                    #
    =-=-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=
                           |
                           |
                           |
    ================================================
   ##################################################
   #[][][][][][][][][][][][][][][][][][][][][][][][]#
   #[][][][][][][][][][][][][][][][][][][][][][][][]#
   ##################################################
   Digite: ''')

    if (modulo == '1'):
        verificar = True
        while verificar == True:

            nome = input('Digite seu login(No minimo 6 caractere): ')
            senha = int(input('Digite sua senha(Em numero): '))
            tamanho = len(nome)

            for i in vendedor:
                ja_cadastrado = False
                if i == nome:
                    print('Erro, usuário já cadastrado!')
                    ja_cadastrado = True
                    checar = True
                    while checar == True:
                        confirm = input('Deseja tentar denovo?(S/N): ')

                        if confirm in ('Ss'):
                            print('Retornando...')
                            checar = False
                        elif confirm in ('Nn'):
                            print('Retornando...')
                            checar = False
                            verificar = False
                        else:
                            print('Valor inválido tente novamente!')

            if tamanho < 6:
                print('Tamanho invalido')

            elif (tamanho >= 6 and ja_cadastrado == False):
                print('Cadastrado com sucesso.')
                vendedor[nome] = [senha, []]
                cont = 0
                verificar = False



    elif (modulo == '2'):
        verificar = True
        checar = False
        while verificar == True:

            if login == True:
                print('Você já está logado, redirecionando...')
                entrou = True
                break


            usuario = input('Digite seu login: ')
            senha = int(input('Digite sua senha(Em numero): '))

            for i in vendedor:

                if (i == usuario and vendedor[i][0] == senha):
                    cont = 0
                    print('Você realizou login com exito!')
                    login = True
                    verificar = False
                    entrou = True
                    checar = True
                    nome = usuario
                    break

            if checar == False:
                conf = input('Login inválido deseja tentar denovo? (S/N): ')

                if conf in 'Ss':
                    print('Retornando...')
                    cont = 0

                elif conf in 'Nn':
                    print('Retornando...')
                    verificar = False
                    cont = 0

            cont = 0
        while entrou == True:
            menu = input('''
    =-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=-=
    #  Bem vindo! Escolha uma das opções abaixo ! #
    #  1) Atualizar senha                         # 
    #  2) Cadastrar produto                       # 
    #  3) Remover produto                         #
    #  4) Buscar produto                          #   
    #  5) Atualizar produto                       # 
    #  6) Listar produtos                         #
    #  7) Retornar                                #
    =-=-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=
                           |
                           |
                           |
     ==============================================
   ##################################################
   #[][][][][][][][][][][][][][][][][][][][][][][][]#
   #[][][][][][][][][][][][][][][][][][][][][][][][]#
   ##################################################
   Digite: ''')

            if menu == '1':
                for i in vendedor:
                    if i == nome:
                        senha = int(input('Digite a nova senha que deseja colocar: '))
                        vendedor[i][0] = senha
                        print('Senha alterada com sucesso!')
                        print(vendedor)
                        break
            elif menu == '2':
                for i in vendedor:
                    if i == nome:
                        produto = input('Digite o nome do produto que deseja cadastrar: ')
                        vendedor[i][1].append(produto)
                        print('Produto cadastrado com exito!')
                        print(vendedor[i][1])


            elif menu == '3':

                busca = input('Digite o produto que deseja remover: ')
                for i in vendedor:
                    if i == nome:
                        lista = vendedor[i][1]
                        for d in lista:
                            if d.find(busca) >= 0:
                                index = lista.index(d)
                                print(f'{d} - {index}')
                                cont += 1
                                if cont == len(lista):
                                    cont = 0
                                    remover = int(input('Digite o codigo do produto que deseja remover: '))
                                    lista.pop(remover)
                                    print('Produto removido com sucesso!')


            elif menu == '4':
                busca = input('Digite o produto que deseja buscar: ')
                for i in vendedor:
                    if i == nome:
                        lista = vendedor[i][1]
                        for d in lista:
                            if d.find(busca) >= 0:
                                cont += 1
                                print(f'Produto - {d}')
                                if cont == len(lista):
                                    cont = 0
                                    break

            elif menu == '5':

                busca = input('Digite o produto que deseja atualizar: ')
                for i in vendedor:
                    if i == nome:
                        lista = vendedor[i][1]
                        for d in lista:
                            cont += 1
                            if d.find(busca) >= 0:
                                index = lista.index(d)
                                print(f'{d} - {index}')
                                if cont == len(lista):
                                    cont = 0
                                    codigo = int(input('Digite o nome do codigo do produto: '))
                                    atualizar = input('Digite o nome do novo produto: ')
                                    lista[codigo] = atualizar
                                    print(lista)
                                    break
                            elif d.find(busca) < 0:
                                print('...')
                                break



            elif menu == '6':
                for i in vendedor:
                    if i == nome:
                        lista = vendedor[i][1]
                        print('Produtos:', *lista)

            elif menu == '7':
                print('Retornando...')
                entrou = False


            else:
                print('Você digitou uma ação inválida, tente novamente!')



    elif modulo == '3':
        if login == True:
            print('Deslogando...')
            login = False
        else:
            print('Erro! Você precisa estar logado para realizar esta ação')
    elif modulo == '4':
        print('\n Usuários:', *vendedor)

    else:
        print('Você digitou uma ação inválida, tente novamente!')