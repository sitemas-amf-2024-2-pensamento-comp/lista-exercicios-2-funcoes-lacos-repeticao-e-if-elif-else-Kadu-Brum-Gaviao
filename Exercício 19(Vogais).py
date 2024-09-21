def contar_vogais(texto):
    texto = texto.lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    i = 0
    for letra in texto:
        if letra in vogais:
            i += 1
    return i


frase = input('Digite uma frase: ')
if not all(letra.isalpha() or letra.isspace() for letra in frase):
    print('Digite usando letras!')
else:
    resultado = contar_vogais(frase)
    print(f"Número de vogais: {resultado}")
