#Librerias
import os
import json

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

temp = ''
ruta = []
suma = 0
cantidad = []

#Salida MAX - MIN
outM = []

#Items para where
item = []


# Función principal
def main():
    clear()
    
    print("--------------------")
    print("  S I M P L E Q L ")
    print("--------------------")

    print()


    print("Ingrese un comando: \n")

    #Quita las comas
    ingreso = input().replace(",","")

    #print(ingreso)

    #Separar por posiciones
    ingreso = ingreso.split()
    #print(ingreso.replace(',',''))

    global instruccion

    instruccion = ingreso

    

    #print(f"El comando es:, {ingreso[0]} "  )

    #Comando CARGAR
    if ingreso[0] == "cargar":
        
       #Llama a la función para cargar archivos '.JSON' 
       readJson()

       
    elif ingreso[0] == "seleccionar":
        select()

    elif ingreso[0] == "maximo":
        #print("Maximo")
        maxi()

    elif ingreso[0] == "minimo":
        #print("Minimo")
        maxi()

    elif ingreso[0] == "suma":
        #print("Suma")
        maxi()

    elif ingreso[0] == "cuenta":
        #print("Cuenta")
        count()

    elif ingreso[0] == "reportar":
        print("Reportar")
    
    else:
        print(f"El texto es: {ingreso}")
        main()









# Leer archivo Json          --------------------------->      C H E C K
def readJson():
    print()
    
   # archivo = instruccion

    
    
    #Recorrer archivos a cargar

    for x in range(1,len(instruccion)):

        #Verifica que no venga vacía la cadena
        if x == None:
            #pausar()
            print("Error")
            #pausar()
            main()

        #Archivos para cargar
       # print(f"Se cargará el archivo {instruccion[x]}" )
       # pausar()

        file = open(instruccion[x],'r')
        #print(file.read())
        #pausar()
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
        for i in range(0, len(DB)):
            print()
            print("-----------------------------------------------------------------------------------------------------")
            print()
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

            if instruccion[i] == 'donde':
                #print("A L T O ")
                # ESCRIBIR CODIGO PARA DONDE
                global pivote

                pivote = i
               # pausar()
                Donde()
            
            elif instruccion[i] == 'nombre':
                global sNombre
                sNombre = instruccion[i]
                item.append(sNombre)
               # print(sNombre)

            elif instruccion[i] == 'edad':
                global sEdad
                sEdad = instruccion[i]
                item.append(sEdad)
                #print(sEdad)

            elif instruccion[i] == 'promedio':
                global sProm
                sProm = instruccion[i]
                item.append(sProm)
                #print(sProm)

            elif instruccion[i] == 'activo':
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
                        
                        if item[n] == 'nombre':
                            print(f"Nombre: {DB[i][j]['nombre']}")
                        elif item[n] == 'edad':
                            print(f"Edad: {DB[i][j]['edad']}")
                        elif item[n] == 'promedio':
                            print(f"Promedio: {DB[i][j]['promedio']}")
                        elif item[n] == 'activo':
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
    if instruccion[0] == 'maximo':
       
        print(f"{instruccion[1]}: {max(outM)}")
        
    elif instruccion[0] == 'minimo':
        print(f"{instruccion[1]}: {min(outM)}")
        
    elif instruccion[0] == 'suma':
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

