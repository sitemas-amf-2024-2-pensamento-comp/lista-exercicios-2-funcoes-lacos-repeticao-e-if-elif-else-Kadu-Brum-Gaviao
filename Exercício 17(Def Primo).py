def eh_primo(numero):
    if numero <= 1:
        print(f'O número {numero} não é primo!')
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                print(f'O número {numero} não é primo!')
                return False
        print(f'O número {numero} é primo!')
        return True


numeroUsuario = int(input('Digite um número: '))
eh_primo(numeroUsuario)
