#Palíndromo
frase = str(input('Digite a frase: ')).upper().strip().split()
a = ''.join(frase)
tot = 0
for c in range(0, len(a)):
    if a[len(a) - 1 - c] == a[c]:
        tot = tot + 1
if tot == len(a):
    print('A frase {} é um palíndromo.'.format(' '.join(frase)))
else:
    print('A frase {} não é um palíndromo.'.format(' '.join(frase)))