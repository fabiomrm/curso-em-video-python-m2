#Programa que lê o primeiro termo e a razão de uma PA
#Depois mostre os 10 primeiros termos dessa PA
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo10 = termo1 + 9 * razao
print(f'PROGRESSÃO ARITMÉTICA\na1 = {termo1} \nrazão = {razao}')
print('-=' * 11)
print('Os 10 primeiros termos da PA são:')
for c in range(termo1, termo10 + 1, razao):
    print(c, end=' ')
