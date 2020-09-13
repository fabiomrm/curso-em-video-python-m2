#Programa que pede dois números e mostra menu com as opções:
# 1 somar - 2 multiplicas - 3 maior - 4 novos números - 5 sair do programa
num_menu = 0
while num_menu != 5:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('MENU DE AÇÕES \n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR')
    num_menu = int(input('Digite o que você deseja fazer: '))
    if num_menu == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}')
    elif num_menu == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif num_menu == 3:
        if num1 > num2:
            print(f'O maior número entre {num1} e {num2} é {num1}')
        elif num1 < num2:
            print(f'O maior número entre {num1} e {num2} é {num2}')
        else:
            print(f'Os dois números são iguais.')
    elif num_menu == 4:
        print('OK! Escolha novos números')
    else:
        print('Comando inválido. Favor escolher dentre as opções do menu')
print('SAINDO')
