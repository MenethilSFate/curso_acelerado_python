'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion2/ejercicio8.py
Autor: Francisco Alejandro Brindis Reyes
Action: detecta numero negativos
'''

CONTRASEÑA_VERDADERA = 123456
print("INICIO DE SESIÓN")
password = int(input("Coloque su contraseña: "))

if password == CONTRASEÑA_VERDADERA:
  print("BIENVENIDO")
else:
  print("CONTRASEÑA ERRONEA")

