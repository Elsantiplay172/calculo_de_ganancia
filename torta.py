from fpdf import FPDF


nombre_del_cliente = input('nombre de cliente:  ')
cedula_del_cliente = input('cedula de cliente:  ')
precio_de_material  = float(input('precio de el material:  '))

precio_de_material2  = float(input('precio de el material:  '))
precio_de_material3  = float(input('precio de el material:  '))
precio_de_material4  = float(input('precio de el material:  '))
precio_de_material5  = float(input('precio de el material:  '))
precio_de_material6  = float(input('precio de el material:  '))
precio_de_material7  = float(input('precio de el material:  '))
precio_de_material8  = float(input('precio de el material:  '))
precio_de_material9 = float(input('precio de el material:  '))
precio_de_material10  = float(input('precio de el material:  '))
precio_de_material11  = float(input('precio de el material:  '))
precio_de_material12= float(input('precio de el material:  '))
precio_de_material13  = float(input('precio de el material:  '))
precio_de_material14  = float(input('precio de el material:  '))
precio_de_material15  = float(input('precio de el material:  '))

precio_del_dolar = float(input('precio del dolar:  '))

subtotal = float (precio_de_material + precio_de_material2 + precio_de_material3 + precio_de_material4 + precio_de_material5 + precio_de_material6 + precio_de_material7 + precio_de_material8 + precio_de_material9 + precio_de_material10 + precio_de_material11 + precio_de_material12 + precio_de_material13 + precio_de_material14 + precio_de_material15 )
margen_de_ganancia = subtotal*0.30

total = subtotal + margen_de_ganancia

print('nombre del cliente',nombre_del_cliente)
print('cedula del cliente',cedula_del_cliente)
print('subtotal',subtotal)
print('margen de ganancia ',margen_de_ganancia)
print('total',total,'bs')
en_dolar = total/precio_del_dolar
dolares = round(en_dolar)
print('en dolares', dolares)
sin_decimas = round(total)
print('total entero',sin_decimas,'bs')