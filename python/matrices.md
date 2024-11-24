# 1. Creación de matrices bidimensionales

## Declaración directa

Puedes crear una matriz bidimensional escribiendo listas dentro de otra lista:

```python
matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]
```

En este caso, matriz[0][1] accederá al elemento en la fila 0, columna 1 (valor 2).

## Creación dinámica

Puedes construir una matriz bidimensional usando bucles anidados:

```python
filas = 3
columnas = 4
matriz = [[i * j for j in range(columnas)] for i in range(filas)]

print(matriz)
# Salida:
# [
#   [0, 0, 0, 0],
#   [0, 1, 2, 3],
#   [0, 2, 4, 6]
# ]
```

2. Acceso a elementos

Puedes acceder a los elementos de una matriz usando dos índices:

```python
print(matriz[0][1])  # Fila 0, Columna 1 -> Imprime: 0
print(matriz[2][3])  # Fila 2, Columna 3 -> Imprime: 6
```

# 3. Recorrer una matriz bidimensional

## Usando bucles anidados

Puedes recorrer una matriz bidimensional con dos bucles for:

```python
for i in range(len(matriz)):  # Recorre las filas
    for j in range(len(matriz[i])):  # Recorre las columnas
        print(f"Elemento en [{i}][{j}]: {matriz[i][j]}")
```

## Usando comprensión de listas

Si solo necesitas procesar elementos, puedes hacerlo de manera compacta:

```python
[print(f"Elemento: {valor}") for fila in matriz for valor in fila]
```

# 4. Modificación de elementos

Puedes modificar los elementos de la matriz asignándoles nuevos valores:

```python
matriz[1][2] = 99  # Cambia el elemento en la fila 1, columna 2
print(matriz)
# Salida:
# [
#   [0, 0, 0, 0],
#   [0, 1, 99, 3],
#   [0, 2, 4, 6]
# ]
```

# 5. Operaciones comunes

## Agregar una fila

Agrega una nueva fila al final con append():

```python
matriz.append([10, 11, 12, 13])
print(matriz)
# Salida:
# [
#   [0, 0, 0, 0],
#   [0, 1, 99, 3],
#   [0, 2, 4, 6],
#   [10, 11, 12, 13]
# ]
```

## Eliminar una fila

Elimina la última fila con pop():

```python
matriz.pop()
print(matriz)
# Salida:
# [
#   [0, 0, 0, 0],
#   [0, 1, 99, 3],
#   [0, 2, 4, 6]
# ]
```

## Agregar una columna

Recorre cada fila y añade un nuevo elemento:

```python
for fila in matriz:
    fila.append(0)

print(matriz)
# Salida:
# [
#   [0, 0, 0, 0, 0],
#   [0, 1, 99, 3, 0],
#   [0, 2, 4, 6, 0]
# ]
```

## Eliminar una columna

Recorre cada fila y elimina el último elemento:

```python
for fila in matriz:
    fila.pop()

print(matriz)
# Salida:
# [
#   [0, 0, 0, 0],
#   [0, 1, 99, 3],
#   [0, 2, 4, 6]
# ]
```

# 6. Ejemplos prácticos

## Suma de todos los elementos

```python
suma = sum(sum(fila) for fila in matriz)
print(f"Suma total: {suma}")  # Suma de todos los elementos de la matriz
```

## Transposición de una matriz

Intercambia filas por columnas:

```python
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(transpuesta)
# Salida:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 99, 4],
#   [0, 3, 6]
# ]
```

## Multiplicación de matrices

Para multiplicar dos matrices, las columnas de la primera deben coincidir con las filas de la segunda:

```python
matrizA = [
    [1, 2, 3],
    [4, 5, 6]
]

matrizB = [
    [7, 8],
    [9, 10],
    [11, 12]
]

resultado = [[sum(a * b for a, b in zip(filaA, columnaB)) for columnaB in zip(*matrizB)] for filaA in matrizA]

print(resultado)
# Salida:
# [
#   [58, 64],
#   [139, 154]
# ]
```

# 7. Usando numpy para matrices más complejas

La biblioteca numpy es ideal para trabajar con matrices grandes o realizar operaciones matemáticas:

```python
import numpy as np

# Crear una matriz bidimensional
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Operaciones básicas
print(matriz + 1)  # Suma 1 a cada elemento
print(matriz.T)    # Transpuesta de la matriz
```

# 8. Ventajas y desventajas

## Ventajas

- Representación directa y flexible para datos tabulares.
- Versatilidad para manipular datos usando listas y comprensión de listas.

## Desventajas

- Las operaciones complejas (transposiciones, multiplicaciones, etc.) pueden ser más lentas sin bibliotecas como numpy.
