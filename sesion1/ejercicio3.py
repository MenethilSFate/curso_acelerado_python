'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio3.py
Autor: Francisco Alejandro Brindis Reyes
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
extras = float(input("Introduce tus horas extras trabajadas: "))
paga = horas * coste
paga2 = extras * coste
paga3 = paga + paga2
print("Tu paga es", paga3)