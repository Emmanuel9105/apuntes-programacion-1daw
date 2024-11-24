# 1. Arrays

## ¿Qué es un array?

Un array es una colección ordenada de elementos, donde cada elemento tiene un índice (posición) que empieza en 0. Los elementos pueden ser de cualquier tipo, incluidos números, strings, objetos, o incluso otros arrays.

## Declaración de un array

Se puede declarar un array de varias maneras:

1. Usando corchetes []:

```js
let frutas = ['manzana', 'banana', 'cereza']
```

2. Usando el constructor Array:

```js
let numeros = new Array(10, 20, 30)
```

## Acceso a elementos

Puedes acceder a los elementos usando su índice:

```js
console.log(frutas[0]) // "manzana"
console.log(frutas[2]) // "cereza"
```

## Propiedades y métodos comunes de los arrays

1. Propiedad .length

Devuelve el número de elementos en el array:

```js
console.log(frutas.length) // 3
```

2. Añadir elementos

- Con .push(): Añade al final.

```js
frutas.push('durazno')
console.log(frutas) // ["manzana", "banana", "cereza", "durazno"]
```

- Con .unshift(): Añade al principio.

```js
frutas.unshift('fresa')
console.log(frutas) // ["fresa", "manzana", "banana", "cereza", "durazno"]
```

3. Eliminar elementos

- Con .pop(): Elimina el último elemento.

```js
frutas.pop()
console.log(frutas) // ["fresa", "manzana", "banana", "cereza"]
```

- Con .shift(): Elimina el primer elemento.

```js
frutas.shift()
console.log(frutas) // ["manzana", "banana", "cereza"]
```

4. Recorrer un array

Usar un bucle for o forEach para iterar:

```js
frutas.forEach((fruta, index) => {
  console.log(`Fruta ${index + 1}: ${fruta}`)
})
// Fruta 1: manzana
// Fruta 2: banana
// Fruta 3: cereza
```

5. Métodos útiles

- .map(): Aplica una función a cada elemento y devuelve un nuevo array.

```js
let precios = [10, 20, 30]
let conImpuesto = precios.map(precio => precio * 1.21)
console.log(conImpuesto) // [12.1, 24.2, 36.3]
```

- .filter(): Filtra elementos según una condición.

```js
let mayoresDe20 = precios.filter(precio => precio > 20)
console.log(mayoresDe20) // [30]
```

- .reduce(): Reduce el array a un único valor.

```js
let total = precios.reduce((suma, precio) => suma + precio, 0)
console.log(total) // 60
```

# 2. Arrays multidimensionales (matrices)

Un array puede contener otros arrays:

```js
let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
console.log(matriz[1][2]) // 6
```

# 3. Manipulación avanzada

## Encontrar elementos

Usa .find() o .findIndex():

```js
let usuarios = [
  { id: 1, nombre: 'Juan' },
  { id: 2, nombre: 'Ana' }
]
let usuario = usuarios.find(u => u.id === 2)
console.log(usuario) // { id: 2, nombre: "Ana" }
```

## Ordenar arrays

Usar .sort() para ordenar:

```js
let numeros = [10, 5, 8, 1]
numeros.sort((a, b) => a - b) // Orden ascendente
console.log(numeros) // [1, 5, 8, 10]
```
