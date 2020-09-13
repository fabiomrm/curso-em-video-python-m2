#Lê o sexo de uma pessoa, mas só aceita M ou F. Se digitar outro valor, pede para digitar novamente
sexo = str(input('Digite seu sexo M/F: ')).strip().upper()
erro = 0
if sexo == 'M' or sexo == 'F':
    print('Registrado.')
else:
    while erro != 'M' and erro != 'F':
        erro = str(input('Inválido! Digite seu sexo: ')).strip().upper()
    print('Registrado.')






