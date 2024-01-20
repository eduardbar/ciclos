def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_lengths(limit):
    for i in range(1, limit):
        sequence = collatz_sequence(i)
        print(f"{i} {'*' * len(sequence)}")

numero_collatz = int(input("Ingrese un número para la secuencia de Collatz: "))
collatz_sequence(numero_collatz)
plot_collatz_lengths(numero_collatz)