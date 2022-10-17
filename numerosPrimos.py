mult = 0
lista = []

for n in range(0, 100):

    for count in range(2, n):
        if (n % count == 0):
            mult += 1

    if (mult == 0):
        lista.append(n)
    else:
        mult = 0

print(lista)