# ==
color = 'azul'
print(color =='azul')
print(color == 'rojo')

# !=
print(color != 'rojo')

# >
altura = 172
altura_minima = 150
print(altura > altura_minima)

# <
print(altura < altura_minima)

# >=
print(altura >= altura_minima)

precio = 100
IVA = 0.12
impuesto = precio * IVA
impuesto = precio * IVA
print(impuesto)

# <=
print(altura < altura_minima)


def abrir_puerta(altura, edad):
    ALTURA_MININA = 150
    EDAD_MININA = 15
    EDAD_MAXINA = 80 

    if altura <= ALTURA_MININA:
        print('No alcanza')
        return

    if edad <= EDAD_MININA: 
        print('Muy Joven')
        return

    if edad >= EDAD_MAXINA:
        print('Muy grande')
        return

    print('pase adelante')

abrir_puerta(140, 14)





