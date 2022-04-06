"""Generador de a10_Letras
Pedimos a un usuario que elija una canción 
de una lista de 6 canciones. Cuando el usuario
 lo hace, imprime la letra de la canción que 
 seleccionó.
 Para llevarlo más lejos, y darle más complejidad,
  tenga al menos 3 canciones del mismo artista.
A continuación, pide al usuario que ponga el nombre 
del artista para que pueda mostrarle solo las opciones 
de ese artista. Luego, el usuario puede seleccionar 
una canción específica de esa lista.
 """
from a10_Letras import Jijiji as ji
from a10_Letras import Un_poco_de_amor_frances as frances
from a10_Letras import El_tesoro_de_los_inocentes as tesoro
from a10_Letras import Residente as reside
from a10_Letras import Trueno as thunder
from a10_Letras import PlanA as A


def menu_indio():
    print("""
    1- Jijiji
    2- Un poco de amor frances
    3- El tesoro de los inocentes
    """
    )
    opcion = int(input('Elija el Nro correspondiente al canción: '))
    return generador(opcion)

def menu_bzrp():
    print("""
    5- Residente
    6- Trueno"""
    )
    opcion = int(input('Elija el Nro correspondiente al canción: '))
    return generador(opcion)

def menu_londra():
    print("""
    4- Plan A"""
    )
    opcion = int(input('Elija el número correspondiente a la canción: '))
    return generador(opcion)

def generador(cancion):
    if cancion == 1:
        print(ji)
    elif cancion == 2:
        print(frances)
    elif cancion == 3:
        print(tesoro)
    elif cancion == 4:
        print(A)
    elif cancion == 5:
        print(reside)
    elif cancion == 6:
        print(thunder)
    """elif cancion == 'Indio':
            print(f'Estas son las canciones del Indio: {menu(opcion)}')
    elif cancion == 'bzrp':
        print((f'Esta son las canciones disponibles de Bzrp: {Bzrp}'))"""
            
def menu():
    numero_artista = int(input("""Quiere elejir por numero de cancion o por artista?
    1- Numero
    2- Artista
    Elija 1 o 2: 
    """))
    print("""
        Canciones:

        1- Jijiji - Indio
        2- Un poco de amor frances - Indio
        3- El tesoro de los inocentes - Indio
        4- Plan A - Londra
        5- Residente - Bzrp
        6- Trueno - Bzrp
        """)
    if numero_artista == 1:
        opcion = int(input('Seleccione el numero de la cancion que quiere su letra: '))
        return generador(opcion)
    elif numero_artista == 2:
        opcion = input('Seleccione el artista de la cancion que quiere su letra: ')
        opcion = opcion.capitalize()
        if opcion == 'Indio':
            return menu_indio()
        elif opcion == 'Bzrp':
            return menu_bzrp()
        elif opcion == 'Londra':
            return menu_londra()
    else:
        print('Algo salio mal, debia ingresar 1 o 2.')

menu()