from random import randint
from time import sleep

#Adicionando Cores.
cores = {'limpa': '\033[m',
        'azul': '\033[34m',
        'vermelho': '\033[31m',
        'amarelo': '\033[33m',
        'verde': '\033[32m',
        'pretoebranco:': '\033[7;30m'
}

#Fazendo o computador 'PENSAR'.
computador = randint(0,5) #Faz o computador 'PENSAR'.
print('--' * 30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinha...')
print('--' * 30)

#Fazendo o jogador adivinhar.
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar.
print(f'{cores['verde']}PROCESSANDO...{cores['limpa']}')
sleep(1.5)
if jogador == computador:
    print(f'{cores['amarelo']}PARABENS!{cores['limpa']} voce consegui me vencer!')
else:
     print('GANHEI! Eu pensei no numero {}{}{} nao no {}{}{}'.format(
        cores['vermelho'], computador,cores['limpa'],
        cores['azul'], jogador, cores['limpa']))
