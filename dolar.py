########## ENCUNCIADO ##########
# Desarrollar un script de línea de comandos que reciba como argumentos:
# Monto
# Moneda (debe aceptar ARS, otra más opcional)
# El script obtendrá la cotización del USD desde alguna página web.
# Mostrará en pantalla la cotización del USD y además el equivalente en USD al monto ingresado por línea de comandos.
# Escribir en Bash o Python, sin ningún framework.
# Incluir control de errores a lo ingresado por línea de comandos y a los posibles errores al obtener la cotización de USD.
# Debe incluir notas y comentarios en el código para entender su funcionamiento y decisiones tomadas.
# El código se puede enviar por este correo o mediante github.
########## FIN ENUNCIADO ##########


#Librerias Usadas
#Como instalar?
#

import requests
import json

#### Bloque de clases ####
#Clases de Colores para formatear texto en consola utilizando Código escape ANSI, para formatearlo en consola.
class bold_color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#### Fin de Bloque de Clases ####


######## BLOQUE FUNCIONES ########
#  FUNCION MAIN: Esta funcion es la responsable de onboarding y desplegar el menu de opciones
#  retorna e instancia la variable "options" que es la responsable de almacenar la opcion selecionada por el usuario. 
#  El tipo de dato que almacena es un string.
#  Esta funcion tambien verifica que el ususario seleccione correctamente la opcion dentro de los valores enteros de 1, 2,3 y 4 le da 3 intentos 
#  luego de esos 3 intentos finaliza la ejecucion del programa\script

def main ():
    print("""
    Tipo de Conversiones de Divisas:
    1 - Conversion de ARS a USD
    2 - Conversion de ARS a EUR
    3 - Conversion de USD a ARS
    4 - Conversion de EUR a ARS
    """)
    intentos=0
    #Bucle infinito para permitir reintentos al usuario.
    while intentos <= 3:
            #asignacion de variable por input del usuario
        options = input("ingrese la opcion numerica: ")
            #Verifico si el usuario ingresa las opciones correctas
        if options in ["1","2","3","4"]:
            #Reitero la opcion seleccionada
            print("Selecciono opcion: ", options)
            #Devuelvo el valor de options.
            return options  
        else:
            #Si falla en colocar una opcion muestro este error y sumo intentos para romper el ciclo while.
            print("Error de Input por favor coloque una opcion validad ejemplo 1 y presione enter \n ")
            intentos+=1
            print("intentos",intentos-1)
    #Rompo ejecucion
    quit()

#  FUNCION "conectivity": Esta funcion es la responsable de verificar la conexion de la API
#  Uso la libreria requests para conectarme con la api publica que actualiza la cotizancion del dolar en tiempo real: https://github.com/Castrogiovanni20/api-dolar-argentina  
#  y asi obtener los estados de la api.
#  en caso que no sea 200 el codigo de respuesta, automaticamente arroja un error de conexion con el estatus code.


def conectivity ():
    response = requests.get("https://api-dolar-argentina.herokuapp.com/")
    print("Estado de Conexion")
    if response.status_code == 200:
        print("Conexion exitosa")
    else:
        print("Error de conexion: ", response.status_code)

#  FUNCION "input_exchange": Esta funcion es la responsable de verificar y convetir errores tipeo. Cuenta con Reintentos por error y luego cierra ejecucion.
#  y asi obtener los estados de la api.
#  en caso que falle el programa se cierra, a exepto que se coloque un numero negativo. que en ese caso solicita infinitos intentos.

def input_exchange ():
    intentos=1

    while intentos <= 3:
        #  Pido el valor de entrada a convertir y luego lo almaceno en la variable value
        value=input("ingrese el valor a convertir expresado en forma decimal: ")   
        try:
            #Utilizo Try para convetir y asegurar que el valor es decimal y puede converirse de str a float.
            value=value.replace(",", ".")
            value=float(value)
            #Valido el numero para que siempre sea positivo caso contrario fuerzo a que vuelva a intentar n veces.
            if value >= 0: 
                return value
            else:
                print("error verifique que no este ingresando un numero negativo")
        except:
            print("ERROR en la expresion intente nuevamente")
            intentos+=1              
    #Cuando salgo del loop arrojo error con intentos y cierro programa.
    print("Se cierra programa por cantidad de intentos: ", intentos-1)
    quit()          
    

