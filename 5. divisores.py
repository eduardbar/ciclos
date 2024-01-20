n = int(input("ingrese numero: \n"))

divisores = []

for a in range(1, n + 1):
    if n % a == 0:
        divisores.append(a)

print (*divisores)