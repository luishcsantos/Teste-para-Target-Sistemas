def is_fibonacci(num):
    a = 0
    b = 1
    while b < num:
        a, b = b, a + b
    return b == num

def fibonacci_sequence(num):
    sequence = [0, 1]
    while sequence[-1] < num:
        sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1] == num:
        print(f"{num} pertence à sequência de Fibonacci")
    else:
        print(f"{num} não pertence à sequência de Fibonacci")
    print(sequence)

numero = int(input("Digite um número: "))
fibonacci_sequence(numero)