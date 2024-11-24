# 1. ¿Qué es JSON?

El JSON (JavaScript Object Notation) es un formato ligero para el intercambio de datos. Es ampliamente utilizado para transmitir información entre un cliente y un servidor, y es nativo en JavaScript, lo que lo hace fácil de usar.

JSON es una representación textual de datos estructurados. Está basado en pares clave-valor (como objetos de JavaScript) y en listas ordenadas de valores (como arrays).

## Formato JSON

```json
{
  "nombre": "Juan",
  "edad": 30,
  "esEstudiante": false,
  "hobbies": ["leer", "programar", "deportes"],
  "direccion": {
    "calle": "Calle Falsa",
    "numero": 123,
    "ciudad": "Springfield"
  }
}
```

# 2. Sintaxis JSON

## Tipos de datos admitidos

1. Cadenas: "texto" (deben ir entre comillas dobles ").
2. Números: 123, 45.67.
3. Booleanos: true o false.
4. Nulos: null.
5. Arrays: [valor1, valor2, ...].
6. Objetos: { "clave": "valor" }.

# 3. Uso de JSON en JavaScript

## 3.1 Creación de objetos JSON

En JavaScript, puedes usar un objeto estándar o un JSON:

```js
const persona = {
  nombre: 'Juan',
  edad: 30,
  esEstudiante: false,
  hobbies: ['leer', 'programar', 'deportes'],
  direccion: {
    calle: 'Calle Falsa',
    numero: 123,
    ciudad: 'Springfield'
  }
}

console.log(persona.nombre) // Acceder al valor "Juan"
console.log(persona.hobbies[1]) // Acceder al segundo hobby "programar"
```

## 3.2 Conversión entre JSON y cadenas (serialización y deserialización)

JavaScript proporciona dos métodos principales para trabajar con JSON:

`JSON.stringify`

Convierte un objeto JavaScript en una cadena JSON (serialización).

```js
const personaJSON = JSON.stringify(persona)
console.log(personaJSON)
// Salida: {"nombre":"Juan","edad":30,"esEstudiante":false,"hobbies":["leer","programar","deportes"],"direccion":{"calle":"Calle Falsa","numero":123,"ciudad":"Springfield"}}
```

`JSON.parse`

Convierte una cadena JSON en un objeto JavaScript (deserialización).

```js
const cadenaJSON = '{"nombre":"Ana","edad":25,"esEstudiante":true}'
const personaObjeto = JSON.parse(cadenaJSON)
console.log(personaObjeto.nombre) // Salida: "Ana"
```

# 4. Ejemplos prácticos

## 4.1 Enviar y recibir datos con JSON

En aplicaciones web, JSON se utiliza para interactuar con APIs.

Enviar datos con `fetch`

```js
const usuario = {
  nombre: 'Carlos',
  correo: 'carlos@example.com',
  edad: 29
}

fetch('https://api.example.com/usuarios', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(usuario) // Convertir objeto a JSON
})
  .then(response => response.json()) // Convertir respuesta a objeto
  .then(data => {
    console.log('Respuesta del servidor:', data)
  })
  .catch(error => {
    console.error('Error:', error)
  })
```

Recibir datos

```js
fetch('https://api.example.com/usuarios')
  .then(response => response.json()) // Convertir respuesta JSON a objeto
  .then(data => {
    console.log('Usuarios recibidos:', data)
  })
  .catch(error => {
    console.error('Error al obtener datos:', error)
  })
```

## 4.2 Validar JSON

Antes de procesar una cadena JSON, puedes validarla:

```js
const cadenaJSON = '{"nombre":"Luisa","edad":28}'
try {
  const objeto = JSON.parse(cadenaJSON)
  console.log('JSON válido:', objeto)
} catch (error) {
  console.error('JSON inválido:', error.message)
}
```

## 4.3 Modificar un JSON

Los JSON son objetos manipulables como cualquier otro en JavaScript:

```js
const usuario = {
  nombre: 'Pedro',
  edad: 35
}

// Agregar una nueva clave
usuario.esEstudiante = false

// Modificar un valor
usuario.edad = 36

// Eliminar una clave
delete usuario.nombre

console.log(usuario)
// Salida: { edad: 36, esEstudiante: false }
```

# 5. JSON anidado

JSON puede contener estructuras complejas, como objetos dentro de arrays o viceversa:

```js
const baseDatos = {
  usuarios: [
    { id: 1, nombre: 'Juan', activo: true },
    { id: 2, nombre: 'María', activo: false }
  ],
  configuracion: {
    tema: 'oscuro',
    idioma: 'español'
  }
}

console.log(baseDatos.usuarios[0].nombre) // Salida: "Juan"
console.log(baseDatos.configuracion.tema) // Salida: "oscuro"
```

# 6. Diferencias entre JSON y objetos JavaScript

- JSON:
  - Es un formato de texto plano.
  - No admite funciones ni métodos.
  - Necesita comillas dobles (") para las claves y cadenas.
- Objeto JavaScript:
  - Es una estructura en memoria.
  - Puede contener funciones y métodos.
  - Las claves no requieren comillas obligatoriamente.

Ejemplo:

```js
// JSON válido
const json = '{"nombre":"Luis"}'

// Objeto JavaScript
const objeto = { nombre: 'Luis', saludo: () => console.log('Hola!') }
```

# 7. Aplicaciones comunes de JSON

1. APIs RESTful: JSON se usa para transmitir datos entre servidores y clientes.
2. Configuraciones: Archivos de configuración para aplicaciones.
3. Bases de datos: MongoDB y Firebase usan JSON como formato principal.

# 8. Ventajas y desventajas

## Ventajas

- Ligero y fácil de leer.
- Compatible con muchos lenguajes de programación.
- Excelente para transmitir datos en redes.

## Desventajas

- Puede ser menos eficiente que formatos binarios para datos muy grandes.
- Solo admite tipos básicos; no incluye soporte nativo para fechas o funciones.
