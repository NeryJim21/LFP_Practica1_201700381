#Librerias
import os
import json
import webbrowser

#Variable de entrada
instruccion = " "

#Base de datos
DB = []

#Variables para seleccionar

sNombre = ''
sEdad = ''
sActivo = ''
sProm = ''
pivote = ''
pvReport = ''
iNombre = 0
conteo = 1
temp = ''
ruta = []
suma = 0
cantidad = []

#Salida MAX - MIN
outM = []

#Items para where
item = []

# Función principal          --------------------------->      C H E C K
def main():
    
    clear()
    
    print("--------------------")
    print("  S I M P L E Q L ")
    print("--------------------")
    
    print()
    
    print("Ingrese un comando: \n")

    #Quita las comas
    ingreso = input().replace(",","")

    #Separar por posiciones
    ingreso = ingreso.split()

    global instruccion

    instruccion = ingreso

    #Comando CARGAR
    if ingreso[0].lower() == "cargar":
        
       #Llama a la función para cargar archivos '.JSON' 
       readJson()
       
    elif ingreso[0].lower() == "seleccionar":
        select()

    elif ingreso[0].lower() == "maximo":
    
        maxi()

    elif ingreso[0].lower() == "minimo":
        maxi()

    elif ingreso[0].lower() == "suma":
        maxi()

    elif ingreso[0].lower() == "cuenta":
        count()

    elif ingreso[0].lower() == "reportar":
        reporte()
    
    else:
        print(f"El texto es: {ingreso}")
        main()

# Leer archivo Json          --------------------------->      C H E C K
def readJson():
    print()

    #Recorrer archivos a cargar
    for x in range(1,len(instruccion)):

        #Verifica que no venga vacía la cadena
        if x == None:
            print("Error")
            main()

        #Archivos para cargar
        file = open(instruccion[x],'r')
        archivo = json.load(file)
        file.close

        #Ingresa la información a la base de datos
        global DB 
        DB.append(archivo)

        print(DB)
        print()

        pausar()

    clear()
    main()

# Comando SELECCIONAR        --------------------------->      C H E C K
def select():
    global item
    #Seleccionar todo
    if instruccion[1] == '*':
        print()
        print("-----------------------------------------------------------------------------------------------------")
        print()
        for i in range(0, len(DB)):
            
            for j in range(0,len(DB[i])):

               # print(DB[i][j])
                #pausar()
             
                print(f"Nombre: {DB[i][j]['nombre']}, edad: {DB[i][j]['edad']}, activo: {DB[i][j]['activo']}, promedio: {DB[i][j]['promedio']} ")
                print()
        print("-----------------------------------------------------------------------------------------------------")
        print()
    
    # Seleccionar campos específicos
    elif instruccion[1] != '*': # Verifica campo en específico
        for i in range(1,len(instruccion)):

            if instruccion[i].lower() == 'donde':
                #print("A L T O ")
                # ESCRIBIR CODIGO PARA DONDE
                global pivote

                pivote = i
               # pausar()
                Donde()
            
            elif instruccion[i].lower() == 'nombre':
                global sNombre
                sNombre = instruccion[i]
                item.append(sNombre)
               # print(sNombre)

            elif instruccion[i].lower() == 'edad':
                global sEdad
                sEdad = instruccion[i]
                item.append(sEdad)
                #print(sEdad)

            elif instruccion[i].lower() == 'promedio':
                global sProm
                sProm = instruccion[i]
                item.append(sProm)
                #print(sProm)

            elif instruccion[i].lower() == 'activo':
                global sActivo
                sActivo = instruccion[i]
                item.append(sActivo)
                #print(sActivo)
            

           


    pausar()
    main()

