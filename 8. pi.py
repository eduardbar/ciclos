import math

def calcular_pi(n):
    suma = 0
    for i in range(n):
        if i % 2 == 0:
            suma += 1 / (2 * i + 1)
        else:
            suma -= 1 / (2 * i + 1)
    return 4 * suma

n = int(input("Introduce el número de términos de la suma: "))
pi_aproximado = calcular_pi(n)
print(f"La aproximación de π es: {pi_aproximado}")