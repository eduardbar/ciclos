import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

e_aproximado = 0
n = 10

while True:
    termino_actual = factorial(n)
    e_aproximado += termino_actual

    if n > 10 and termino_actual < 0.0001:
        break

    n += 1

print(f"Valor aproximado de e: {e_aproximado}")