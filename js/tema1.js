// Esto es un comentario de una linea

/*
    Esto es un comentario
    de varias lineas
*/

// Imprimir información por consola
console.log('Esto se ve por consola')

// Introducir información por consola (en JS es por el navegador)
// Los datos siempre se envían como texto
// ! prompt('Introduce un texto:')
// Para poder trabajar con los datos hace falta guardarlos en una variable
// ! let text1 = prompt('Introduce un texto:')

// Declaración antigua que tiene en cuenta el scope (ámbito) de trabajo.
var variableEnDesuso = 'Declaración de variable en desuso'
// Declaración moderna que tiene en cuenta el scope (ámbito) de trabajo.
let variableEnUso = 'Declaración de variable en uso'
// Declaración moderna e inmutable que tiene en cuenta el scope (ámbito) de trabajo.
const CONSTANTE_EN_USO = 'Declaración de constante en uso'

// Ejemplo de uso VAR (en desuso)
function exampleVar() {
  var x = 10 // x con ID 1

  if (true) {
    var x = 20 // x con ID 1
    console.log(x) // 20 o x con ID 1
  }

  console.log(x) // 20 o x con ID 1
}

exampleVar()

// Ejemplo de uso LET (en uso)
function exampleLet() {
  let x = 10 // x con ID 1

  if (true) {
    let x = 20 // x con ID 2
    console.log(x) // 20 o x con ID 2
  }

  console.log(x) // 10 o x con ID 1
}

exampleLet()

// Comparaciones lógicas

// Asignación
variableEnUso = 'Asignación'
// Asignación de adición
variableEnUso += ' de adición' //Asignación de adición

console.log(variableEnUso)

// Asignación de resta (sólo con números)
num1 = 25
num1 -= 3 // 22
// Asignación de multiplicación (sólo con números)
num1 *= 2 // 44
// Asignación de división (sólo con números)
num1 /= 4 // 11
// Asignación de exponenciación (sólo con números)
num1 **= 2 // 121
// Asignación de residuo (sólo con números)
num1 %= 2 // 1
// Igual (sin tener en cuenta el tipo, sólo el contenido)
num1 == '0' // false
// Estrictamente igual (teniendo en cuenta el tipo y contenido)
num1 === 0 // false
// No igual (sin tener en cuenta el tipo, sólo el contenido)
num1 != '0' // true
// Estrictamente no igual (teniendo en cuenta el tipo y contenido)
num1 !== 0 // true
// Mayor que (excluye el número indicado, en este caso 4)
num1 > 4 // false
// Menor que (excluye el número indicado, en este caso 4)
num1 < 4 // true
// Mayor o igual que (incluye el número indicado, en este caso 4)
num1 >= 4 // false
// Menor que (incluye el número indicado, en este caso 4)
num1 <= 4 // true

console.log(num1)

// Operadores aritméticos

// Suma
console.log(1 + 2) // 3
// Resta
console.log(2 - 1) // 1
// Multiplicación
console.log(2 * 2) // 4
// División (divisor 0)
console.log(2 / 0) // Infinity
// División (divisor diferente a 0)
console.log(6 / 3) // 2
// Potencia
console.log(2 ** 3) // 8
// Residuo
console.log(12 % 5) // 2
// Incremento
console.log(num1++) // 1; Primero imprime el número y luego le suma 1
console.log(++num1) // 3; Primero le suma 1 y luego imprime el número
// Decremento
console.log(num1--) // 3; Primero imprime el número y luego le resta 1
console.log(--num1) // 1; Primero le resta 1 y luego imprime el número

// Operadores lógicos
// AND lógico
console.log(true && false) // false
// OR lógico
console.log(true || false) // true
// NOT lógico
console.log(!true) // false

// Condiciones

// If
if (num1 === 1) {
  console.log('Hola 1er mundo') // Esto se imprime por consola
}

// Else
if (num1 !== 1) {
  console.log('Adiós 1er mundo')
} else {
  console.log('Hola mundo') // Esto se imprime por consola
}

// Else if

if (num1 === 2) {
  console.log('Hola 2º mundo')
} else if (num1 === 1) {
  console.log('Hola 1er mundo') // Esto se imprime por consola
} else {
  console.log('Adiós a todo el mundo')
}

// Nesting (a evitar, síntoma de refactorización)
if (num1 !== 1) {
  // No se entra en este if, por lo que el siguiente no se ejecuta
  if (num1 === 1) {
    console.log('Hola 1er mundo') // Esto no se imprime por consola
  }
}

// Valores truthy y falsy
// En Javascript todo es verdadero o falso, dependiendo de su valor

// Falsy
false
0
;('') // En Javascript se escribe así, pero es '' a lo que se refiere
null
undefined
NaN

// Truthy
;('Todo lo demás') // En Javascript se escribe así, pero es 'Todo lo demás' a lo que se refiere

// While (se ejecuta mínimo 0 veces)
while (num1 <= 5) {
  console.log(num1++) // 1, 2, 3, 4, 5
}

num1 = 1
while (num1 <= 5) {
  console.log(++num1) // 2, 3, 4, 5, 6
}

// Do while (se ejecuta mínimo 1 vez)
num1 = 1
do {
  console.log(num1++) // 1, 2, 3, 4, 5
} while (num1 <= 5)

// For
num1 = 1
for (let i = 1; i <= 5; i++) {
  console.log(i) // 1, 2, 3, 4, 5
}

// For in
const FRUITS = ['Manzana', 'Pera', 'Plátano']
for (const fruit in FRUITS) {
  console.log(fruit) // 0, 1, 2
}

