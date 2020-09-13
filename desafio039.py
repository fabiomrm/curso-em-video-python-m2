#Programa que lê o ano de nascimento de uma pessoa e diz:
#se é hora de se alistar, se já passou do tempo e o prazo para se alistar
import datetime
ano = int(input('Digite o ano do seu nascimento: '))
alistou = str(input('Você já se alistou? ')).strip().upper()
hoje = datetime.date.today().year
idade = hoje - ano
if (idade) >= 18 and alistou == 'SIM':
    print(f'Tudo certo! Você já está com tudo regularizado há {idade - 18} anos')
elif (idade) >= 18 and alistou == 'NÃO':
    print(f'Regularizar situação! Você está fora do prazo há {idade - 18} anos')
elif (idade) <= 18 and alistou == 'SIM':
    print(f'Tudo certo! Mesmo antes dos 18 anos, sua situação já está regularizada')
else:
    print(f'Atenção para não perder o prazo! Você deve se alistar daqui a {18 - idade} anos')




