#!/usr/bin/env python3

def generate_fibonacci(length):
    if length <= 0:
        return []
    elif length == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, length):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

def print_fibonacci(length):
    fib_sequence = generate_fibonacci(length)
    print(fib_sequence)