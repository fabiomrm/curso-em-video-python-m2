#desafio 61, mas depois de mostrar 10 termos, pergunta se o usuário quer ver mais termos
#e quantos ele quer ver. O programa para quando ele diz 0 termos
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    termo = a1 + cont * r
    cont = cont + 1
    print(termo, end=' ')
cont3 = 0
pergunta = 1
termo = termo + r
while pergunta != 0:
    pergunta = int(input('Gostaria de ver mais quantos números? Caso não queira, aperte 0'))
    cont2 = 0
    while cont2 < pergunta:
        termo2 = - termo + cont3 * r
        print(int(- termo2), end=' ')
        cont2 = cont2 + 1
        cont3 = ((termo2 + termo - r)/r)
print('Ok! Parando de exibir a sequência')










