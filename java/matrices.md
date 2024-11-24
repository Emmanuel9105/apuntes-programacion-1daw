# 1. Declaración y creación de matrices bidimensionales

## Declaración y asignación directa

```java
int[][] matriz = {
    {1, 2, 3}, // Fila 0
    {4, 5, 6}, // Fila 1
    {7, 8, 9}  // Fila 2
};
```

Aquí, matriz[0][1] representa el elemento en la fila 0, columna 1 (valor 2).

## Creación dinámica

Usando la palabra clave new:

```java
int filas = 3;
int columnas = 4;
int[][] matriz = new int[filas][columnas];

// Inicialización
for (int i = 0; i < filas; i++) {
    for (int j = 0; j < columnas; j++) {
        matriz[i][j] = i * j;
    }
}

// Imprimir la matriz
for (int i = 0; i < filas; i++) {
    for (int j = 0; j < columnas; j++) {
        System.out.print(matriz[i][j] + " ");
    }
    System.out.println();
}
```

# 2. Acceso a elementos

Accede a los elementos de la matriz usando los índices de fila y columna:

```java
System.out.println(matriz[1][2]); // Fila 1, Columna 2
```

# 3. Recorrer una matriz bidimensional

## Usando bucles anidados

```java
for (int i = 0; i < matriz.length; i++) { // Recorre filas
    for (int j = 0; j < matriz[i].length; j++) { // Recorre columnas
        System.out.print(matriz[i][j] + " ");
    }
    System.out.println();
}
```

## Usando bucles for-each

```java
for (int[] fila : matriz) {
    for (int valor : fila) {
        System.out.print(valor + " ");
    }
    System.out.println();
}
```

# 4. Modificación de elementos

Puedes modificar los elementos de la matriz asignando nuevos valores:

```java
matriz[2][1] = 99; // Cambia el elemento en la fila 2, columna 1
System.out.println(matriz[2][1]); // Salida: 99
```

# 5. Operaciones comunes

## Agregar una fila o columna

En Java, las matrices tienen tamaño fijo. Para agregar filas o columnas, debes crear una nueva matriz y copiar los elementos existentes:

```java
int[][] nuevaMatriz = new int[matriz.length + 1][matriz[0].length];

// Copiar datos
for (int i = 0; i < matriz.length; i++) {
    for (int j = 0; j < matriz[i].length; j++) {
        nuevaMatriz[i][j] = matriz[i][j];
    }
}

// Añadir nueva fila
nuevaMatriz[3] = new int[] {10, 11, 12};
```

## Eliminar una fila o columna

No es posible eliminar directamente elementos en matrices fijas. Puedes simularlo copiando datos a una nueva matriz excluyendo la fila o columna que quieres eliminar.

# 6. Ejemplos prácticos

## Suma de todos los elementos

```java
int suma = 0;
for (int[] fila : matriz) {
    for (int valor : fila) {
        suma += valor;
    }
}
System.out.println("Suma total: " + suma);
```

## Transposición de una matriz

Intercambia filas por columnas:

```java
int[][] transpuesta = new int[matriz[0].length][matriz.length];
for (int i = 0; i < matriz.length; i++) {
    for (int j = 0; j < matriz[i].length; j++) {
        transpuesta[j][i] = matriz[i][j];
    }
}

// Imprimir transpuesta
for (int[] fila : transpuesta) {
    for (int valor : fila) {
        System.out.print(valor + " ");
    }
    System.out.println();
}
```

## Multiplicación de matrices

La multiplicación de matrices requiere que el número de columnas de la primera coincida con el número de filas de la segunda:

```java
int[][] matrizA = {
    {1, 2, 3},
    {4, 5, 6}
};
int[][] matrizB = {
    {7, 8},
    {9, 10},
    {11, 12}
};

int filasA = matrizA.length;
int columnasA = matrizA[0].length;
int columnasB = matrizB[0].length;

int[][] resultado = new int[filasA][columnasB];

for (int i = 0; i < filasA; i++) {
    for (int j = 0; j < columnasB; j++) {
        for (int k = 0; k < columnasA; k++) {
            resultado[i][j] += matrizA[i][k] * matrizB[k][j];
        }
    }
}

// Imprimir resultado
for (int[] fila : resultado) {
    for (int valor : fila) {
        System.out.print(valor + " ");
    }
    System.out.println();
}
```

# 7. Ventajas y limitaciones

## Ventajas

- Estructura clara y fácil de usar para datos tabulares.
- Permite aprovechar índices para un control preciso de filas y columnas.

## Desventajas

- Tamaño fijo: no puedes cambiar dinámicamente el tamaño de la matriz.
- Operaciones complejas como transposiciones y multiplicaciones requieren mayor esfuerzo manual.

# 8. Uso avanzado con librerías

Para cálculos matemáticos avanzados, puedes usar bibliotecas como Apache Commons Math o EJML:

```java
// Ejemplo con Apache Commons Math
import org.apache.commons.math3.linear.*;

RealMatrix matrizA = new Array2DRowRealMatrix(new double[][] {
    {1, 2, 3},
    {4, 5, 6}
});
RealMatrix matrizB = new Array2DRowRealMatrix(new double[][] {
    {7, 8},
    {9, 10},
    {11, 12}
});

RealMatrix resultado = matrizA.multiply(matrizB);
System.out.println(resultado);
```
