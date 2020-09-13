#Programa que lê idade e o sexo de várias pessoas, perguntando se o usuário quer cadastrar novos
#ao final mostra:
#1. Quantas pessoas tem + 18 anos
#2. Quantos homens cadastrados
#3. Quantas mulheres < 20 anos
contidade = 0
conthomem = 0
contmulher = 0
sexo = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Digite sexo [M/F]: ')).strip().upper()
    print('-='*20)
    check = str(input('Quer continuar [S/N]? ')).strip().upper()
    while check not in 'SN':
        check = str(input('Quer continuar [S/N]? ')).strip().upper()
    print('-=' * 20)
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F':
        if idade > 20:
            contmulher +=1
    if check == 'N':
        break
print(f'Foram cadastradas {contidade} pessoas maior de idade')
print(f'Foram cadastrados {conthomem} homens')
print(f'Foram cadastradas {contmulher} mulheres com mais de 20 anos')



