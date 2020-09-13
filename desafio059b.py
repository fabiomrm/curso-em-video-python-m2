#Programa que pede dois números e mostra menu com as opções:
# 1 somar - 2 multiplicas - 3 maior - 4 novos números - 5 sair do programa
num_menu = 0
while num_menu != 5:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('MENU DE AÇÕES \n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR')
    num_menu = int(input('Digite o que você deseja fazer: '))
    for num_menu in range(1,4):
