'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio17.py
Autor: Francisco Alejandro Brindis Reyes
Action: Tabla de multiplicar
'''
resultado = 0
numeracion = 1
contador = 1
tabla = int(input("Ingrese la tabla de multiplicar deseada (del 1 al 10): "))
while contador <= 12:
  print(str(tabla) + "*" + str(numeracion) + " = " + str(contador * tabla))
  numeracion += 1
  contador += 1
