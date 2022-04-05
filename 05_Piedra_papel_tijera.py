from random import randint
from time import sleep
def juego():
    while True:
        print("""
        1- Jugar Piedra-Papel-Tijera
        2- Salir
        """)
        try:
            jugar_salir = int(input('Elija una opcion 1 o 2: '))
        
            if jugar_salir == 1: 
                opcion = ('piedra','papel','tijera')
                computadora = opcion[randint(0,2)]
                nombre = input('Ingresa tu nombre: ')
                humano = input('¿Que elije? piedra/papel/tijera: ')
                humano = humano.lower()
                try:
                    if humano in opcion:
                        sleep(1)
                        print(f'La computadora eligio: {computadora}')
                        try:
                            if humano == computadora:
                                print(f'Fue un empate, ambos eligieron {humano}')
                            elif humano == 'piedra' and computadora == 'papel':
                                print(f'Gana computadora')
                            elif humano == 'piedra' and computadora == 'tijera':
                                print(f'Gana {nombre}')
                            elif humano == 'papel' and computadora == 'piedra':
                                print(f'Gana {nombre}')
                            elif humano == 'papel' and computadora == 'tijera':
                                print(f'Gana computadora')
                            elif humano == 'tijera' and computadora == 'papel':
                                print(f'Gana {nombre}')
                            elif humano == 'tijera' and computadora == 'piedra':
                                print(f'Gana computadora')
                            sleep(2)
                        except:
                            print('Algo salio mal, intente denuevo')
                    else:
                        print('Debe elegir: piedra, papel o tijera!')
                except:
                    print('Debe elegir: piedra, papel o tijera!')
            elif jugar_salir == 2:
                break
        except:
            print('Error, debe eligir 1 o 2: ')
            juego()

juego()
