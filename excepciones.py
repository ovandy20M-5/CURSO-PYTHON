

edad = 17

if edad < 18:
    raise Exception('Eres menor para usar el programa')

print('continuacion')

class AgeExcepcion(Exception):
    pass

try:
    'texto' + 5 
    if edad < 18:
        raise AgeExcepcion('Eres menor para usar el programa')
except Exception:
    print('se lanzó el error')