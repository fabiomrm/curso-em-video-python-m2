#Programa que lê nome e preço de vários produtos. Pergunta se o usuário vai continuar
#Ao final mostra:
#1. Total gasto na compra
#2. Quantos produtos > R$ 1000,00
#3. Nome do produto mais barato
soma = cont_mais_de_1000 = cont_produto = menor = 0
while True:
    print('-='*20)
    print('NOVO PRODUTO')
    nome = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$ '))
    cont_produto += 1
    if preço > 1000:
        cont_mais_de_1000 += 1
    soma += preço
    if cont_produto == 1:
        menor = preço
        produto_barato = nome
    else:
        if preço < menor:
            menor = preço
            produto_barato = nome
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break
print(f'O total de compra foi \033[1;33mR$ {soma:.2f}\033[m')
print(f'Temos \033[1;33m{cont_mais_de_1000}\033[m produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato é \033[1;33m{produto_barato}\033[m. Ele custa \033[1;33mR$ {menor:.2f}\033[m')

