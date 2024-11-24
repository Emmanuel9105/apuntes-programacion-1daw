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

while True:
  try:
    variable = int(input('Introduce un número: '))
  except ValueError:
    print('El número introducido no es un número')