from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-'*20)
print('vou pensar em um numero de 0 a 10 tente advinhar')
print('-=-'*20)
jogador = int(input('em que numero eu pensei? '))
print('Processando...')
sleep(4)
if jogador == computador:
    print('parabens')
else:
    print('eu ganhei eu pensei em {} e nao em {}'.format(computador, jogador))
