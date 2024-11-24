# 1. Arrays en Java

## ¿Qué es un array?

Un array es una estructura de datos que almacena elementos del mismo tipo. Su tamaño es fijo, y los elementos se indexan desde 0 hasta n-1 (donde n es la longitud del array).

## Declaración y creación de un array

Puedes declarar y crear un array de las siguientes maneras:

1. Declaración y asignación inmediata:

```java
int[] numeros = {10, 20, 30, 40}; // Un array de enteros
```

2. Declaración y creación por separado:

```java
int[] numeros = new int[4]; // Array con espacio para 4 enteros
numeros[0] = 10;
numeros[1] = 20;
numeros[2] = 30;
numeros[3] = 40;
```

## Acceso a elementos

Puedes acceder a los elementos de un array usando índices:

```java
System.out.println(numeros[0]); // Imprime: 10
System.out.println(numeros[3]); // Imprime: 40
```

## Propiedades y operaciones con arrays

1. Propiedad length

Devuelve la longitud del array:

```java
System.out.println(numeros.length); // Imprime: 4
```

2. Recorrer un array

- Usando un bucle for:

```java
for (int i = 0; i < numeros.length; i++) {
    System.out.println(numeros[i]);
}
```

- Usando un bucle for-each:

```java
for (int numero : numeros) {
    System.out.println(numero);
}
```

3. Arrays multidimensionales

Los arrays en Java pueden ser multidimensionales, como una matriz:

```java
int[][] matriz = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
System.out.println(matriz[1][2]); // Imprime: 6
```

## Limitaciones de los arrays

Tamaño fijo: Una vez creado, no puedes cambiar su tamaño.
Operaciones limitadas: No tiene métodos avanzados como los que ofrecen las listas (agregar, eliminar, etc.).

# 2. Listas en Java

## ¿Qué es una lista?

Las listas (implementadas a través de la interfaz List en Java) son estructuras de datos dinámicas que pueden cambiar de tamaño y ofrecen una variedad de métodos útiles para manipular datos.

## Declaración y creación de listas

Para usar listas, generalmente utilizamos la implementación ArrayList de la interfaz List. Debes importar el paquete java.util:

1. Declaración de una lista de enteros:

```java
import java.util.ArrayList;
import java.util.List;

List<Integer> numeros = new ArrayList<>();
```

2. Declaración de una lista de cadenas:

```java
List<String> frutas = new ArrayList<>();
```

## Agregar elementos

Usa el método add() para agregar elementos a la lista:

```java
frutas.add("Manzana");
frutas.add("Banana");
frutas.add("Cereza");

System.out.println(frutas); // Imprime: [Manzana, Banana, Cereza]
```

## Acceso a elementos

Usa el método get() para acceder a un elemento por su índice:

```java
System.out.println(frutas.get(0)); // Imprime: Manzana
System.out.println(frutas.get(2)); // Imprime: Cereza
```

## Propiedades y métodos comunes de listas

1. Tamaño de la lista

Usa size() para obtener el número de elementos:

```java
System.out.println(frutas.size()); // Imprime: 3
```

2. Eliminar elementos

- Por índice:

```java
frutas.remove(1); // Elimina "Banana"
System.out.println(frutas); // Imprime: [Manzana, Cereza]
```

- Por valor:

```java
frutas.remove("Cereza");
System.out.println(frutas); // Imprime: [Manzana]
```

3. Recorrer una lista

- Usando un bucle for:

```java
for (int i = 0; i < frutas.size(); i++) {
    System.out.println(frutas.get(i));
}
```

- Usando un bucle for-each:

```java
for (String fruta : frutas) {
    System.out.println(fruta);
}
```

## Métodos avanzados de las listas

1. Buscar elementos

- contains(): Verifica si un elemento está en la lista.

```java
System.out.println(frutas.contains("Manzana")); // Imprime: true
```

- indexOf(): Devuelve el índice de la primera aparición de un elemento.

```java
System.out.println(frutas.indexOf("Manzana")); // Imprime: 0
```

2. Ordenar una lista

Usa Collections.sort() para ordenar una lista:

```java
import java.util.Collections;

List<Integer> numeros = new ArrayList<>();
numeros.add(30);
numeros.add(10);
numeros.add(20);

Collections.sort(numeros); // Orden ascendente
System.out.println(numeros); // Imprime: [10, 20, 30]
```

3. Vaciar la lista

Usa clear() para eliminar todos los elementos:

```java
frutas.clear();
System.out.println(frutas); // Imprime: []
```

# 3. Diferencias entre arrays y listas

<!-- Tabla de diferencias -->

| Característica    | Array        | List (ArrayList)         |
| ----------------- | ------------ | ------------------------ |
| Tamaño            | Fijo         | Dinámico                 |
| Tipo de datos     | Solo uno     | Puede contener genéricos |
| Métodos avanzados | Limitados    | Amplia variedad          |
| Importación       | No requerida | Requiere java.util       |
