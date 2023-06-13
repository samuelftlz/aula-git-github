import openai
def menu_modulo(logado):
    print('\n    Você', logado, 'está atualmente logado')
    modulo = ('''
     =-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=-=
     #  Bem vindo! Escolha uma das opções abaixo ! #
     #  1) Cadastro                                # 
     #  2) Logar como vendedor                     # 
     #  3) Logar como cliente                      #
     #  4) Deslogar                                #   
     #  5) Listar usuario                          #
     #  6) Sair                                    #
     =-=-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=
                            |
                            |
                            |
     ================================================
    ##################################################
    #[][][][][][][][][][][][][][][][][][][][][][][][]#
    #[][][][][][][][][][][][][][][][][][][][][][][][]#
    ##################################################
    ''')
    print(modulo)

def cadastrar_usuario(vendedor, cliente):
    verificar = True
    while verificar == True:

        nome = input('Digite seu login(No minimo 6 caractere): ')
        senha = int(input('Digite sua senha(Em numero): '))
        tamanho = len(nome)

        for i in vendedor.copy():
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
                cliente[nome] = [senha, []]
                cont = 0
                verificar = False

def logar_vendedor(vendedor, login):
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
                print('Você realizou login com exito!')
                login = True
                verificar = False
                checar = True
                nome = usuario
                return usuario


            if checar == False:
                conf = input('Login inválido deseja tentar denovo? (S/N): ')

            if conf in 'Ss':
                print('Retornando...')
                cont = 0

            elif conf in 'Nn':
                print('Retornando...')
                verificar = False
                cont = 0

def logar_cliente(cliente, login):
    cont = 0
    verificar = True
    checar = False
    while verificar == True:

        if login == True:
            print('Você já está logado, redirecionando...')
            break

        usuario = input('Digite seu login: ')
        senha = int(input('Digite sua senha(Em numero): '))

        for i in cliente:

            if (i == usuario and cliente[i][0] == senha):
                cont += 1
                print('Você realizou login com exito!')
                login = True
                verificar = False
                checar = True
                nome = usuario
                if cont == 1:
                    return nome


            if checar == False:
                conf = input('Login inválido deseja tentar denovo? (S/N): ')

                if conf in 'Ss':
                    print('Retornando...')
                    cont = 0

                elif conf in 'Nn':
                    print('Retornando...')
                    verificar = False
                    cont = 0

def deslogar_vendedor(login):
    if login == True:
        print('Deslogando...')
        return True
    else:
        print('Erro! Você precisa estar logado para realizar esta ação')
        return False
def menu_loja():
    menu = ('''
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
       ''')
    print(menu)

def menu_cliente():
    modulo = ('''
     =-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=-=
     #  Bem vindo! Escolha uma das opções abaixo ! #
     #  1) Buscar Produto                          # 
     #  2) Comprar Produto                         # 
     #  3) Listar Compras                          #
     #  4) Consultar ChatGPT                       #   
     #  5) Retornar                                #
     =-=-=-=-=-=-==-=-=-=-=Menu-=-=-=-=-=-==-=-=-=-=
                            |
                            |
                            |
     ================================================
    ##################################################
    #[][][][][][][][][][][][][][][][][][][][][][][][]#
    #[][][][][][][][][][][][][][][][][][][][][][][][]#
    ##################################################
    ''')
    print(modulo)

def atualizar_senha(vendedor, nome):
    for i in vendedor:
        if i == logar_vendedor(vendedor, nome):
            senha = int(input('Digite a nova senha que deseja colocar: '))
            vendedor[i][0] = senha
            print('Senha alterada com sucesso!')
            print(vendedor)
            break

def cadastrar_produto(vendedor, nome):
    for i in vendedor:
        if i == logar_vendedor(vendedor, nome):
            produto = input('Digite o nome do produto que deseja cadastrar: ')
            preco = float(input('Digite o preco do produto: '))
            quantidades = int(input('Digite a quantidade do produto: '))
            descricao = input('Digite a descrição do produto: ')
            vendedor[i][1].append(produto)
            vendedor[i][1].append(str(preco))
            vendedor[i][1].append(str(quantidades))
            vendedor[i][1].append(descricao)
            print('Produto cadastrado com exito!')
            print(*vendedor[i][1])

