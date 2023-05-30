from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1,6),
        'jogador4': randint(1, 6)}
ranking = dict()
print('Valores sorteados')

for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' *30)

for x, y in enumerate(ranking):
    print(f'{x+1}ª lugar --> {y[0]} com {y[1]}')
    sleep(1)