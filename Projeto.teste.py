pessoas = [['felipe', 19, 9999], ['pedro', 23, 11111],
           ['caiqui',22,7777], ['peterson',18,7777]]

op = 99
while(op != 0):
    print('\n\n--------MENU----------\n')
    print('1-cadastrar pessoa')
    print('2-listar pessoas')
    print('3-buscar uma pessoa')
    print('4-Calcular media de idades')
    print('5-Remover pessoa')
    print('6-Atualizar pessoa')
    print('7-Aumentar salario das pessoas > 50 anos')
    print('0-sair')

    op = int(input('digite a opcao desejada: '))

    if(op == 1):
        nome = input('digite seu nome: ')
        idade = int(input('digite sua idade: '))
        sal = float(input('digite seu salario: '))

        pessoas.append([nome, idade, sal])

        print('Cadastro feito com sucesso!')

    elif(op == 2):
        print('\nNome - idade - salario')
        for p in pessoas:
            print(f'{p[0]} - {p[1]} - {p[2]}')

    elif(op == 3):
        busca = input('digite o nome para pesquisa ')
        entrou = False

        for pessoa in pessoas:
            if(pessoa[0].find(busca) >= 0):
                print(pessoa[0])
                entrou = True

        if(entrou == False):
            print('nao foi encontrado nenhum usuario com esse nome')

    elif(op == 4):

        soma = 0
        for pessoa in pessoas:
            soma = soma + pessoa[1]
        media = soma / len(pessoas)
        print('-------------------')
        print(f'Media de idades: {media}')

    elif(op == 5):
        busca = input('digite o nome da pessoa que vc quer remover')
        removidos = []

        for pessoa in pessoas:
            if(pessoa[0].find(busca) >= 0):
                removidos.append(pessoa)

        for pes in removidos:
            pessoas.remove(pes)


    elif(op == 6):
        busca = input('digite o nome da pessoa para atualizar')

        for i in range(len(pessoas)):
            if(pessoas[i][0].find(busca) >= 0):
                print(f'\nvoce vai atualizar {pessoas[i][0]}')
                resp = input('-digite sim para atualizar ou não caso contrario')
                if(resp == 'sim'):
                    nome = input('digite o nome para atualizar')
                    idade = int(input('digite a idade para atualizar'))
                    salario = float(input('digite o salario para atualizar'))

                    pessoas[i] = [nome, idade, salario]
                    print('Pessoa atualizada com sucesso')



    elif (op == 7):
        for ind in range(len(pessoas)):
            idade = pessoas[ind][1]

            if(idade > 50):
                novo_sal = pessoas[ind][2] * 1.15
                pessoas[ind][2] = novo_sal
                print('Salario Atualizado')
                print(f'{pessoas[ind][0]}: {novo_sal}')

    elif (op < 0):
        print('\nErro, informe um valor valido. ')
    elif (op == 0):
        print('\nVoce saiu!')