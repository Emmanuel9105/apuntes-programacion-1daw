# 1. Creación de matrices bidimensionales

## Declaración directa

Puedes declarar una matriz bidimensional manualmente asignando arrays dentro de otro array:

```js
let matriz = [
  [1, 2, 3], // Fila 0
  [4, 5, 6], // Fila 1
  [7, 8, 9] // Fila 2
]
```

En este caso, matriz[0][1] accederá al elemento en la fila 0, columna 1 (valor 2).

## Creación dinámica

Puedes crear una matriz bidimensional dinámica con bucles anidados:

```js
let filas = 3
let columnas = 4
let matriz = []

for (let i = 0; i < filas; i++) {
  matriz[i] = [] // Crea una nueva fila
  for (let j = 0; j < columnas; j++) {
    matriz[i][j] = i * j // Llena con algún valor
  }
}

console.log(matriz)
// Imprime:
// [
//   [0, 0, 0, 0],
//   [0, 1, 2, 3],
//   [0, 2, 4, 6]
// ]
```

2. Acceso a elementos

Puedes acceder a los elementos de una matriz usando dos índices:

```js
console.log(matriz[0][1]) // Fila 0, Columna 1 -> Imprime: 0
console.log(matriz[2][3]) // Fila 2, Columna 3 -> Imprime: 6
```

# 3. Recorrer una matriz bidimensional

## Usando bucles anidados

Para recorrer toda la matriz, utiliza un bucle for anidado:

```js
for (let i = 0; i < matriz.length; i++) {
  // Recorre las filas
  for (let j = 0; j < matriz[i].length; j++) {
    // Recorre las columnas
    console.log(`Elemento en [${i}][${j}]: ${matriz[i][j]}`)
  }
}
```

## Usando forEach

Puedes recorrer cada fila y columna utilizando el método forEach:

# 4. Modificación de elementos

Puedes modificar elementos específicos de la matriz usando sus índices:

```js
matriz[1][2] = 99 // Cambia el elemento en fila 1, columna 2
console.log(matriz)
// [
//   [0, 0, 0, 0],
//   [0, 1, 99, 3],
//   [0, 2, 4, 6]
// ]
```

# 5. Operaciones comunes

## Agregar una fila

Usa el método push() para agregar una nueva fila al final de la matriz:

```js
matriz.push([10, 11, 12, 13])
console.log(matriz)
// [
//   [0, 0, 0, 0],
//   [0, 1, 99, 3],
//   [0, 2, 4, 6],
//   [10, 11, 12, 13]
// ]
```

## Eliminar una fila

Usa el método pop() para eliminar la última fila:

```js
matriz.pop()
console.log(matriz)
// [
//   [0, 0, 0, 0],
//   [0, 1, 99, 3],
//   [0, 2, 4, 6]
// ]
```

## Agregar una columna

Recorre cada fila y agrega un nuevo elemento:

```js
matriz.forEach(fila => fila.push(0))
console.log(matriz)
// [
//   [0, 0, 0, 0, 0],
//   [0, 1, 99, 3, 0],
//   [0, 2, 4, 6, 0]
// ]
```

## Eliminar una columna

Recorre cada fila y elimina el último elemento:

```js
matriz.forEach(fila => fila.pop())
console.log(matriz)
// [
//   [0, 0, 0, 0],
//   [0, 1, 99, 3],
//   [0, 2, 4, 6]
// ]
```

# 6. Ejemplos prácticos

## Suma de todos los elementos

```js
let suma = 0

matriz.forEach(fila => {
  fila.forEach(valor => {
    suma += valor
  })
})

console.log(`Suma total: ${suma}`) // Suma de todos los elementos de la matriz
```

## Transposición de una matriz

La transposición de una matriz intercambia las filas con las columnas:

```js
let transpuesta = []

for (let i = 0; i < matriz[0].length; i++) {
  transpuesta[i] = []
  for (let j = 0; j < matriz.length; j++) {
    transpuesta[i][j] = matriz[j][i]
  }
}

console.log(transpuesta)
// Transpone la matriz original
```

## Multiplicación de matrices

Para multiplicar dos matrices, el número de columnas de la primera debe coincidir con el número de filas de la segunda:

```js
let matrizA = [
  [1, 2, 3],
  [4, 5, 6]
]

let matrizB = [
  [7, 8],
  [9, 10],
  [11, 12]
]

let resultado = []

for (let i = 0; i < matrizA.length; i++) {
  resultado[i] = []
  for (let j = 0; j < matrizB[0].length; j++) {
    let suma = 0
    for (let k = 0; k < matrizA[0].length; k++) {
      suma += matrizA[i][k] * matrizB[k][j]
    }
    resultado[i][j] = suma
  }
}

console.log(resultado)
// Imprime la matriz resultante
```

# 7. Ventajas y desventajas de matrices bidimensionales en JavaScript

## Ventajas

- Representación directa y clara de datos tabulares.
- Flexibilidad para representar datos dinámicos.
- Compatible con las potentes funciones de array de JavaScript (map, filter, reduce, etc.).

## Desventajas

- No es tan eficiente para operaciones complejas como estructuras especializadas (por ejemplo, librerías de álgebra lineal).
- La gestión de índices puede ser propensa a errores en grandes matrices.
