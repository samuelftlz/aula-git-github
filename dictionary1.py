aluno = {}
aluno['nome'] = input('digite o nome: ')
aluno['media'] = float(input(f'media do {aluno["nome"]}: '))

if (aluno['media'] >= 7):
    print('aprovado')
else:
    print('reprovado')
print(aluno)
