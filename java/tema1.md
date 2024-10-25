# Java cheatsheet

## Comentarios

```java
// Este es un comentario de una sola línea
```

```java
/*
 Este es un comentario de múltiples líneas.
 Es útil para añadir descripciones largas o
 explicaciones detalladas.
*/
```

## Imprimir información por consola

```java
System.out.println("¡Hola mundo!"); // ¡Hola mundo!
```

```java
System.out.print("¡Hola ");
System.out.print("mundo!");
// ¡Hola mundo!
```

```java
String nombre = "Jero";
int edad = 22;
System.out.printf("Nombre: %s, Edad: %d", nombre, edad);
// Nombre: Jero, Edad: 22
```

## Introducir información por consola

```java
// Importar Scanner en la parte superior del documento
import java.util.Scanner;
```

```java
Scanner scanner = new Scanner(System.in);

System.out.print("Introduce tu nombre: ");
String nombre = scanner.nextLine(); // Lee una línea completa

System.out.print("Introduce tu edad: ");
int edad = scanner.nextInt(); // Lee un número entero

System.out.println("Nombre: " + nombre + ", Edad: " + edad);
// Nombre: XXX, Edad: 000

scanner.close(); // Cerrar el Scanner cuando ya no se necesite
```

## Variables y asignación

### Primitivos

```java
// Número entero de 8 bits, con rango de -128 a 127
byte edad = 22;
// Número entero de 16 bits, con rango de -32,768 a 32,767
short año = 2024;
// Número entero de 64 bits, con rango de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807; ‘L’ al final indica que es un `long`
long distanciaEstrella = 123456789012345L;
// Número de coma flotante de precisión simple de 32 bits; ‘f’ indica que es un `float`
float precio = 19.99f;
// Número de coma flotante de precisión doble de 64 bits; es el tipo decimal más común
double pi = 3.14159;
// Representa valores de verdad; true o false
boolean esMayorEdad = true;
// Almacena un solo carácter Unicode de 16 bits
char inicial = 'A';
```

### De referencia

```java
// Almacena secuencias de caracteres
String nombre = "Juan";
// Una lista (array, arreglo, vector) almacena múltiples valores del mismo tipo en una estructura fija.
int[] numeros = {1, 2, 3, 4, 5};
```

### Constantes

```java
// Su valor se fija al declararlas
final int EDAD_MAXIMA = 100;
// Static se utiliza para declarar constantes a nivel de clase que no cambian y pueden ser accedidas sin crear una instancia de la clase
public static final double PI = 3.14159;
```

## Operadores lógicos

AND

```java
boolean a = true;
boolean b = false;
System.out.println(a && b); // false
```

OR

```java
boolean a = true;
boolean b = false;
System.out.println(a || b); // true
```

NOT

```java
boolean a = true;
System.out.println(!a); // false
```

XOR

```java
boolean a = true;
boolean b = false;
System.out.println(a ^ b); // true
```

## Comparadores lógicos

Mayor que

```java
int a = 5;
int b = 3;
boolean resultado = a > b; // true
```

Menor que

```java
int a = 5;
int b = 3;
boolean resultado = a < b; // false
```

Mayor o igual que

```java
int a = 5;
int b = 5;
boolean resultado = a >= b; // true
```

Menor o igual que

```java
int a = 5;
int b = 6;
boolean resultado = a <= b; // true
```

Igual que

```java
int a = 5;
int b = 5;
boolean resultado = a == b; // true
```

Diferente que

```java
int a = 5;
int b = 3;
boolean resultado = a != b; // true
```

## Operadores aritméticos

Suma

```java
int a = 5;
int b = 3;
int resultado = a + b; // 8
```

Resta

```java
int a = 5;
int b = 3;
int resultado = a - b; // 2
```

Multiplicación

```java
int a = 5;
int b = 3;
int resultado = a * b; // 15
```

División

```java
int a = 10;
int b = 3;
int resultado = a / b; // 3
double resultadoConDecimales = (double) a / b; // 3.3333
```

Módulo

```java
int a = 10;
int b = 3;
int resultado = a % b; // 1
```

Incremento

```java
int a = 5;
int resultadoPreIncremento = ++a; // resultado = 6, a = 6
int resultadoPostIncremento = a++; // resultado = 6, a = 7
```

Decremento

```java
int a = 5;
int resultadoPreDecremento = --a; // resultado = 4, a = 4
int resultadoPostDecremento = a--; // resultado = 4, a = 3
```

Suma y asignación

```java
int a = 5;
a += 3; // a = a + 3; Resultado: a = 8
```

Resta y asignación

```java
int a = 5;
a -= 3; // a = a - 3; Resultado: a = 2
```

Multiplicación y asignación

```java
int a = 5;
a *= 3; // a = a * 3; Resultado: a = 15
```

División y asignación

```java
int a = 10;
a /= 2; // a = a / 2; Resultado: a = 5
```

Módulo y asignación

```java
int a = 10;
a %= 3; // a = a % 3; Resultado: a = 1
```

## Condiciones

```java
int numero = 0;

if (numero > 0) {
  System.out.println("El número es positivo."); // No se imprimirá por consola
} else if (numero < 0) {
  System.out.println("El número es negativo."); // No se imprimirá por consola
} else {
  System.out.println("El número es cero."); // Se imprimirá por consola
}
```

## Condición anidada

```java
int edad = 16;

if (edad >= 18) {
  System.out.println("Eres mayor de edad."); // No se imprimirá por consola
} else {
  if (edad >= 13) {
    System.out.println("Eres un adolescente."); // Se imprimirá por consola
  } else {
    System.out.println("Eres un niño."); // No se imprimirá por consola
  }
}
```

## Bucle While

```java
int contador = 1;

while (contador <= 5) {
  System.out.println(contador);
  contador++; // Incrementa el contador en 1
}
```

## Bucle Do while

```java
int contador = 1;

do {
  System.out.println(contador);
  contador++; // Incrementa el contador en 1
} while (contador <= 5);
```

## Bucle For

```java
for (int i = 1; i <= 5; i++) {
  System.out.println(i);
}
```

## Longitud de elementos

```java
String texto = "Hola, mundo!";

// Obtener la longitud de la cadena
int longitud = texto.length();
```

```java
String texto = "Hola, mundo!";

// Subcadena que contenga los caracteres del índice 0 al 4
String subcadena = texto.substring(0, 4); // Incluye 0, 1, 2, 3 (4 es exclusivo)
```

## Funciones

Función sin parámetros ni retorno

```java
public int saludo() {
  System.out.println("Hola");
}
```

Función con parámetros sin retorno

```java
public int saludo(String nombre) {
  System.out.println("Hola " + nombre);
}
```

Función sin parámetros con retorno

```java
public int suma() {
  return 10 + 12;
}
```

Función con parámetros y retorno

```java
public int saludo(String nombre) {
  return "Hola " + nombre;
}
```

## Excepciones

```java
try {
  int resultado = 10 / 0; // Esto lanza una ArithmeticException
  System.out.println("El resultado es: " + resultado);
} catch (ArithmeticException e) {
  System.out.println("Error: No se puede dividir por cero.");
} finally {
  System.out.println("Este bloque se ejecuta siempre.");
}
```
