#Lê nome, idade e sexo de 04 pessoas. No final deve mostrar:
#1. A média de idade do grupo
#2. O nome do homem mais velho
#3. Quantas mulheres são maiores de idades
contmedia = 0
maior = 0
nomemaior = str()
cont_maior_idade = 0
cont_menor_idade = 0
for c in range(1, 5):
    print(f'------\033[1;33m{c}ª PESSOA\033[m------')
    nome = str(input('Digite nome: ')).upper().strip()
    sexo = str(input('M/F: ')).upper().strip()
    idade = int(input('Digite idade: '))
    contmedia = contmedia + idade

    if sexo == 'M':
        if c == 1:
            maior = idade
            nomemaior = nome
            menor = idade
        else:
            if idade > maior:
                maior = idade
                nomemaior = nome
    elif sexo == 'F':
        if idade >= 18:
            cont_maior_idade = cont_maior_idade + 1
        else:
            cont_menor_idade += cont_menor_idade
    elif sexo == 'OUTRO':
        print('Favor informar sexo para acrescentarmos ao banco de dados!')
#1. Média de idades do grupo
print(f'A média das idades é: {contmedia/c} anos.')
print('='*30)
#2. Nome do homem mais velho
print(f'A idade do homem mais velho é: {maior}')
print(f'O nome do homem mais velho é: {nomemaior}')
print('='*30)
#3. Mulheres maiores de idade
print(f'Quantidades de mulheres maiores de idade: {cont_maior_idade}')
