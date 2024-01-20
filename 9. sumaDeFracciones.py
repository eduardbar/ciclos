potencia = 1
fraccion = 1.0
suma = 0.0

print("{:<10} {:<10} {:<10}".format("Potencia", "Fraccion", "Suma"))

while fraccion > 0.000001:
    fraccion /= 2
    suma += fraccion
    print("{:<10} {:<10} {:<10}".format(potencia, fraccion, suma))
    potencia += 1