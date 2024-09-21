def multiplicacao(a, b):
    somaSucessiva = 0
    for i in range(abs(b)):
        somaSucessiva += a
        print(f'Soma após {i + 1} iterações: {somaSucessiva}')
    if b < 0:
        somaSucessiva = -somaSucessiva
    print(f'A multiplicação é {somaSucessiva}')


n1 = int(input('Digite o primeiro número(a): '))
n2 = int(input('Digite o segundo número(b): '))
multiplicacao(n1, n2)
