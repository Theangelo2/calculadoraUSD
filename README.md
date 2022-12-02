
# Calculadora de Divisas 
Esta es una calculadora de divisas desarollada en python, sin fraameworks que utilza 2 libreias
y consulta via api los valores.




## Instalacion
Para poder utilizar este script esta necesario instalar: python3 y las librerias "request" y "json"
Para ello debemos descargar python3 en base al SO que tengas en el siguiente link: https://www.python.org/downloads/
y tener pip instalado: https://pip.pypa.io/en/stable/installation/

Luego de descargarlo debemos ejecutar

```bash
  python -m pip install requests
```
Una vez instalado la liberia requets instalamos la liberia json

```bash
  python -m pip install json
```


## Deployment
Una vez instaladas las dependencias podemos ejecutar el script de la siguientes formas 
```bash
  python3 .\dolar.py  
```
Nota importante: Tenes en cuenta que debemos estar en el mismo directorio que el script caso contrario es muy probable que nos indique que no encuentra el archivo.

## FAQ

### ¿Cuantas Divisas puedo Convertir?

Podes convertir 4 formas:

- De Dolar a Peso

- De Peso a Dolar

- De Euro a Peso

- De Peso a Euro

### ¿Donde Calcula las cotizaciones?
De la siguiente api https://github.com/Castrogiovanni20/api-dolar-argentina

### ¿Tengo que ingresar algun comando?
No, no hace falta solo con ingresar lo que indican los menus es suficiente

### ¿Es key sensitive el menu?
Si, es Key sensitive, te recomendamos ingresar tal cual indican las opciones respetando las mayusculas.
Ejemplo
```bash
Tipo de Conversiones de Divisas:

    1 - Conversion de ARS a USD

    2 - Conversion de ARS a EUR

    3 - Conversion de USD a ARS

    4 - Conversion de EUR a ARS
    
    ingrese la opcion numerica:
```
Deberas ingresar 1, caso contrario te arrojará el error:
```bash
ingrese la opcion numerica:  
Error de Input por favor coloque una opcion validad ejemplo 1 y presione enter 

intentos 0
```

Ten en cuenta que a los 4 intentos se cerrara la ejecucion