#  FUNCION "exchange_money": Esta funcion es la responsable de calcular, mostar y verificar los diferentes tipos de divisas aparte que cuenta con un menu propio. 
#  Esta funcion cuenta con un menu interno para cotizar 3 tipos de dolares diferentes y euros, aparte que toma el valor de la opcion que selecciona el usuario.
#  Cuenta con control de errores y ciclo de menu.
#  Tambien consulta y se conecta con la api: https://github.com/Castrogiovanni20/api-dolar-argentina y en base al menu selecciona las opciones hace una consulta u otra.

def exchange_money (rsp_of_menu,value):
    intentos=1
    responseeur= requests.get("https://api-dolar-argentina.herokuapp.com/api/euro/nacion")
    cotizationeur = float(json.loads(responseeur.text)['compra'])
    selleur = float(json.loads(responseeur.text)['venta'])
    timeeur = str(json.loads(responseeur.text)['fecha'])
    
    #Calculo de opciones basado en la seleccion del usuario en la funcion MAIN
    if rsp_of_menu == "1":
        #while en loop para reiterar hasta 3 veces el menu.
        while intentos <=3: 
           
            print("""
            Que tipo de dolar queres cotizar:
            A -  Dolar Oficial
            B -  Dolar Blue
            C -  Contado con Liqui 
            """)
            #asignacion de variable por input del usuario
            pdolar=input("Ingrese la Opcion: ")
             #Verifico si el usuario ingresa las opciones correctas
            if pdolar in ["A","B","C"]:
                #Reitero la opcion seleccionada
                print("Selecciono opcion: ", pdolar)
                #Verifico opciones en base al input del usuario
                if pdolar == "A": 
                    #Si la opcion es A aplica el dolar oficial, llamando la api del mismo consultando el valor 
                    # y la fecha en UTC y a cada variable la convierto en un float y str para poder procesarlos
                    usdvariable = "dolaroficial"
                    reponseusd = requests.get(f"https://api-dolar-argentina.herokuapp.com/api/{usdvariable}")
                    cotizationusd = float(json.loads(reponseusd.text)['compra'])
                    timeusd = str(json.loads(reponseusd.text)['fecha'])

                    #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.    
                    print("Convirtiendo ARS a Dolar Oficial - Cantidad indicada: ",value,"\n")
                    print("Fecha de Cotizacion: " + bold_color.BOLD + timeusd + bold_color.END +"\n")
                    print("Valor de Precio de Compra: ",cotizationusd)

                    #Calculo el valor de los pesos diviendolos por el dolar.
                    ariop = value/cotizationusd
                    #Muestro resultado formateado
                    print("Total en Dolar Oficial: "+ bold_color.RED +"{0:.2f}".format(ariop)+bold_color.END)
                    return ariop
                #Opcion B
                elif pdolar == "B":
                    #Si la opcion es B aplica el dolar blue, llamando la api del mismo consultando el valor 
                    # y la fecha en UTC y a cada variable la convierto en un float y str para poder procesarlos
                    usdvariable = "dolarblue"
                    reponseusd = requests.get(f"https://api-dolar-argentina.herokuapp.com/api/{usdvariable}")
                    cotizationusd = float(json.loads(reponseusd.text)['compra'])
                    timeusd = str(json.loads(reponseusd.text)['fecha'])

                    #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
                    print("Convirtiendo ARS a Dolar Blue - Cantidad indicada: ",value,"\n")
                    print("Fecha de Cotizacion: " + bold_color.BOLD + timeusd + bold_color.END +"\n")
                    print("Valor de Precio de Compra: ",cotizationusd)

                    #Calculo el valor de los pesos diviendolos por el dolar.    
                    ariop = value/cotizationusd

                    #Muestro resultado formateado
                    print("Total en Dolar Blue: "+ bold_color.BLUE + "{0:.2f}".format(ariop)+bold_color.END)
                    return ariop

                #Opcion C
                elif pdolar == "C": 
                     #Si la opcion es C aplica el Contado con Liqui, llamando la api del mismo consultando el valor 
                     # y la fecha en UTC y a cada variable la convierto en un float y str para poder procesarlos
                    usdvariable = "contadoliqui"
                    reponseusd = requests.get(f"https://api-dolar-argentina.herokuapp.com/api/{usdvariable}")
                    cotizationusd = float(json.loads(reponseusd.text)['compra'])
                    timeusd = str(json.loads(reponseusd.text)['fecha'])

                    #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
                    print("Convirtiendo ARS a Contado con Liqui - Cantidad indicada: ",value,"\n")
                    print("Fecha de Cotizacion: " + bold_color.BOLD + timeusd + bold_color.END +"\n")
                    print("Valor de Precio de Compra: ",cotizationusd)

                    #Calculo el valor de los pesos diviendolos por el dolar.
                    ariop = value/cotizationusd

                    #Muestro resultado formateado
                    print("Total en Dolares Contado con Liqui: "+bold_color.GREEN+"{0:.2f}".format(ariop)+bold_color.END)
                    return ariop

                #Sumo intento para romper while
                else:
                  print(bold_color.RED + "Error al seleccionar tipo de dolar - Verifique la opcion seleccionada." + bold_color.END)
                  intentos+=1


    #Calculo de opcion 2       
    elif rsp_of_menu == "2": 
    #Recibo Input del usuario si es Opcion 2 Covierto Pesos a Euros llamando la api del mismo consultando el valor
    #  y la fecha en UTC y a cada variable la convierto en un float y str para poder procesarlos.
            
            #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
            print("Convirtiendo ARS a Euros - Cantidad indicada: ",value,"\n")
            print("Fecha de Cotizacion: "+ bold_color.BOLD + timeeur + bold_color.END +"\n")
            print("Valor de Precio de Compra: ",cotizationeur)

            #Calculo el valor de los pesos diviendolos por el dolar.
            ariop = value/cotizationeur
            
            #Muestro resultado formateado.
            print("Total en Euros: "+bold_color.PURPLE+"{0:.2f}".format(ariop)+bold_color.END)
            return ariop


    #Calculo de opcion 3
    elif rsp_of_menu == "3": 
        #while en loop para reiterar hasta 3 veces el menu de conversion inversa.
        while intentos <=3:
           

            print("""
            Que tipo de dolar queres cotizar:
            A -  Dolar Oficial
            B -  Dolar Blue
            C -  Contado con Liqui 
            """)
            #asignacion de variable por input del usuario
            pdolar=input("Ingrese la Opcion: ")

            #Verifico si el usuario ingresa las opciones correctas
            if pdolar in ["A","B","C"]:
                #Reitero la opcion seleccionada
                print("Selecciono opcion: ", pdolar)
               
                if pdolar == "A":
                    #Si la opcion es A aplica el dolar oficial, llamando la api del mismo consultando el valor y la fecha en UTC 
                    # y a cada variable la convierto en un float y str para poder procesarlo.    
                    usdvariable = "dolaroficial"
                    reponseusd = requests.get(f"https://api-dolar-argentina.herokuapp.com/api/{usdvariable}")
                    sellusd = float(json.loads(reponseusd.text)['venta'])
                    timeusd = str(json.loads(reponseusd.text)['fecha'])

                    #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
                    print("Convirtiendo Dolar Oficial a ARS - Cantidad indicada: ",value,"\n")
                    print("Fecha de Cotizacion: " + bold_color.BOLD + timeusd + bold_color.END +"\n")
                    print("Valor de Precio de Compra: ",sellusd)

                    #Calculo el valor de los pesos diviendolos por el dolar.
                    ariop = value*sellusd

                    #Muestro resultado formateado.
                    print("Total en Pesos Argentinos: "+ bold_color.RED +"{0:.2f}".format(ariop)+bold_color.END)
                    return ariop

                elif pdolar == "B":
                    #Si la opcion es B aplica el Dolar Blue, llamando la api del mismo consultando el valor y la fecha en UTC 
                    # y a cada variable la convierto en un float y str para poder procesarlo.
                    usdvariable = "dolarblue"
                    reponseusd = requests.get(f"https://api-dolar-argentina.herokuapp.com/api/{usdvariable}")
                    sellusd = float(json.loads(reponseusd.text)['venta'])
                    timeusd = str(json.loads(reponseusd.text)['fecha'])

                    #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
                    print("Convirtiendo Dolar Blue a ARS - Cantidad indicada: ",value,"\n")
                    print("Fecha de Cotizacion: " + bold_color.BOLD + timeusd + bold_color.END +"\n")
                    print("Valor de Precio de Compra: ",sellusd)
                    
                    #Calculo el valor de los pesos diviendolos por el dolar.
                    ariop = value*sellusd
                    
                    #Muestro resultado formateado.
                    print("Total en Pesos Argentinos: "+ bold_color.BLUE +"{0:.2f}".format(ariop)+bold_color.END)
                    return ariop

                elif pdolar == "C": 
                    #Si la opcion es C aplica el Dolar Contado Liqui, llamando la api del mismo consultando el valor y la fecha en UTC 
                    # y a cada variable la convierto en un float y str para poder procesarlo.
                    usdvariable = "contadoliqui"
                    reponseusd = requests.get(f"https://api-dolar-argentina.herokuapp.com/api/{usdvariable}")
                    sellusd = float(json.loads(reponseusd.text)['venta'])
                    timeusd = str(json.loads(reponseusd.text)['fecha'])

                    #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
                    print("Convirtiendo Dolar Contado con Liqui a ARS - Cantidad indicada: ",value,"\n")
                    print("Fecha de Cotizacion: " + bold_color.BOLD + timeusd + bold_color.END +"\n")
                    print("Valor de Precio de Compra: ",sellusd)
                    
                    #Calculo el valor de los pesos diviendolos por el dolar.
                    ariop = value*sellusd
                    
                    #Muestro resultado formateado.
                    print("Total en Pesos Argentinos: "+ bold_color.GREEN +"{0:.2f}".format(ariop)+bold_color.END)
                    return ariop
            
                else:
                  #Sumo intento para romper while
                  print("Error al seleccionar tipo de dolar - Verifique la opcion seleccionada.")
                  intentos+=1

    #Calculo de opcion 4
    elif rsp_of_menu == "4": 
    #Recibo Input del usuario si es Opcion 4 Covierto Euros a Pesos llamando la api del mismo consultando el valor
    #y la fecha en UTC y a cada variable la convierto en un float y str para poder procesarlos.
            
            #Muestro los inputs valores de las variables consultadas formateadas con la clase declarada.
            print("Convirtiendo Euros a ARS - Cantidad indicada: ",value,"\n")
            print("Fecha de Cotizacion: ",timeeur,"\n")
            print("Valor de Precio de Compra: ",selleur)
        
            #Calculo el valor de los pesos diviendolos por el dolar.
            ariop = value*selleur
        
            #Muestro resultado formateado.
            print("Total en Pesos: "+bold_color.PURPLE+"{0:.2f}".format(ariop)+bold_color.END)
            return ariop  
    else:    
        #Mensaje de Input Incorrecto que obliga a seguir en el loop.        
        print("Error de Input por favor coloque una opcion valida "+bold_color.RED+"\n"+bold_color.END)

######## FIN DEL BLOQUE FUNCIONES ########   
   
### bloque de codigo main ###
#Loop Infinito para que el usuario pueda repetir el proceso, saliendo del loop ingresando el str Y.
while True: 
    print(bold_color.RED +"Bienvenido a la calculadora de divisas","\n"+bold_color.END)
    #Verifico la conexion con la funcion
    conectivity()
    #Almaceno la variable del return de Main 
    rsp_of_menu=main()
    #Almaceno la variable del return de input_exchange
    exchange= input_exchange()

    #Ejecuto y envio los parametros generados por las funciones main y input_exchange, enviadolos al menu de cotizador
    finalcotization=exchange_money(rsp_of_menu,exchange)
    
    #Variable de escape para salir del Loop del While.
    election=input("Para Realizar otra cotizacion ingrese Y caso contrario ingrese cualquier tecla para que finalice la ejecucion "+bold_color.END)

    #Condicionate para escapar del while, si envia cualquier input sale de la ejecucion con mensaje de despedida.
    if election == "Y":
        continue
    else:
        print("Muchas gracias por usar la Calculadora de Divisas, el programa se cerrara")
        break




