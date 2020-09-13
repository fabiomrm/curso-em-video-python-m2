#Programa que jogue pedra,papel e tesoura
from random import choice
import time
import emoji
jogar = str(input((emoji.emojize('\033[1;36mVAMOS JOGAR \033[7;33m:punch:\033[m, \033[7;35m:page_facing_up:\033[m E \033[7;31m:scissors:\033[m?\033[m ', use_aliases=True)))).strip().upper()
if jogar == 'SIM':
    print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
    sua_escolha = int(input('Qual a sua jogada? '))
    print('-=' * 10)
    if sua_escolha == 0:
        sua_escolha2 = 'PEDRA'
    elif sua_escolha == 1:
        sua_escolha2 = 'PAPEL'
    elif sua_escolha == 2:
        sua_escolha2 = 'TESOURA'
    print('JO..')
    time.sleep(1)
    print('KEN..')
    time.sleep(1)
    print('PO!!')
    print('\033[1;31m-=\033[m' * 10)
    computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
    print(f'EU ESCOLHI: {computador}\nVOCÊ ESCOLHEU: {sua_escolha2}')
    print('\033[1;31m-=\033[m' * 10)
    if computador == 'PEDRA' and sua_escolha == 1:
        print(str('VOCÊ VENCEU!'))
    elif computador == 'PEDRA' and sua_escolha == 2:
        print(str('GANHEI!'))
    elif computador == 'PAPEL' and sua_escolha == 0:
        print(str('GANHEI!'))
    elif computador == 'PAPEL' and sua_escolha == 2:
        print(str('VOCÊ VENCEU!'))
    elif computador == 'TESOURA' and sua_escolha == 0:
        print(str('VOCÊ VENCEU!'))
    elif computador == 'TESOURA' and sua_escolha == 1:
        print(str('GANHEI!'))
    else:
        print(str('\033[1;34mEMPATE!\033[m'))
elif jogar == 'NÃO':
    print(emoji.emojize('Que pena! :cry:', use_aliases=True))
else:
    print('Po meu amigo, é sim ou não! ')








