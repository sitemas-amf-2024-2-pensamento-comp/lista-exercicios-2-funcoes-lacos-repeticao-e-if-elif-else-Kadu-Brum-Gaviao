somaNotas = 0
numeroNotas = 0

while True:
    notas = float(input('Digite uma nota ou digite ou -1 para encerrar o programa: '))
    if notas == -1:
        print('Saindo do programa.')
        break
    somaNotas += notas
    numeroNotas += 1

if numeroNotas > 0:
    mediaNotas = somaNotas / numeroNotas
    print(f'A média de {somaNotas} / {numeroNotas} = {mediaNotas:.2f}')
else:
    print('Nenhuma nota válida foi inserida.')