# comando DONDE              --------------------------->      C H E C K
def Donde():
   # print("Where ere e r e")
    global ruta, item
    global sNombre, sActivo, sEdad, sProm

    for i in range(pivote+1,len(instruccion)):
    #    print(instruccion[i])
        #Guarda instrucción de comando DONDE
        #ruta += ' '+instruccion[i]+' '
        ruta.append(instruccion[i])
    #pausar()
    #print(ruta)
    
    if ruta[0] != '':
       # print(ruta)
        
        # Elemento a buscar
        for t in range(2,len(ruta)):
            global temp
            temp +=ruta[t]+' '
        
        #print(f"temp: {temp}")
        #pausar()
        for i in range(0, len(DB)):
            for j in range(0,len(DB[i])):
               # print(ruta)
                #pausar()
                verificar = DB[i][j][ruta[0]]
                #print(verificar)
                #print("mama mia")
                #pausar()
                comodin = temp.replace('"','')

                if str(verificar) == comodin[:-1]:
                   # paso = "paso"
                    #main()
                #else:
                
                    #print(f"verificar verificado: {verificar}")
                    #pausar()

                    #Imprime los atributos seleccionados
                    #print(item)
                    print()
                    print("-----------------------------------------------------------------------------------------------------")
                    print()
                    for n in range(0,len(item)):
                        
                        if item[n].lower() == 'nombre':
                            print(f"Nombre: {DB[i][j]['nombre']}")
                        elif item[n].lower() == 'edad':
                            print(f"Edad: {DB[i][j]['edad']}")
                        elif item[n].lower() == 'promedio':
                            print(f"Promedio: {DB[i][j]['promedio']}")
                        elif item[n].lower() == 'activo':
                            print(f"Activo: {DB[i][j]['activo']}")
                        #print(n)
                    print()
                    print("-----------------------------------------------------------------------------------------------------")
                    print()
                    #pausar()
                
                #pausar()
            #pausar()
    else:
        print("Nombre vacío")

        


    #pausar()
    # Termina el comando DONDE, vacía la vriable 
    ruta = []
    sNombre = ''
    sEdad = ''
    sActivo = ''
    sProm = ''
    item = []
    

    temp = ''
    #print("cadenas vacías")
    pausar()
    main()

#Comando MAX - MIN           --------------------------->      C H E C K
def maxi():
   # print(f"Encontremos el maximo de {instruccion[1]} pue")
    #pausar()
    global outM, suma 
    for n in range(0, len(DB)):
       # print(f"Respuesta: {DB[n]}")
        #print("----------------------")

        for m in range(0, len(DB[n])):
            #print(f"Respuesta 2: {DB[n][m][instruccion[1]]}")

            # Ingresa todos los datos de instruccion[1] a una lista
            outM.append(DB[n][m][instruccion[1]])
            
           # print("-----------------")
    
   # print(outM)
    #Ordena ascendentemente la lista
    outM.sort()
    print()
    print("-----------------------------------------------------------------------------------------------------")
    print()
    if instruccion[0].lower() == 'maximo':
       
        print(f"{instruccion[1]}: {max(outM)}")
        
    elif instruccion[0].lower() == 'minimo':
        print(f"{instruccion[1]}: {min(outM)}")
        
    elif instruccion[0].lower() == 'suma':
        for i in outM:
            suma = suma + i
        print(f"La suma de {instruccion[1]} es: {suma}")
        suma = 0
        

    else:
        print("No se encontró registro")
       
    print()
    print("-----------------------------------------------------------------------------------------------------")
    print()

    #print(f"  {instruccion[1]} máxima: {max(outM)}")
    #print(f" Valor mínimo: {min(outM)}")
    outM = []
    pausar()
    main()

# comando CUENTA             --------------------------->      C H E C K
def count():
    global cantidad
    print()
    print("-----------------------------------------------------------------------------------------------------")
    print()
    for m in range(0, len(DB)):
        for n in range(0, len(DB[m])):
            cantidad.append(n)
            
    print(f"Se han realizado {len(cantidad)} registros en la base de datos ")
    print()
    print("-----------------------------------------------------------------------------------------------------")
    print()
    cantidad = []
    pausar()
    main()

