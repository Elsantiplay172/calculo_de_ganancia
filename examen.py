from datetime import datetime
from fpdf import FPDF
import qrcode


print('rutina de asistencia del cole')
tiempo_inicio = datetime.now()
print(tiempo_inicio)

#SANTIAGO SANGRONIS LO HIZO
print('rutina de asistencia del cole')
materia = input('nombre de la materia: ')
nombredelprofesor = input('nombre del profesor:  ')
nombredelestudiante =  (input('nombre del estudiante:  '))
examen1 = float (input('nota del primer examen: '))
examen2 = float (input('nota del segundo examen: '))
examen3 = float (input('nota del tercer examen:'))
examen4 = float (input('nota del cuarto examen:'))

sumadelosexamenes =  examen1 + examen2 + examen3 + examen4 

notafinaldecimal =  (sumadelosexamenes )/4
recomendaciones = input('recomendaciones:    ')
notafinal = round(notafinaldecimal)

comentario = 'sin comentario'

print('materia',materia)
print('profesor',nombredelprofesor)
print('estudiante', nombredelestudiante)
print('nota final', notafinal, 'de 20')
print('nota final decimal es ', notafinaldecimal, 'de 20.0')
if notafinal >=10: 
    print('apobrado')
    comentario= 'aprobado'
 
else:
    print('reprobado')
    comentario= 'reprobado'

if notafinal >=19:
    print('eres sobresaliente,felicidades')
  
else:
    print('eres del promedio')  

    




print('tiempo de fin')
tiempo_defin = datetime.now()
print(tiempo_defin)

duracion_de_la_rutina = tiempo_defin - tiempo_inicio

print('duracion de la rutina', duracion_de_la_rutina)
print('duracion de la rutina ', duracion_de_la_rutina.seconds,'en segundos')
print('duracion de la rutina', duracion_de_la_rutina.microseconds,'en microsegundos')

pdf = FPDF(orientation='portrait',unit='mm',format= 'A4')
pdf.add_page()
pdf.set_font('ARIAL','B',16)
pdf.image('escudo.jpg',y= 20, x= 150, w= 40,h = 40, link= 'https://www.google.com/maps/place/Colegio+San+Felipe+Neri/@10.3493652,-67.0487782,20z/data=!4m6!3m5!1s0x8c2a8c578df048cd:0x20ad459644777517!8m2!3d10.3496289!4d-67.048265!16s%2Fg%2F11c1tt5gdy?hl=es&entry=ttu')
pdf.text(y = 40, x = 15,txt= 'boleta de fin de clases')
pdf.text(y = 50, x = 15,txt = 'fecha:  '+ str(tiempo_inicio))
pdf.text(y = 60, x = 15,txt = 'nombre del profesor:  '+ str(nombredelprofesor))
pdf.text(y = 70, x = 15,txt = 'nombre del estudiante:  '+ str(nombredelestudiante))
pdf.text(y = 80, x = 15,txt = 'materia:  '+ str(materia))
pdf.text(y = 85, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y = 90, x = 15,txt = ' primer examen:  '+ str(examen1))
pdf.text(y = 100, x = 15,txt = 'segundo examen:  '+ str(examen2))
pdf.text(y = 110, x = 15,txt = 'tercer examen:  '+ str(examen3))
pdf.text(y = 120, x = 15,txt = 'cuarto examen:  '+ str(examen4))
pdf.text(y = 125, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y = 130, x = 15,txt = 'notafinal:  '+ str(notafinal))
pdf.text(y = 135, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y = 140, x= 15,txt= 'recomendaciones'+ str(recomendaciones))
pdf.text(y = 145, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y= 150, x = 15, txt= str (comentario) )
pdf.text(y = 155, x= 0,txt = '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
pdf.text(y = 160, x = 15, txt= 'inscrito en la ley organica de educacion')
pdf.image('bandera.png',y= 170, x= 150, w= 40,h = 40, link='http://apps.ucab.edu.ve/nap/recursos/LeyOrganicadeEducacion.pdf' )
nota_nombre = nombredelestudiante+ str(notafinal)
img = qrcode.make(nota_nombre)
img.save('nota_nombre.png')
pdf.image('nota_nombre.png',y=200, x= 35, w=40, h=40)
pdf.output('reporte nota.pdf','f')