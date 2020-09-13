#Fatorial
print('\033[1;34mCALCULADORA DE FATORIAL\033[m')
n = int(input('Digite o número: '))
num = n
acum = 1
print(f'\033[1;34m{num}!\033[m = ', end='')
while n >= 1:
    acum = n * acum
    print(f'\033[1;34m{n}\033[m', end=' = ')
    n = n - 1
print(f'\033[4;33m{acum}\033[m')