#Comando REPORTAR            --------------------------->      C H E C K
def reporte():
    global pvReport, iNombre, conteo
    
    itm = instruccion[1]
    #print(m)
   # pausar()
    for n in range(0,len(DB)):
        
        for m in range(0,len(DB[n])):
            
            if (conteo <= int(itm)):    
                #print(DB[n][m])
                #print(conteo)
                
                # Genera las tablas del reporte:
                pvReport += f"""
                <tr>
                    <td>{DB[n][m]['nombre']}</td>
                    <td>{DB[n][m]['edad']}</td>
                    <td>{DB[n][m]['activo']}</td>
                    <td>{DB[n][m]['promedio']}</td>
                </tr>
                """
                conteo = conteo+1
    conteo = 1
                
        
    #pausar()
    
    # Genera el archivo HTML

    iNombre = iNombre+1 

    htmlCode = open(f'reporte{iNombre}.html','w')

    mensaje1 = """

    <!DOCTYPE html>
    <html>
        <head>
            <title>Reporte</title>
            <link rel=StyleSheet href="stylesheet.css" type="text/css" >
        </head>

        <body>
        <h1><span class="blue"></span>SIMPLE<span class="blue"></span><span class="yellow">QL</pan></h1>
        <h2>REPORTE DE REGISTROS EN BASE DE DATOS</h2>

            <table class="container">
                <thead>
                    <tr>
                        <th><h1>NOMBRE</h1></th>
                        <th><h1>EDAD</h1></th>
                        <th><h1>ACTIVO</h1></th>
                        <th><h1>SALDO</h1></th>
                    </tr>
                </thead>

                <tbody>
    """

    mensaje2 = """
        </tbody>
                </table>
        </body>
    </html>

    """

    escribir = mensaje1+pvReport+mensaje2

    htmlCode.write(escribir)
    htmlCode.close()

    #Genera el CSS del HTML

    estilo = open('stylesheet.css','w')
    code = """
    /*	
	Side Navigation Menu V2, RWD
	===================
	Author: @heyPablete

    */

    @charset "UTF-8";
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
    
    body {
    font-family: 'Open Sans', sans-serif;
    font-weight: 300;
    line-height: 1.42em;
    color:#A7A1AE;
    background-color:#1F2739;
    }
    
    h1 {
    font-size:3em; 
    font-weight: 300;
    line-height:1em;
    text-align: center;
    color: #4DC3FA;
    }
    
    h2 {
    font-size:1em; 
    font-weight: 300;
    text-align: center;
    display: block;
    line-height:1em;
    padding-bottom: 2em;
    color: #FB667A;
    }
    
    h2 a {
    font-weight: 700;
    text-transform: uppercase;
    color: #FB667A;
    text-decoration: none;
    }
    
    .blue { color: #185875; }
    .yellow { color: #FFF842; }
    
    .container th h1 {
        font-weight: bold;
        font-size: 1em;
    text-align: left;
    color: #185875;
    }
    
    .container td {
        font-weight: normal;
        font-size: 1em;
    -webkit-box-shadow: 0 2px 2px -2px #0E1119;
            -moz-box-shadow: 0 2px 2px -2px #0E1119;
                box-shadow: 0 2px 2px -2px #0E1119;
    }
    
    .container {
        text-align: left;
        overflow: hidden;
        width: 80%;
        margin: 0 auto;
    display: table;
    padding: 0 0 8em 0;
    }
    
    .container td, .container th {
        padding-bottom: 2%;
        padding-top: 2%;
    padding-left:2%;  
    }
    
    /* Background-color of the odd rows */
    .container tr:nth-child(odd) {
        background-color: #323C50;
    }
    
    /* Background-color of the even rows */
    .container tr:nth-child(even) {
        background-color: #2C3446;
    }
    
    .container th {
        background-color: #1F2739;
    }
    
    .container td:first-child { color: #FB667A; }
    
    .container tr:hover {
        background-color: #464A52;
    -webkit-box-shadow: 0 6px 6px -6px #0E1119;
            -moz-box-shadow: 0 6px 6px -6px #0E1119;
                box-shadow: 0 6px 6px -6px #0E1119;
    }
    
    .container td:hover {
    background-color: #FFF842;
    color: #403E10;
    font-weight: bold;
    
    box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
    transform: translate3d(6px, -6px, 0);
    
    transition-delay: 0s;
        transition-duration: 0.4s;
        transition-property: all;
    transition-timing-function: line;
    }
    
    @media (max-width: 800px) {
    .container td:nth-child(4),
    .container th:nth-child(4) { display: none; }
    }



    """

    estilo.write(code)
    estilo.close()
        
    webbrowser.open_new_tab(f'reporte{iNombre}.html')

    pausar()

    pvReport = ''
    
    main()

#Pausar ejecución
def pausar ():
    os.system('pause')

#Limpiar pantalla
def clear ():
    os.system('cls')

#Salir de la app
def exit ():
    print("¿Está seguro que desea salir del sistema?")

#Ejecutar app
main()

