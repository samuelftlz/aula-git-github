from pacote_vendedor import *

vendedor = {'samuel': [123456, ['manga', '2.0', '6', 'fruta']]}
cliente = {'samuel': [123456, []]}
compras = []
logado = ''
nome = ''
cont = 0
modulo = 3
verificar = True
login = False
entrou = False
ja_cadastrado = False
entrou_cliente = False

while True:

    if login == False:
        logado = 'não'

    elif login == True:
        logado = ''
    menu_modulo(logado)
    modulo = input('Digite a opcao que deseja: ')

    if (modulo == '1'):
        cadastrar_usuario(vendedor, cliente)

    elif (modulo == '2'):
        logar_vendedor(vendedor, nome)
        entrou = True
        login = True

        while entrou == True:
            menu_loja()
            menu = input('Digite a opcao que voce deseja: ')

            if menu == '1':
                atualizar_senha(vendedor, nome)

            elif menu == '2':
                cadastrar_produto(vendedor, nome)

            elif menu == '3':
                remover_produto(vendedor, nome)

            elif menu == '4':
                buscar_produto(vendedor, nome)

            elif menu == '5':
                atualizar_produto(vendedor, nome)

            elif menu == '6':
                listar_produtos(vendedor, nome)

            elif menu == '7':
                retornar()
                entrou = False

            else:
                print('Você digitou uma ação inválida, tente novamente!')

    elif (modulo == '3'):
        logar_cliente(cliente, login)
        entrou_cliente = True
        login = True

        while entrou_cliente == True:
            menu_cliente()
            menu = input('Digite a opção que deseja: ')

            if menu == '1':
                buscar_produto(vendedor, nome)
            elif menu == '2':
                comprar_produtos(cliente, nome, compras, vendedor)
            elif menu == '3':
                listar_compras(compras, cliente, nome)
            elif menu == '4':
                consultarchatgpt(cliente, vendedor, nome)

            elif menu == '5':
                retornar(compras)
                entrou_cliente = False
            else:
                print('Você digitou informação inválida!')

    elif modulo == '4':
        deslogar_vendedor(login)
        if deslogar_vendedor(login) == True:
            login = False

    elif modulo == '5':
        print('\n Vendedores:', *vendedor)
        print('\n Clientes:', *cliente)

    elif modulo == '6':
        print('Até mais!')
        break

    else:
        print('Você digitou uma ação inválida, tente novamente!')