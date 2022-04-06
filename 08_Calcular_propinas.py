"""En este caso, nuestro objetivo es averiguar exactamente la cantidad de 
propina que hay que proporcionar después de un servicio. En este caso, hay 
que solicitar la factura total. Con esto, aplicaremos la propina para el 
18%, 20% y 25%.

Ejemplo:

Mensaje inicial: ¿Cuál es la factura total de hoy, por favor?
Entrada: $55.87
Salida: La propina aplicando el 18% is $10.06, que contabiliza un total de $65.93
Recordemos que queremos ser amable, por lo que no olvidemos redondear. 
Para impulsar esta funcionalidad, vamos a preguntar por la cantidad de 
personas involucradas, para dividir la propina de manera equitativa y 
el coste total entre esas personas.
Por darle otro punto de vista, prueba a añadir dividiendo de manera desigual
, para poner en práctica estos aspectos (por ejemplo, una persona paga el 70% 
de la factura mientras que la otra paga el 30%).
"""
from time import sleep

def propinas(parcial, propina = 18):
    sleep(1)
    total = parcial + parcial*propina/100
    print(f'La propina aplicando el {propina}% es {parcial*propina/100}$, y da un total de {total}$')
    dividir = input('Desea que calcule equitativamente cuanto debe abonar cada uno? si/no: ')
    dividir.lower()
    
    if dividir == 'si':
        cantidad_personas = int(input('Ingrese cuantas personas son: '))
        por_persona = total/cantidad_personas
        print(f'Cada persona debe abonar {por_persona}')
    else:
        print(f'El total a abonar es {total}')
    

parcial = float(input('¿Cual es la factura total de hoy, por favor?: '))
propinas(parcial)