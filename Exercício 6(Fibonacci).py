"""
Faça um programa que peça ao usuário um número inteiro
n e exiba os n primeiros números da sequência de Fibonacci.

"""
a = 0
b = 1
n = int(input('Quantos números você que ver na sequência: '))
i = 0

while i < n:
    print(a)
    num = a + b
    a = b
    b = num
    i += 1