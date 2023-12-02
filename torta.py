from fpdf import FPDF
import qrcode

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

pdf = FPDF(orientation='portrait',unit='mm',format= 'A4')
pdf.add_page()
pdf.set_font('ARIAL','B',16)

pdf.text(y= 5, x= 15, txt= 'empresa ¨postresamalia')
pdf.image('postresamalia.jpg',y= 10, x= 150, w= 40,h = 40, link= 'https://www.facebook.com/people/Postresamalia/100063545463998/')
pdf.text(y= 20,x= 15,txt= 'nombre del cliente'+ str (nombre_del_cliente))
pdf.text(y= 30,x= 15,txt= 'cedula del cliente'+ str (cedula_del_cliente))
pdf.text(y = 35, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y=40,x=15,txt= 'precio del dolar'+str(precio_de_material))
pdf.text(y=50,x=15,txt= 'margen de ganancia'+str(margen_de_ganancia))
pdf.text(y=60,x=15,txt= 'subtotal'+str(subtotal))
pdf.text(y =65, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y=70,x=15,txt= 'total'+str(total))
pdf.text(y =75, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y=80,x=15,txt= 'total'+str(total))
pdf.text(y=70,x=15,txt= 'en dolares'+str(en_dolar))
pdf.output('cauculo_de_ganancia.pdf')