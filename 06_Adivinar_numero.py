from random import randint

numero_random = randint(1,50)
def juego():
    print("""
        Adivinar el numero entre 1 y 50

        1 - Jugar
        2 - Salir
        """)
    try:
        jugar_salir = int(input('Elija una opcion 1 o 2: '))
        cuenta = 0
        while True:
            cuenta +=1
            try:
                if jugar_salir == 1:
                    eleccion = int(input('Ingrese un numero: '))
                    if eleccion == numero_random:
                        print(f'Haz adivinado en {cuenta} intentos!')
                        break
                    else:
                        if eleccion > numero_random:
                            print(f'Tiene que ser un numero mas chico')
                        elif eleccion < numero_random:
                            print(f'Tiene que ser un numero mas grande')
                else:
                    break
            except:
                print('Debe ingresar un numero entre 1 y 50!')
    except:
        print('Algo salio mal, elija 1 o 2')
        juego()

juego()