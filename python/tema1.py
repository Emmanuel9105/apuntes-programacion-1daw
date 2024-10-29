# Importaciones en Python
import math

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

# Excepciones

try:
  # Código que puede causar excepciones
  print('Try') # Se muestra por consola
except:
  # Código para manejar la excepción
  print('Except') # Se muestra por consola
else:
  # Código que se ejecuta si no hay excepciones (opcional)
  print('Else') # No se muestra por consola
finally:
  # Código que siempre se ejecuta, haya o no una excepción (opcional)
  print('Finally') # Se muestra por consola

# Operaciones

# Sumatorio
sumatorio1 = 3
sumatorio2 = 5
resultadoSumatorio = sum(range(sumatorio1, sumatorio2 + 1))

print(resultadoSumatorio)

# Productorio
productorio1 = 3
productorio2 = 5
resultadoProductorio = math.prod(range(productorio1, productorio2 + 1))

print(resultadoProductorio)

# Factorial
factorial = 3
resultadoFactorial = math.factorial(factorial)

print(resultadoFactorial)

# Número primo
numeroPrimo = 29

def isPrime(number):
  if number <= 1:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False
  return True

print(isPrime(numeroPrimo))

# Suma de factoriales
factorial1 = 3
factorial2 = 5

resultadoFactorial1 = math.factorial(factorial1)
resultadoFactorial2 = math.factorial(factorial2)

resultadoSumaFactoriales = resultadoFactorial1 + resultadoFactorial2

print(resultadoSumaFactoriales)

def sumaFactoriales(factorial1, factorial2):
  resultadoFactorial1 = math.factorial(factorial1)
  resultadoFactorial2 = math.factorial(factorial2)
  resultadoSumaFactoriales = resultadoFactorial1 + resultadoFactorial2
  return resultadoSumaFactoriales

print(sumaFactoriales(3, 5))

# Media de N números

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = sum(listaNumeros) / len(listaNumeros)

print(media)

#  Capicúa
def isCapicua(numero):
    # Convertimos el número a string para poder compararlo al revés
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

# Longitud de una cadena
longitudCadena = "Hola"

print(len(longitudCadena))

# Tabla de multiplicar de N número
def tabla_multiplicar(numero, hasta=10):
    for i in range(0, hasta + 1):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(2)

# Potencia

numeroAElevar = 2
numeroPotencia = 3

resultadoPotencia = math.pow(numeroAElevar, numeroPotencia)

print(resultadoPotencia)

# Raíz cuadrada
numeroRaiz = 100

if numeroRaiz < 0:
  print('No se puede calcular la raíz cuadrada de un número negativo')
else:
  print(math.sqrt(numeroRaiz))

# Redondeo
numeroRedondear = 2.747584
print(round(numeroRedondear, 2)) # 2 es el número de decimales que devuelve el round

# Imprimir número impar hasta un número dado

def oddNumbersUpTo():
  number = int(input("Enter a positive integer: "))
  if number <= 0:
    print("Please enter a positive integer.")
    return

  odds = [str(i) for i in range(1, number + 1) if i % 2 != 0]
  result = ", ".join(odds[:-1]) + " and " + odds[-1] + "."
  print(result)

oddNumbersUpTo()
