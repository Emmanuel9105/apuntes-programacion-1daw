// Esto es un comentario de una linea

/*
    Esto es un comentario
    de varias lineas
*/

// Declaración antigua que no hace caso al scope (ámbito) de trabajo.
var variableEnDesuso = 'Declaración de variable en desuso'
// Declaración moderna que tiene en cuenta el scope (ámbito) de trabajo.
let variableEnUso = 'Declaración de variable en uso'
// Declaración moderna e inmutable que tiene en cuenta el scope (ámbito) de trabajo.
const CONSTANTE_EN_USO = 'Declaración de constante en uso'

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
