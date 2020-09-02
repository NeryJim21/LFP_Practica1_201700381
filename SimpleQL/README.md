SISTEMA SIMPLEQL

1] ¿Qué es SIMPLEQL?

Es una solución de software que representa una versión minimalista de lo que se conoce en el mercado como SQL. Dicho proyecto puede realizar las tareas de consultas simples. 

Funciona únicamente a nivel de consola, tiene como objetivo facilitar busquedas de atributos dentro de registros en archivos JSON.

El usuario puede escribir una serie de comandos que le devuelven valores como "nombre", "edad", "promedio" y "activo" de los registros realizados. Estos registros pueden ser mostrados en un reporte en archivo HTML que se visualiza automáticamente al ejecutar el comando REPORTAR.

2] Modo de uso:

Al ejecutar el software se le presentará el mensaje principal que le indica el ingreso de los comandos:

--------------------
  S I M P L E Q L
--------------------

Ingrese un comando: 

3] Sintaxis de comandos:

SIMPLEQL reconoce 7 sentencias distintas para la gestión de información dentro de bases de datos simples, los comandos tolerar el CASE INSENSITIVE, por lo cual pueden venir escritos en mayusculas o minúsculas. Los atributos si deben escribirse como fueron almacenados dentro de los archivos a cargar.

A continuación se presentan los comandos reconocidos por el software, una breve explicación de cada uno, y su sintaxis:

3.1] CARGAR:
El primer comando que debe ingresar es CARGAR, seguido de los nombres de los archivos en formato JSON separados por comas.

Ejemplo:   

CARGAR archivo1.json, archivo2.json, archivoN.json

3.2] SELECCIONAR:
Este comando puede usarse de dos maneras, la primera seguido de un asterisco, *, que le indica al programa que debe mostrar todos los registros realizados con sus respectivos atributos.

La segunda opción es especificando qué atributos desea observar de un registro en específico, esto utilizando el comando DONDE, que dá los parámetros para realizar las búsquedas en el registro que coincida con los valores.

Ejemplo:

SELECCIONAR *

SELECCIONAR edad, promedio DONDE nombre = "registro 1"

3.3] MAXIMO

Este comando devuelve únicamente el valor máximo de un atributo numérico, los cuales son "edad" y "promedio".

ejemplo:

MAXIMO edad
MAXIMO promedio

3.4] MINIMO

Similar al comando MAXIMO, devuelve el valor mínimo de esos mismos atributos.

ejemplo:

MINIMO edad
MINIMO promedio

3.5] SUMA

Realiza la suma de todos los registros en las propiedades numéricas "edad" y "promedio".

ejemplo:

SUMA edad
SUMA promedio

3.6] CUENTA

Este comando devuelve el total de registros encontrados en la base de datos, no es acompañado por ningún otro atributo

ejemplo:

CUENTA

3.7] REPORTAR

Con este comando el usuario puede generar un reporte en formato HTML (página web) que se abrirá automáticamente en el navegador, se debe indicar cuántos registros desea incluír en el reporte.

ejemplo:

REPORTAR 6 
Muestra los primeros 6 registros en la base de datos.

4] Archivos JSON

Los archivos JSON deben cumplir con el siguiente formato:

[
    {
        "nombre": "registro1",
        "edad": 45,
        "activo": true,
        "promedio": 56.456
    },
    {
        "nombre": "registro 2",
        "edad": 35,
        "activo": false,
        "promedio": 45.896
    }
]

Puede incluír cuantos registros desee, siempre y cuando se respeten los atributos numéricos, y que el nombre venga entre comillas dobles " ".











