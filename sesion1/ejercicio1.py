'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion/ejercicio1.py
Autor: Francisco Alejandro Brindis Reyes
Action: asignación de variables

'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['chiapas', 'campeche', 'veracruz']
productos_tbasco = ['Cacao', 'Coco', 'Caña']

print(
  nombre_estado,
  " es un estado que ",
)
print("con ", estados_cercanos[2], "colinda al sur", "y")
print("Tiene una superficie de ", superficie)
print("En los ultimos años su población ha aumentado llegando a un total de: ",
      poblacion_total)
print("Su temperatura es de: ", promedio_temperatura,
      "y los productos que produce son: ", productos_tbasco[0])
