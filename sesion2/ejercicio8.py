'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio8.py
Autor: Francisco Alejandro Brindis Reyes
Action: detecta numero negativos
'''
numero = int(input("Escriba un número entero: "))
if numero < 0:
  print("ESTE NUMERO ES NEGATIVO")
  print(f"Ha escrito el número {numero}")
if numero > 0:
  print("ESTE NUMERO ES POSITIVO")
  print(f"Ha escrito el número {numero}")
else:
  print("ESTE NUMERO ES 0")
