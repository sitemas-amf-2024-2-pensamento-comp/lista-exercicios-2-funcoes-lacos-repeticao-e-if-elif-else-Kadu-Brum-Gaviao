num = int(input('Digite um número: '))
i = 1

while num > 1:
    i = i * num
    num = num - 1
print(f'O fatorial é {i}')
