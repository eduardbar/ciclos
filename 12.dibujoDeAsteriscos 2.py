def dibujar_triangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)

altura = int(input("Introduce la altura del triángulo: "))
dibujar_triangulo(altura)