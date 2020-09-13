#Tabuada
num = int(input('Digite um número: '))
print(f'\033[36mTABUADA DO {num}\033[m')
for c in range(0, 11):
    print(f'{num}x{c} = {num * c}')
print('FIM')