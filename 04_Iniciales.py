cadena = input('Ingrese sus nombres y apellidos: ')
lista = cadena.split(' ')
acronimo = ''
for palabra in lista:
    acronimo += palabra[0]
print(f'Su acronimo es: {acronimo.upper()}')
