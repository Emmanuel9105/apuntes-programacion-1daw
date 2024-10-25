# Esto es un comentario de una linea

'''
  Esto es un comentario
  de varias lineas
'''

# Imprimir información por consola
print('Esto se ve por consola')

# Introducir información por consola
# Los datos siempre se envían como texto
# ! input('Introduce un texto:')
# Para poder trabajar con los datos hace falta guardarlos en una variable
# ! text1 = input('Introduce un texto:')
# ! print(text1)

# Declaración de variables
variable = 'Declaración de variable'
print(variable)

# Comparaciones lógicas

# Igual
print(1 == 2) # False
# Distinto
print(1 != 2) # True
# Mayor que
print(1 > 2) # False
# Menor que
print(1 < 2) # True
# Mayor o igual que
print(1 >= 2) # False
# Menor o igual que
print(1 <= 2) # True

# Operadores lógicos

# AND
print((1 < 2) and (1 == 2)) # False
# OR
print((1 < 2) or (1 == 2)) # True
# NOT
print(not (1 == 2)) # True

# Operadores aritméticos

# Suma
print(1 + 2) # 3
# Resta
print(2 - 1) # 1
# Multiplicación
print(2 * 2) # 4
# División
print(4 / 2) # 2.0 (La división devuelve un float siempre)
# División entera (devuelve el cociente entero sin decimales)
print(5 // 2) # 2
# Módulo (residuo, resto)
print(5 % 2) # 1
# Potencia
print(2 ** 3) # 8

# Precedencia de operaciones
""" 
  1º ( ) Paréntesis
  2º ** Exponentes
  3º * / % // Multiplicaciones, divisiones, módulos y divisiones enteras
  4º + - Sumas y restas
"""

# Condiciones

edad = 18

if edad < 18:
  print('Eres menor de edad') # No se imprime por consola
elif edad == 18:
  print('Acabas de cumplir la mayoría de edad') # Se imprime por consola
else:
  print('Eres mayor de edad') # No se imprime por consola

# Condición anidada

edad = 25
licencia = True

if edad >= 18:
  if licencia:
    print('Puedes conducir') # Se imprime por consola
  else:
    print('Necesitas una licencia para conducir') # No se imprime por consola
else:
  print('Debes ser mayor de edad para conducir') # No se imprime por consola

# Valores truthy y falsy

# Falsy
None
False
0
''
[]
()
{}

# Truthy
'Todo lo demás'

# Bucle While

secretNumber = 7
tries = None

print('Adivina el número entre 1 y 10')

while tries != secretNumber:
  # ! tries = int(input('Introduce un número: '))

  tries = 7

  if tries < secretNumber:
    print('Demasiado bajo')
  elif tries > secretNumber:
    print('Demasiado alto')
  else:
    print('Has acertado')

# Bucle For

for number in range(1, 6): # Genera los números del 1 al 5
  if number == 3:
    print('Hemos encontrado el 3')
  else:
    print(number)

# Longitud de elementos

FRUITS = ['Manzana', 'Pera', 'Plátano']

print(len(variable))
# ! print(len(secretNumber)) # Rompe el programa porque los números no tiene longitud
print(len(FRUITS))

# Índice de elementos
print(variable[2:4]) # cl -> Declaración de variable

# Funciones

def nombreFuncion():
  # Código que ejecuta la función
  return # Las funciones deben tener al menos una línea de código en su interior

# Función sin parámetros ni retorno

def saludar():
  print('Hola')

saludar()

# Función con parámetros sin retorno

def saludar2(nombre):
  print(f'Hola {nombre}')

saludar2('Emmanuel')
saludar2('Jero')

# Función sin parámetros con retorno
def suma():
  return 10 + 12

print(suma())

# Función con parámetros y retorno

def resta (a, b):
  return a - b

print(resta(30, 8))