def remover_produto(vendedor,nome):
    cont = 0
    busca = input('Digite o produto que deseja remover: ')
    for i in vendedor:
        if i == logar_vendedor(vendedor, nome):
            lista = vendedor[i][1]
            for d in lista:
                if d.find(busca) >= 0:
                    index = lista.index(d)
                    print(f'{d} - {index}')
                    cont += 1
                else:
                    cont += 1
                    if cont == len(lista):
                        cont = 0
                        remover = int(input('Digite o codigo do produto que deseja remover: '))
                        for i in range(3):
                            lista.pop(remover)
                        print('Produto removido com sucesso!')

def buscar_produto(vendedor, nome):
    cont = 0
    busca = input('Digite o produto que deseja buscar: ')
    for i in vendedor:
        if i == logar_vendedor(vendedor, nome):
            lista = vendedor[i][1]
            for d in lista:
                if d.find(busca) >= 0:
                    cont += 1
                    print(f'Produto - {d}')
                    if cont == len(lista):
                        cont = 0
                        break

def atualizar_produto(vendedor, nome):
    cont = 0
    busca = input('Digite o produto que deseja atualizar: ')
    for i in vendedor:
        if i == logar_vendedor(vendedor, nome):
            lista = vendedor[i][1]
            for d in lista:
                if d.find(busca) >= 0:
                    index = lista.index(d)
                    print(f'{d} - {index}')
                    cont += 1
                else:
                    cont += 1
                    if cont == len(lista):
                        cont = 0
                        codigo = int(input('Digite o nome do codigo do produto: '))
                        atualizar = input('Digite o nome do novo produto: ')
                        at_preco = input('Digite um novo preco: ')
                        at_quantidade = input('Digite um nova quantidade: ')
                        lista[codigo] = atualizar
                        codigo += 1
                        lista[codigo] = at_preco
                        codigo += 1
                        lista[codigo] = at_quantidade
                        print(lista)
                        break

def listar_produtos(vendedor, nome):
    for i in vendedor:
        if i == logar_vendedor(vendedor, nome):
            lista = vendedor[i][1]
            print('Produtos:', *lista)

def comprar_produtos(cliente, nome, compras, vendedor):
    cont = 0
    busca = input('Digite o produto que deseja comprar: ')
    for i in cliente:
        if i == logar_cliente(cliente, nome):
            for c in vendedor:
                lista = vendedor[c][1]
                for d in lista:
                    if d.find(busca) >= 0:
                        index = lista.index(d)
                        print(f'{d} - {index}')
                        cont += 1
                    else:
                        cont += 1
                if cont == len(lista):
                    cont = 0
                    comprar = int(input('Digite o codigo do produto que deseja comprar: '))
                    quant = lista[comprar + 2]
                    num = int(quant)
                    num -= 1
                    if num < 0:
                        print('Produto fora de estoque!')
                    else:
                        lista[comprar + 2] = str(num)

                        for i in range(comprar, comprar + 3):
                            if lista[comprar] in compras and lista[comprar + 1] in compras and lista[comprar + 2] in compras:
                                cont += 1
                                if cont == 3:
                                    break
                            elif i != comprar + 2:
                                compras.append(lista[i])
                            elif i == comprar + 2:
                                compras.append('1')
                                cont += 1
                        if cont == 3:
                            pos = compras[comprar + 2]
                            contador = int(pos)
                            if contador >= 1:
                                quantidade = compras[comprar + 2]
                                numero = int(quantidade)
                                numero += 1
                                compras[comprar + 2] = str(numero)
                    print('Produto comprado!')
                    print(compras)

def listar_compras(compras, cliente, nome):
    for i in cliente:
        if i == logar_cliente(cliente, nome):
            print('Compras realizadas:')
            print(compras)

def consultarchatgpt(cliente, vendedor, nome):
    busca = input('Digite o produto que deseja consultar: ')
    cont = 0
    openai.api_key = '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'
    model_engine = "text-davinci-003"
    max_tokens = 1024



    for i in cliente:
        if i == logar_cliente(cliente, nome):
            for c in vendedor:
                lista = vendedor[c][1]
                for d in lista:
                    if d.find(busca) >= 0:
                        index = lista.index(d)
                        print(f'{d} - {index}')
                        cont += 1
                    else:
                        cont += 1
                if cont == len(lista):
                    cont = 0
                    comprar = int(input('Digite o codigo do produto que deseja consultar: '))

                    prompt = 'me diga resumidamente o que você acha do produto:' + lista[comprar] + 'e a  descrição:' + lista[comprar + 3] + '?'


                    completion = openai.Completion.create(
                        engine=model_engine,
                        prompt=prompt,
                        max_tokens=max_tokens,
                        temperature=0.5,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )

                    # Print the response
                    print(completion.choices[0].text)



def retornar(compras):
    print('Retornando...')
    compras.clear()