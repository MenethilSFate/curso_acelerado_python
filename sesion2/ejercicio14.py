'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio14.py
Autor: Francisco Alejandro Brindis Reyes
Action: Mostrar 10 veces una palabra pedida
'''
palabra = input("Escriba una palabra: ")
numeracion = 1
contador = 1
while contador <= 10:
  print(str(numeracion) + ".-" + palabra)
  numeracion += 1
  contador += 1
