"""
Recopilamos una dirección de correo electrónico del usuario y 
luego vamos a averiguar si ese email tiene nombre de dominio 
personalizado o un nombre de un dominio popular. Por ejemplo:

Entrada: mary.jane@gmail.com
Salida: Hola Mary, estoy viendo que tu email está registrado 
con Google. ¡Eso es genial!.
Entrada: peter.pan@myfantasy.com
Salida: Hola Peter, estoy observando que estás utilizando un 
dominio personalizado de myfantasy. ¡Impresionante!.
"""
def correo(email):
    separador = email.split('@')
    usuario = separador[0]
    dominio = separador[1]
    if '.com' in dominio:
        dominio = dominio[:dominio.find('.com')]
        print(f'Hola {usuario}, estoy viendo que tu email esta registrado con {dominio}!!')


mail = input('Ingrese su email: ')
correo(mail)