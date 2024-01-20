def dibujar_hexagono(lado):
    for i in range(lado):
        if i == 0 or i == lado - 1:
            print(' ' * (lado - i - 1) + '*' * (2 * i + 1))
        else:
            print(' ' * (lado - i - 1) + '*' + ' ' * (2 * i - 1) + '*')

lado = int(input("Introduce el tamaño del hexágono (lado): "))
dibujar_hexagono(lado)