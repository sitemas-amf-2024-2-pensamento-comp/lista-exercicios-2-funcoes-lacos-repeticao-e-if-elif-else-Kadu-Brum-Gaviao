def converter_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsiusTemperatura = int(input('Temperatura em graus celsius: '))
fahrenheitTemperatura = converter_para_fahrenheit(celsiusTemperatura)

print(f'{celsiusTemperatura}° são convertidos para: {fahrenheitTemperatura}°')
