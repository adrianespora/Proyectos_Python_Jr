"""
Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?
"""
respuesta = input('¿Quieres saber si un numero es Par o Impar? si/no: ')
respuesta = respuesta.lower()

while respuesta == 'si':
    numero = int(input('¿En que numero estas pensando?: '))
    if numero%2 == 0:
        print('Es un numero Par! ')
        respuesta = input('¿Quieres añadir otro numero? si/no: ')
        respuesta = respuesta.lower()
    else:
        print('Es un numero Impar')
        respuesta = input('¿Quieres añadir otro numero? si/no: ')
        respuesta = respuesta.lower()