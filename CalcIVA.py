def calc_iva(cant, iva=0.21):
    return cant * iva


cant = float(input('Introduce la cantidad: '))
iva = calc_iva(cant)
iva_red = calc_iva(cant, 0.06)
print('El IVA normal de', cant, 'es', iva)
print('El IVA reducido de', cant, 'es', iva_red)