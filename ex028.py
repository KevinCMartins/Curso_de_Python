from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador 'PENSAR'.
print('--' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinha...')
print('--' * 30)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} nao no {}'.format(computador, jogador))