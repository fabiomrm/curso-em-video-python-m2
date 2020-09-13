#Melhorar o desafio 58: Jogo da adivinhação
#Computador pensa em um número de 0 a 10,
#jogador chuta até acerta e o computador mostra quantas tentativas foram necessárias
from random import randint
print('\033[7;33;41m====BEM VINDO AO JOGO DA ADIVINHAÇÃO!====\033[m')
print('Acabei de pensar em um número entre 0 e 10, vamos ver se você descobre qual foi:')
num = randint(0, 10)
chute = int(input('Vamos lá! Digite um número: '))
cont = 1
while chute != num:
    chute = int(input('Não foi esse! Tente novamente: '))
    cont = cont + 1
print(f'ACERTOU! Pensei no número {chute} e e você levou {cont} tentativas para acertar')