// For of
for (const fruit of FRUITS) {
  console.log(fruit) // Manzana; Pera; Plátano;
}

// Bucles infinitos

// While infinito
// ! NO EJECUTAR NI DESCOMENTAR
let numWhile = 1
/* 
  while (numWhile < 5) {
    console.log('Esto es un bucle infinito');
  }
  */

// El bucle deja de ser infinito de la siguiente forma
while (numWhile < 5) {
  console.log('Esto NO es un while infinito')
  numWhile++ // Esto cambia el valor del condicionante para parar el bucle en cierto momento
}

// Do while infinito
// ! NO EJECUTAR NI DESCOMENTAR
let numDoWhile = 1
/* 
  do {
    console.log('Esto es un bucle infinito');
  } while (numDoWhile < 5)
  */

// El bucle deja de ser infinito de la siguiente forma
do {
  console.log('Esto NO es un do while infinito')
  numDoWhile++
} while (numDoWhile < 5)

// For infinito
// ! NO EJECUTAR NI DESCOMENTAR
/* 
  for (;;) {
    console.log('Esto es un bucle infinito');
  } 
  */

for (let i = 1; i < 5; i++) {
  console.log('Esto NO es un for infinito')
}

// Longitud de elementos
console.log(variableEnUso.length) // 21
console.log(num1.length) // undefined (la longitud de un número no puede medirse)
console.log(FRUITS.length) // 3

// Índice de elementos
console.log(variableEnUso.slice(3, 5)) //gn (incluye el primer elemento y no incluye el segundo)

// Funciones

// Función sin parámetros ni retorno
function nombreFuncion() {
  // Código que ejecuta la función
}

function saludar() {
  console.log('Hola desde la función')
}

saludar()

// Función con parámetros sin retorno
function saludar2(nombre) {
  console.log(`Hola ${nombre}`)
}

saludar2('Emmanuel')
saludar2('Jero')

// Función sin parámetros con retorno
function suma() {
  return 10 + 12
}

console.log(suma())

// Función con parámetros y retorno
function resta(a, b) {
  return a - b
}

console.log(resta(30, 8))

// Función con parámetros y retorno pidiendo números desde el prompt
/* function mult(a, b) {
  return a * b
}

const NUM1 = parseInt(prompt('Introduce un número entero:'))
const NUM2 = parseInt(prompt('Introduce un segundo número entero:'))

console.log(mult(NUM1, NUM2)) */

// Función flecha
const flecha = () => {
  let saludo = 'Hola desde la flecha'
  console.log(saludo)
}

flecha()
console.log(flecha)

/* Función flecha contraída
  const potencia = (a, b) => {
    return a ** b
  }
 */
const potencia = (a, b) => a ** b

console.log(potencia(2, 3))

//Excepciones
let res = 10 / 0

console.log(res) // Infinity

// ! NO DESCOMENTAR O NO SE EJECUTARÁ EL RESTO DEL SCRIPT
// console.log(miNombreCompleto) // Uncaught ReferenceError: miNombreCompleto is not defined <- Variable no definida y rompería el programa

try {
  // No se debe añadir todo el código al try porque no se sabrá de dónde viene el error
  console.log(miNombreCompleto)
} catch (error) {
  console.log(`Ha ocurrido un error: ${error.message}`) // Ha ocurrido un error: miNombreCompleto is not defined
} finally {
  console.log(
    'Parte de excepciones que siempre se ejecuta falle o no el try/catch'
  ) // Siempre se ejecuta
}

function dividir(a, b) {
  if (b === 0) {
    throw new Error('No se puede dividir por 0')
  }

  return a / b
}

try {
  dividir(10, 0)
} catch (error) {
  console.log(`Error: ${error.message}`) // Error: No se puede dividir por 0
}

// * Ejercicio try/catch

// notas = [] -> Lista (array, arreglo, vector) vacía
function calcularPromedio(notas) {
  let suma = 0
  let promedio

  try {
    // i = 0; notas.length = 0 -> 0 < 0
    for (let i = 0; i < notas.length; i++) {
      suma += notas[i]
    }

    // Entra en el if porque notas.length = 0
    if (notas.length === 0) {
      // Lanza el error y pasa al catch
      throw new Error('La lista de notas está vacía')
    }

    promedio = suma / notas.length

    // Si vamos a mostrar por pantalla el resultado de la función este console.log es innecesario
    console.log(`El promedio es ${promedio}`)
  } catch (error) {
    // Imprimimos por consola
    console.log('Error:', error.message) // Error: La lista de notas está vacía
    // Asignamos promedio = null
    promedio = null
  }

  // Devolvemos promedio = null
  return promedio
}

const NOTAS_ESTUDIANTE = []
const RESULTADO = calcularPromedio(NOTAS_ESTUDIANTE)
console.log(`Resultado: ${RESULTADO}`) // Resultado: null

// * Solución del ejercicio try/catch

function calcularPromedio2(notas) {
  let suma = 0
  let promedio

  // Como notas.length = 0 entramos en el if
  if (notas.length === 0) {
    console.log('La lista de notas está vacía')
    // Salimos de la función, el resto no se ejecuta
    return null
  }

  try {
    for (let i = 0; i < notas.length; i++) {
      suma += notas[i]
    }

    promedio = suma / notas.length
  } catch (error) {
    console.log('Error:', error.message)
    promedio = null
  }

  return promedio
}

const NOTAS_ESTUDIANTE_2 = [4, 7, 6]
console.log(`Resultado: ${calcularPromedio2(NOTAS_ESTUDIANTE_2)}`)
