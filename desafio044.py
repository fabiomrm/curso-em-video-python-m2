#Programa que calcula o valor a ser pago por um produto
#À vista (dinheiro ou cheque): 10% de desconto
#À vista (cartão): 5% de desconto
#Parcelado em até 2x: preço normal
#Parcelado em 3x ou mais: juros 20%
print(str('\033[33m###\033[4;36mCÁLCULO DO VALOR A SER PAGO\033[m\033[33m###\033[m'))
preço = float(input('Digite o preço do produto: R$ '))
forma_de_pagamento = str(input('Insira a forma de pagamento: ')).strip().upper()
if forma_de_pagamento == 'DINHEIRO':
    print(f'Valor do produto (\033[4m10% de desconto\033[m): \033[1;36mR$ {(preço*0.9):.2f}\033[m')
elif forma_de_pagamento == 'CHEQUE':
    print(f'Valor do produto (\033[4m10% de desconto\033[m): \033[1;36mR$ {(preço*0.9):.2f}\033[m')
elif forma_de_pagamento == 'CARTÃO':
    parcelas = int(input('Número de parcelas (até 12): x'))
    if parcelas == 1:
        print(f'Valor do produto (\033[4m5% de desconto\033[m):\033[1;36m R$ {(preço * 0.95):.2f}\033[m')
    elif parcelas == 2:
        print(f'Valor do produto (\033[4msem desconto\033[m):\033[1;36m R$ {preço:.2f}\033[m')
    elif 3 <= parcelas <= 12:
        print(f'Valor do produto (\033[4m20% de juros\033[m):\033[1;36m R$ {(preço * 1.2):.2f}\033[m')
    else:
        print('\033[4;31mMÁXIMO DE PARCELAS PERMITIDAS: x12!\033[m')
else:
    print('\033[4;31mFavor inserir forma de pagamento válida!\033[m')

