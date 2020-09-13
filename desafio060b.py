#fatorial usando "for"

n = int(input('Digite um número: '))
acum = 1
for c in range(n, 0, -1):
    acum = c * acum
print(acum)