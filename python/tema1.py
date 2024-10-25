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