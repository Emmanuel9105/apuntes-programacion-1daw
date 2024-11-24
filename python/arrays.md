# 1. Listas

## ¿Qué es una lista?

Una lista es una colección ordenada y mutable que permite almacenar cualquier tipo de elementos, como números, strings, u otras listas. Las listas son extremadamente versátiles y forman parte de los tipos de datos integrados de Python.

## Declaración de una lista

Puedes crear una lista utilizando corchetes [] o la función list():

```python
# Lista de strings
frutas = ["manzana", "banana", "cereza"]

# Lista de números
numeros = [10, 20, 30]

# Lista mixta
mixta = [42, "Hola", True, 3.14]

# Lista vacía
vacia = []
```

## Acceso a elementos

Puedes acceder a los elementos de una lista usando índices, que comienzan en 0:

```python
print(frutas[0])  # "manzana"
print(frutas[2])  # "cereza"

# Índices negativos para acceder desde el final
print(frutas[-1])  # "cereza"
```

## Propiedades y métodos comunes de las listas

1. Longitud de una lista

La función len() devuelve el número de elementos:

```python
print(len(frutas))  # 3
```

2. Añadir elementos

- append(): Añade un elemento al final.

```python
frutas.append("durazno")
print(frutas)  # ["manzana", "banana", "cereza", "durazno"]
```

- insert(): Inserta un elemento en una posición específica.

```python
frutas.insert(1, "fresa")
print(frutas)  # ["manzana", "fresa", "banana", "cereza", "durazno"]
```

3. Eliminar elementos

- pop(): Elimina y devuelve el elemento en una posición específica (por defecto, el último).

```python
ultimo = frutas.pop()
print(ultimo)  # "durazno"
print(frutas)  # ["manzana", "fresa", "banana", "cereza"]
```

- remove(): Elimina la primera ocurrencia de un elemento.

```python
frutas.remove("banana")
print(frutas)  # ["manzana", "fresa", "cereza"]
```

4. Recorrer una lista

Puedes usar un bucle for para iterar:

```python
for fruta in frutas:
    print(fruta)
```

## Métodos avanzados de listas

1. extend(): Combina listas.

```python
frutas.extend(["kiwi", "uva"])
print(frutas)  # ["manzana", "fresa", "cereza", "kiwi", "uva"]
```

2. sort(): Ordena la lista en su lugar.

```python
numeros = [30, 10, 20]
numeros.sort()  # Orden ascendente
print(numeros)  # [10, 20, 30]

numeros.sort(reverse=True)  # Orden descendente
print(numeros)  # [30, 20, 10]
```

3. reverse(): Invierte el orden de la lista.

```python
frutas.reverse()
print(frutas)  # ["uva", "kiwi", "cereza", "fresa", "manzana"]
```

4. index() y count()

- index(valor): Devuelve el índice de la primera aparición del valor.

```python
print(frutas.index("cereza"))  # 2
```

- count(valor): Cuenta cuántas veces aparece un valor.

```python
print(frutas.count("manzana"))  # 1
```

# 2. Arrays

En Python, los arrays están disponibles a través del módulo array, pero no son tan comunes como las listas. Los arrays se utilizan cuando todos los elementos son del mismo tipo y necesitas operaciones más específicas (similares a los arrays en C o Java).

## Importar y crear un array

Para usar arrays, necesitas importar el módulo array:

```python
import array

# Crear un array de enteros
numeros = array.array('i', [10, 20, 30])
print(numeros)  # array('i', [10, 20, 30])
```

## Tipos de datos en arrays

El primer argumento al crear un array indica el tipo de datos:

- 'i': Enteros (4 bytes).
- 'f': Flotantes (4 bytes).
- 'd': Flotantes de doble precisión (8 bytes).

## Acceso y operaciones básicas

El acceso a los elementos funciona igual que en las listas:

```python
print(numeros[0])  # 10
numeros.append(40)
print(numeros)  # array('i', [10, 20, 30, 40])
```

# 3. Listas multidimensionales

Las listas pueden contener otras listas, permitiendo crear estructuras como matrices:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  # 6
```

# 4. Manipulación avanzada de listas

## Comprensión de listas (List Comprehension)

Es una forma concisa de crear listas nuevas a partir de iterables:

```python
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# Filtrar elementos
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```
