# retotecnico-cobol

## Introduccion:

El reto tiene como proposito demostrar habilidades en procesamiento de datos, manejo de archivos y generación de reportes.
Esto consiste en procesar un archivo CSV con transacciones bancarias y generar un reporte :
    - Balance final (Creditos - debitos)
    - Transacciones de mayor monto
    - Contro de transacciones por tipo

## Instrucciones de Ejecucion:
     ### Requisitos
        - python <= 3.13
        - no se requiere dependencias, csv dentro del paquete de python
     ### Ejecución
        - Clona repositorio     -> git clone https://github.com/codeableorg/interbank-academy-25
        - Define path "archivo.csv" 
        - Ejecuta el programa   -> python reporte_transacciones.py
            

## Enfoque y Solución:
    - Lectura de datos: Uso de liberia csv para manejar eficientemente los datos.
    

    - Procesamiento
      * Definción de función "transaccion"
      * Lectura de archivo
      * Logica de comparación
      * Acumuladores separados para creditos y debitos
      * Comparacion para hallar el monto maximo
      * Contadores por tipo de transaccion      
      * Manejo de errores: Validacion de archivo y formato de datos

## Estructura del Proyecto:
```
/retotecnico-cobol/
    │
    ├── reporte_transacciones.py  # Script principal 
    ├── data.csv                  # Archivo CSV de ejemplo
    ├── README.md                 # Este archivo con documentacion
    ├──requirements.txt           # Version 3.13.1 py

```