def palindromo(palabra):
    letras = []
    for letra in palabra:
        letras.append(letra)
    letras.reverse()
    palabra_invertida = ''
    for letra in letras:
        palabra_invertida += letra
    if palabra == palabra_invertida: print(f'{palabra.capitalize()} es un palindromo')
    else: print(f'{palabra.capitalize()} no es un palindromo')

palabra = input('Ingrese una palabra: ')
palindromo(palabra)