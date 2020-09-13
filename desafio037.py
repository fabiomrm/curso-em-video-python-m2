#Programa que lê um número inteiro, pergunta para o usuário base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal
num = int(input('Digite um número inteiro: '))
conversoes = ('binário', 'octal', 'hexadecimal')
print('''Escolha uma base para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
base = int(input('Sua opção: '))
if base == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')



