from tkinter import *               #Tkinter 
import os                           #Nenecesario para usar el os.path.join 
import random                       #Generadador de numeros random
from tkinter import messagebox      #Caja de mensajes 
import pickle                       #Necesario para hacer el leaderboard
import winsound                     #Reproducir la cancion de fondo                         

#Globlanes 
global binario, octal, hexadecimal, decimal
global base

#Funcion para las bases numericas 
from Bases_numericas import dec_bin,octal_conv, hexa



##### Menú del juego ####
root = Tk()
root.minsize(600,550)
root.resizable(width=NO, height =NO)
root.title("PLAY 2048 PLUS")

Canvas_root = Canvas(root,width = 600,height=550,bg = "light yellow")
Canvas_root.place(x=0,y=0)

##### Funcion que carga imagenes #####
#Entradas: Nombre de la imagen
#Salidas: imagen
#Restricciones: Solamente se pueden ingresar strings
def cargarImg(nombre):
    ruta=os.path.join('img2',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

#### Cargar la imagen del fondo del menu###
fondoImg=cargarImg('Menu2.gif')
F_juego=Label(Canvas_root, bg='red')
F_juego.place(x=0,y=0)
F_juego.config(image=fondoImg)
F_juego.lower()



TituloLeaderboard = Label(text= "LEADERBOARD",font=('Arial',15),bg='white')
TituloLeaderboard.place(x=20,y=20)

Leaderboard = Label(text= "No hay datos que mostrar",font=('Arial',20),bg='white')
Leaderboard.place(x=20,y=70)

####LEADER BOARD###
def leaderboard():
    existe = os.path.isfile("Puntaje.txt")
    if (existe):
        Tabla= open("Puntaje.txt","rb")
        Tabla = pickle.load(Tabla)
        Leaderboard['text'] = str(Tabla['Jugador1']+" "+Tabla["Puntaje1"] + "\n" + Tabla['Jugador2']+" "+Tabla["Puntaje2"] + "\n" + Tabla['Jugador3']+" "+Tabla["Puntaje3"] + "\n" + Tabla['Jugador4']+" "+Tabla["Puntaje4"] +"\n" + Tabla['Jugador5']+" "+Tabla["Puntaje5"]) 
    else:
        return 

leaderboard()
    


#Funcion que carga la musica de fondo
def Song1():
    winsound.PlaySound('', winsound.SND_ASYNC)

Song1()

#Funcion que apaga la cancion de fondo 
def off():
    winsound.PlaySound( None, winsound.SND_ASYNC)


##### Informacion del jugador ####
NombreJugador = Entry(text="Ingrese su nombre",width=15,font=('Arial',20))
NombreJugador.place(x=350,y=250)

Nombrelabel = Label(text= "Ingrese su nombre",font=('Arial',20),bg='light blue')
Nombrelabel.place(x=350,y=200)



######  Ventana para seleccionar la base ######
def seleccionar_base():

    global base
    ### Ventana de la base ####
    root.withdraw()
    base = Toplevel()
    base.minsize(500,300)
    base.resizable(width=NO,height=NO)
  
    Canvas_base = Canvas(base,width=500,height=300,bg="light blue")
    Canvas_base.place(x=0,y=0)
    
    ### Funcion para cargar la imagen del fondo de la base###
    fondoImg=cargarImg('FondoBases.gif')
    F_base=Label(Canvas_base, image = fondoImg,bg='light yellow')
    F_base.place(x=-40,y=-100)
    F_base.photo = fondoImg
    F_base.lower()

    
    ### Label con informacion ####
    Label_bases = Label(Canvas_base,text="Seleccionar una base",font=("Arial",20),bg="white")
    Label_bases.place(x=125,y=50)


    #### Botones para selecionar la base ####
    Decimal = Button(Canvas_base,text="Decimal",font=("Arial",15),command=salir_base_decimal,bg="green",relief="sunken",borderwidth=5)
    Decimal.place(x=30,y=125)

    Octal = Button(Canvas_base,text="Octal",font=("Arial",15),command=salir_base_octal,bg="red",relief="sunken",borderwidth=5)
    Octal.place(x=140,y=125)

    Hexadecimal = Button(Canvas_base,text="Hexadecimal",font=("Arial",15),command=salir_base_hexadecimal,bg="orange",relief="sunken",borderwidth=5)
    Hexadecimal.place(x=240,y=125)

    Binario = Button(Canvas_base,text="Binario",font=("Arial",15),command=salir_base_binario,bg="blue",relief="sunken",borderwidth=5)
    Binario.place(x=400,y=125)


    #### Funcion y boton para volver al menú principal ####
    def volver_menu2():         
        base.destroy()
        root.deiconify()

    Back_button = Button(Canvas_base,text="Volver",font=("Arial",13),bg="tomato2",command=volver_menu2,relief="sunken",borderwidth=5)
    Back_button.place(x=30,y=225)



#####  Ventana del juego ####
def ventana_juego(Jugador):
    #Llamado de la funcion para muter la cancion
    off()
    
    #Pantalla del juego
    Juego = Toplevel()
    Juego.minsize(700,700)
    Juego.resizable(width=NO, height =NO)

    #Canvas del juego
    Canvas_juego = Canvas(Juego,width = 700,height=700,bg = "light yellow")
    Canvas_juego.place(x=0,y=0)

    #Cargar cuadrícula del juego
    fondoImg=cargarImg('Fondo.gif')
    F_juego=Label(Canvas_juego, image = fondoImg,bg='light yellow')
    F_juego.place(x=100,y=130)
    F_juego.photo = fondoImg
    F_juego.lower()

    #Label con la puntuacion y el tiempo de la partida
    Puntuacion = Label(Canvas_juego,text= "Puntuacion:",font=('Arial',20),bg="light yellow")
    Puntuacion.place(x=225,y=10)

    Tiempo = Label(Canvas_juego,text= "Tiempo:",font=('Arial',20),bg="light yellow")
    Tiempo.place(x=460,y=10)




    #Leaderbord

    def recorrer_puntajes(leaderboard,num,nombre):
        if (isinstance(num,int) and isinstance(nombre,str)):
            return recorrer_puntajes_aux(leaderboard,1,num,nombre)
        else:
            return "Datos invalidos"

    def recorrer_puntajes_aux(leaderboard,i,num,nombre):
        #print(len(leaderboard)-5)
        print(i)
        if (i < len(leaderboard)-6):  
            if (num >= int(leaderboard['Puntaje{}'.format(i)])):

                num2 = int(leaderboard['Puntaje{}'.format(i)])
                nombre2 = leaderboard['Jugador{}'.format(i)]

                leaderboard['Puntaje{}'.format(i)] = str(num)
                leaderboard['Jugador{}'.format(i)] = nombre

                num = num2
                nombre = nombre2
                return recorrer_puntajes_aux(leaderboard,i+1,num,nombre)
            else:
                return recorrer_puntajes_aux(leaderboard,i+1,num,nombre)
        else:
            return leaderboard


    def CargarArchivos():
        existe = os.path.isfile("Puntaje.txt")

        if (existe):
            file = open("Puntaje.txt","rb")
            memoria = pickle.load(file)
            file.close()
        else:
            file = open("Puntaje.txt", "wb+")
            memoria = {'Jugador1':"Sin nombre",'Puntaje1':"0",'Jugador2':"Sin nombre",'Puntaje2':"0",'Jugador3':"Sin nombre",'Puntaje3':"0",'Jugador4':"Sin nombre",'Puntaje4':"0",'Jugador5':"Sin nombre",'Puntaje5':"0"}
            pickle.dump(memoria,file)
            file.close()

        return memoria


    def guardarArchivo(memory):

        file = open("Puntaje.txt","wb")
        pickle.dump(memory,file)
        file.close()


    def crearDatos(Jugador,Puntaje):
        data = {}

        data["Jugador"] = Jugador
        data["Puntaje"] = Puntaje

        return data


    def AgregarDatos(memoria,NuevosDatos):
        
        nombre = NuevosDatos['Jugador']
        puntaje = int(NuevosDatos['Puntaje'])
        

        memoria = recorrer_puntajes(memoria,puntaje,nombre)
        guardarArchivo(memoria)

        return memoria 



            


    #Labels de la cuadricula
    Cuadro1 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro1.place(x=5,y=7)

    Cuadro2 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro2.place(x=130,y=7)

    Cuadro3 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro3.place(x=255,y=7)

    Cuadro4 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro4.place(x=380,y=7)

    Cuadro5 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro5.place(x=5,y=130)

    Cuadro6 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro6.place(x=130,y=130)

    Cuadro7 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro7.place(x=255,y=130)

    Cuadro8 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro8.place(x=380,y=130)

    Cuadro9 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro9.place(x=5,y=255)

    Cuadro10 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro10.place(x=130,y=255)

    Cuadro11 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro11.place(x=255,y=255)

    Cuadro12 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro12.place(x=380,y=255)

    Cuadro13 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro13.place(x=5,y=380)

    Cuadro14 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro14.place(x=130,y=380)

    Cuadro15 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro15.place(x=255,y=380)

    Cuadro16 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20),bg="navajo white3")
    Cuadro16.place(x=380,y=380)
    

    #Matriz principal y global del puntaje 
    global matriz_main,Puntaje
    matriz_main =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    Puntaje =0

    #Puntaje del juego (Label y función que lo actualiza)
    Score = Label(Canvas_juego,text= "0",font=('Arial',30),bg="white",width =6)
    Score.place(x=225,y=50)


    #Entradas: Numero correspondiente a la suma de todos los movimientos
    #Salidas: El numero convertido según la base elegida
    #Restricciones: Solamente se puede ingresar numero 
    def score(X):
        global Puntaje 
        Puntaje += X
        if (isinstance(X,int)):
            if (binario):
                New_score = dec_bin(Puntaje)
                Score['text'] = str(Puntaje)
            if (octal):
                New_score = octal_conv(Puntaje)
                Score['text'] = str(Puntaje)
            if (hexadecimal):
                New_score= hexa(Puntaje)
                Score['text'] = Puntaje
            if (decimal):
                Score['text'] = str(Puntaje)
        else:
            return "Solamente puede ser enteros"
            
            
    #Funcion para actualizar la pantalla de juego
    #Entradas: Un numero entero
    #Salidas: El numero convertido según la base elegida
    #Restricciones: Solamente pueden ser enteros 
    def convertir(numero):
        if (binario):
            numero = dec_bin(numero)
            return numero
        if (octal):
            numero = octal_conv(numero)
            return numero
        if (hexadecimal):
            numero = hexa(numero)
            return numero
        if (decimal):
            return numero 

    #Entradas: i = 0 y j = 0 correspodientes a los indices de la matriz
    #Salidas: Pantalla del juego actualizada dependiendo de los movimientos de la matriz_main
    #Restricciones: Los parámetros solamente pueden ser 0     
    def update_screen(i,j):
        if (i < 4):
            if (j <4):
                if (matriz_main[i][j] == 0):
                    matriz2[i][j]['text'] = ""
                    matriz2[i][j]['bg'] = "navajo white3"
                    return update_screen(i,j+1)
                else:
                    if (matriz_main[i][j] == 4):
                        numero=  convertir(matriz_main[i][j])
                        matriz2[i][j]['text'] = str(numero)
                        matriz2[i][j]['bg'] = "Antique white3"
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] == 8 or matriz_main[i][j] == 16):
                        numero = convertir(matriz_main[i][j])
                        matriz2[i][j]['text'] = str(numero)
                        matriz2[i][j]['bg'] = "orange"
                        return update_screen(i,j+1)  
                    if (matriz_main[i][j] == 32):
                        numero = convertir(matriz_main[i][j])
                        matriz2[i][j]['text'] = str(numero)
                        matriz2[i][j]['bg'] = "dark orange"
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] == 64 ):
                        numero = convertir(matriz_main[i][j])
                        matriz2[i][j]['text'] = str(numero)
                        matriz2[i][j]['bg'] = "red"
                        return update_screen(i,j+1)
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] >=128 ):
                        numero = convertir(matriz_main[i][j])
                        matriz2[i][j]['text'] = str(numero)
                        matriz2[i][j]['bg'] = "yellow"
                        return update_screen(i,j+1)
                    else:
                        numero= convertir(matriz_main[i][j])
                        matriz2[i][j]['text'] = str(numero)
                        matriz2[i][j]['bg'] = 'linen'
                        return update_screen(i,j+1)
            else:
                return update_screen(i+1,0)
        else:
            return matriz_main



    #Funcion que introduce un nuevo numero en cada movimiento
    #Entradas: Ninguna
    #Salidas: Introducir a la matriz_main un numero aleatorio en una posicion aleatoria
    #Restricciones: No se deben ingresar parámetros
    def fill_screen():
        numero_aleatorio = random.randrange(2,5,2)
        indices = espacios_vacios()
        aleatorio = random.randint(0,len(indices)-1)
        temp = indices[aleatorio]
        matriz_main[temp[0]][temp[1]] += numero_aleatorio
        
        update_screen(0,0)
        


    #Matriz donde se encuentra las cada uno de los labels de la pantalla mostrada al usuario
    matriz2= [[Cuadro1,Cuadro2,Cuadro3,Cuadro4],
             [Cuadro5,Cuadro6,Cuadro7,Cuadro8],
             [Cuadro9,Cuadro10,Cuadro11,Cuadro12],
             [Cuadro13,Cuadro14,Cuadro15,Cuadro16]]


    
    #Funcion booleana que indica si existen movimientos posibles
    #Entradas: Nunguna
    #Salidas: True en caso de que exista al menos un movimento posible, False en caso contrario
    #Restricciones: No se deben ingresar parámetros
    def opciones():
        return opciones_aux(0,0)

    def opciones_aux(i,j):
        if (i<=3):
                if (j<=3):
                    #Cao en haya un 0 dentro de la matriz
                    if (matriz_main[i][j] == 0):
                        return True
                    #Esquina 1
                    elif (i==0 and j==0):
                        if (matriz_main[i][j] == matriz_main[i+1][j] or matriz_main[i][j] == matriz_main[i][j+1]):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Esquina 2
                    elif (i==0 and j==3):
                        if (matriz_main[i][j] == matriz_main[i+1][j] or matriz_main[i][j] == matriz_main[i][j-1]):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Esquina 3
                    elif (i==3 and j==0):
                        if ((matriz_main[i][j] == matriz_main[i-1][j]) or (matriz_main[i][j] == matriz_main[i][j+1])):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Esquina 4 
                    elif (i==3 and j==3):
                        if (matriz_main[i][j] == matriz_main[i-1][j] or matriz_main[i][j] == matriz_main[i][j-1]):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Costado izquierda
                    elif ((i==1 or i==2) and (j==0)):
                        if (matriz_main[i][j] == matriz_main[i][j+1] or matriz_main[i][j] == matriz_main[i-1][j] or matriz_main[i][j] == matriz_main[i+1][j]):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Costado arriba
                    elif ((i==0) and (j==1 or j==2)):
                        if ((matriz_main[i][j] == matriz_main[i+1][j]) or (matriz_main[i][j] == matriz_main[i][j+1]) or (matriz_main[i][j] == matriz_main[i][j-1])):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Costado derecha
                    elif ((i==1 or i==2) and (j==3)):
                        if (matriz_main[i][j] == matriz_main[i+1][j] or matriz_main[i][j] == matriz_main[i-1][j] or matriz_main[i][j] == matriz_main[i][j-1]):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Costado abajo
                    elif ((i==3) and (j==1 or j==2)):
                        if (matriz_main[i][j] == matriz_main[i-1][j] or matriz_main[i][j] == matriz_main[i][j+1] or matriz_main[i][j] == matriz_main[i][j-1]):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                    #Centro
                    elif ((i==1 or i==2) and (j==1 or j==2)):
                        if ((matriz_main[i][j] == matriz_main[i+1][j]) or (matriz_main[i][j] == matriz_main[i-1][j]) or (matriz_main[i][j] ==matriz_main[i][j+1]) or (matriz_main[i][j] == matriz_main[i][j-1])):
                            return True
                        else:
                            return opciones_aux(i,j+1)
                
                else:
                        return opciones_aux(i+1,0)
        else:
                return False

    #Funcion booleana que indica si existe un elemeto de la matriz_main con 2048
    #Entradas: Ninguna
    #Salidas: True en caso de que un elemento de la matriz_main sea 2048, False en caso contrario
    #Restricciones: No se ingresar parámetros        
    
    def FichaMayor():
        return FichaMayor_aux(0,0)

    def FichaMayor_aux(i,j):
        if (i<4):
            if (j<4):
                if (matriz_main[i][j]==2048):
                    return True
                else:
                    return FichaMayor_aux(i,j+1)
            else:
                return FichaMayor_aux(i+1,0)
        else:
            return False 


    #Funcion booleana que permite o no seguir jugando hacia una direccion
    #Entradas: Una sublista de la matriz
    #Salidas: True en caso de que exista al menos una opcion de juego hacia esa direccion
    #Restricciones: Solamente una sublista de la matriz 
    def opciones_direccion(matriz):
        return opciones_direccion_aux(matriz,0)

    def opciones_direccion_aux(matriz,i):
        if (matriz[0]!=0 and matriz[1]==0 and matriz[2]==0 and matriz[3]==0):
            return False
        if (matriz[0]==0 and matriz[1]==0 and matriz[2]==0 and matriz[3]!=0):
            return True 
        else:
            if (cantidad_ceros(matriz)==4):
                return False
            matriz2 = quitar_ceros(matriz)
            if (encontrar_ceros(matriz2)):
                return True
            else:
                matriz = combinar(matriz,0)
                return verificar(matriz)

    #Funcion booleana que verifia si existen numeros que se pueden sumar
    #Entradas: Una sublista de la matriz
    #Salidas: True en caso de que los numeros sean iguales, False en caso de que la longitud de la lista sea 1
    #Restricciones: Solamente una sublista de la matriz
    def verificar(matriz):
        if (len(matriz)==1):
            return False
        elif (matriz[0] == matriz[1]):
            return True
        else:
            return verificar(matriz[1:])
            
    #Funcion que retorna True O False en caso de que encuntre un 0 en medio
    #Entradas: Una sublista de la matriz
    #Salidas: True en caso de que encuentre un 0, False en caso contrario
    #Restricciones: Solamente una sublista de la matriz
    def encontrar_ceros(matriz):
        if (matriz==[]):
            return False
        elif (matriz[0] == 0):
            return True
        else:
            return encontrar_ceros(matriz[1:])

    #Funcion que retorna la cantidad de ceros que encontró
    #Entradas: Una sublista de la matriz
    #Salidas: Cantidad de ceros
    #Restricciones: Solamente una sublista de la matriz
    def cantidad_ceros(matriz):
        if (matriz == []):
            return 0
        elif (matriz[0] == 0):
            return 1 + cantidad_ceros(matriz[1:])
        else:
            return cantidad_ceros(matriz[1:])

    #Funcion que elimina los ultimos ceros de la lista
    #Entradas: Una sublista de la matriz
    #Salidas: La sublista sin los ultimos ceros 
    #Restricciones: Solamente una sublista de la matriz
    def quitar_ceros(matriz):
        if (matriz[-1] != 0):
            return matriz
        else:
            return quitar_ceros(matriz[:-1])

    #Funcion que retorna una lista con sublistas de las indices de las posiciones vacias
    #Entradas: Ninguna
    #Salidas: Una lista con sunlistas de los indices de las posiciones vacias de la matriz_main
    #Restricciones: No se deben ingresar parámetros
    def espacios_vacios():
        return espacios_vacios_aux(0,0)

    def espacios_vacios_aux(i,j):
        if (i<4):
            if (j < 4):
                if (matriz_main[i][j] == 0):
                    return [[i,j]] + espacios_vacios_aux(i,j+1)
                else:
                    return espacios_vacios_aux(i,j+1)
            else:
                return espacios_vacios_aux(i+1,0)
        else:
            return []


    #Funcion que suma y combinar las listas de derecha a izquierda (arriba,abajo)
    #Entradas: Una sublista de la matriz convertida y un indice 
    #Salidas: Solamente los numeros diferente a 0 integrados en una lista
    #Restricciones: El indice debe ser solamente 0
    def combinar(matriz,i):
        if (i != 4):
            if (matriz[i] != 0):
                return [matriz[i]] + combinar(matriz,i+1)
            else:
                return combinar(matriz,i+1)
        else:
            return []

        
    #Entradas: Una sublista de la matriz convertida, la longitud de la sublista y la meta
    #Salidas: Una lista rellenada con los 0 faltantes para que su longitud sea 3
    #Restricciones: La meta siempre debe ser 3
    def rellenar(matriz,longitud,meta):
       if (longitud != meta):
           matriz +=[0]
           return rellenar(matriz,longitud+1,meta)
       else:
           return matriz

    #Entradas: Una sublista de la matriz convertida y un indice
    #Salidas: Una lista con la suma de los numeros segun las reglas del juego
    #Restricciones: El indice siempre debe ser 0
    def sumar(matriz,i):
        if (i<=2):
            if (matriz[i] == matriz[i+1]):
                matriz[i] += matriz[i+1]
                score(matriz[i])
                matriz[i+1] = 0
                return sumar(matriz,i+1)
            else:
                return sumar(matriz,i+1)
        else:
            return matriz


    """Arriba"""
    #Funcion que convierte la matriz para sumar hacia arriba
    #Entradas: Una matriz 4x4
    #Salidas: Una matriz convertida
    #Restricciones: Solamente se puede ingresar una matriz 4x4
    def convertir_arriba(matriz):
        matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return convertir_arriba_aux(matriz,0,0,matriz2)

    def convertir_arriba_aux(matriz,i,j,matriz2):
        if (i<4):
            if (j<4):
                matriz2[j][i] = matriz[i][j]
                return convertir_arriba_aux(matriz,i,j+1,matriz2)
            else:
                return convertir_arriba_aux(matriz,i+1,0,matriz2)
        else:
            return matriz2


    ### Funcion que desconvierte la matriz a la original ###
    #Entradas: Una matriz 4x4
    #Salidas: Una matriz desconvertida a la original 
    #Restricciones: Solamente se puede ingresar una matriz 4x4
    def desconvertir_arriba(matriz):
        matriz2 = matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return desconvertir_arriba_aux(matriz,0,0,matriz2)

    def desconvertir_arriba_aux(matriz,i,j,matriz2):
        if (i<4):
            if (j<4):
                matriz2[i][j] = matriz[j][i]
                return desconvertir_arriba_aux(matriz,i,j+1,matriz2)
            else:
                return desconvertir_arriba_aux(matriz,i+1,0,matriz2)
        else:
            return matriz2


        

    #### Funcion que convierte la matriz de la derecha####
    #Entradas: Una matriz 4x4
    #Salidas: Una matriz convertida
    #Restricciones: Solamente se puede ingresar una matriz 4x4
    def convertir_derecha(matriz):
        matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return convertir_derecha_aux(matriz,0,3,matriz2)


    def convertir_derecha_aux(matriz,i,j,matriz2):
        if (i<4):
            if (j>=0):
                matriz2[i][3-j] += matriz[i][j]
                return convertir_derecha_aux(matriz,i,j-1,matriz2)
            else:
                return convertir_derecha_aux(matriz,i+1,3,matriz2)
        else:
            return matriz2

    ###Funcion que desconvierte la matriz a la original a la derecha###
    #Entradas: Una matriz 4x4
    #Salidas: Una matriz desconvertida a la original 
    #Restricciones: Solamente se puede ingresar una matriz 4x4
    def desconvertir_derecha(matriz):
        matriz2 = matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return desconvertir_derecha_aux(matriz,0,3,matriz2)

    def desconvertir_derecha_aux(matriz,i,j,matriz2):
        if (i<4):
            if (j>=0):
                matriz2[i][j] += matriz[i][3-j] 
                return desconvertir_derecha_aux(matriz,i,j-1,matriz2)
            else:
                return desconvertir_derecha_aux(matriz,i+1,3,matriz2)
        else:
            return matriz2



        
    ####Funcion que convierte la matriz de abajo###
    #Entradas: Una matriz 4x4
    #Salidas: Una matriz convertida
    #Restricciones: Solamente se puede ingresar una matriz 4x4
    def convertir_abajo(matriz):
        matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return convertir_abajo_aux(matriz,3,3,matriz2)

    def convertir_abajo_aux(matriz,i,j,matriz2):
        if (j>=0):
            if (i>=0):
                matriz2[3-j][3-i] += matriz[i][j]
                return convertir_abajo_aux(matriz,i-1,j,matriz2)
            else:
                return convertir_abajo_aux(matriz,3,j-1,matriz2)
        else:
            return matriz2
        

                            
    ###Funcion que desconvierte la matriz a la original a la derecha###
    #Entradas: Una matriz 4x4
    #Salidas: Una matriz desconvertida a la original 
    #Restricciones: Solamente se puede ingresar una matriz 4x4
    def desconvertir_abajo(matriz):
        matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return convertir_abajo_aux(matriz,3,3,matriz2)

    def desconvertir_abajo_aux(matriz,i,j,matriz2):
        if (j>=0):
            if (i>=0):
                matriz2[i][j] += matriz[3-j][3-i]
                return desconvertir_abajo_aux(matriz,i-1,j,matriz2)
            else:
                return desconvertir_abajo_aux(matriz,3,j-1,matriz2)
        else:
            return matriz2


    Tiempo = Label(Canvas_juego,text="",font=("Arial",30),bg="white",width=5)
    Tiempo.place(x=450,y=50)

    global minutos,segundos
    minutos = 0
    segundos = 0

    def tiempo():
        global minutos
        if (minutos==5):
            memoria = CargarArchivos()
            NuevosDatos = crearDatos(Jugador,str(Puntaje))
            Puntajes = AgregarDatos(memoria,NuevosDatos)
            Mensaje = messagebox.showinfo("","Se te agotó el tiempo, tu puntaje es de {}".format(str(Puntaje)))
            Juego.destroy()
            return root.deiconify()
   
        else:
            return

    #FUNCION DE TIEMPO
    def reloj():
        global minutos,segundos
        if (minutos < 5):
            if (segundos <=58):
                segundos +=1
                tiempo()
                Tiempo['text'] = str(minutos) +":" + str(segundos)
                Tiempo.after(1000,reloj)
            else:
                minutos += 1
                segundos = 0
                tiempo()
                Tiempo['text'] = str(minutos) +":" + str(segundos)
                Tiempo.after(1000,reloj)
        else:
            return False 


    #Funcion para empezar el juego
    def empezar_juego():
        pos1 = random.randint(0,3)
        pos2 = random.randint(0,3)

        pos3 = random.randint(0,3)
        pos4 = random.randint(0,3)

        if ((pos1 == pos3) and (pos2 == pos4)):
            return empezar_juego()
        else:
            aleatorio1 = random.randrange(2,5,2)

            matriz_main[pos1][pos2] = 2
            matriz_main[pos3][pos4] = aleatorio1

            reloj()

            update_screen(0,0)


    def condiciones_ganar_perder():
        global minutos, Puntaje
        if (FichaMayor()):
            memoria = CargarArchivos()
            NuevosDatos = crearDatos(Jugador,str(Puntaje))
            Puntajes = AgregarDatos(memoria,NuevosDatos)
            print(Puntajes)
            Mensaje = messagebox.showinfo("","Felicidades Ganaste")
            volver_menu()
        if not (opciones()):
            memoria = CargarArchivos()
            NuevosDatos = crearDatos(Jugador,str(Puntaje))
            Puntajes = AgregarDatos(memoria,NuevosDatos)
            print(Puntajes)
            Mensaje = messagebox.showinfo("","Tu puntaje es de {}".format(str(Puntaje)))
            volver_menu()
        else:
            return False




    ### FUNCION QUE REALIZA LOS MOVIMIENTOS, SUMA SEGUN LAS REGLAS DEL JUEGO ###
    #Entradas: Una sublista de la matriz convertida y un indice
    #Salidas: Una lista con los movimientos y suma segun la reglas del jueg
    #Restricciones: El indice debe ser siempre 0 
    def movimientos(matriz,i):
        combinar1 = combinar(matriz,i)
        rellenar1 = rellenar(combinar1,len(combinar1)-1,3)
        suma = sumar(rellenar1,0)
        combinar2 = combinar(suma,0)
        return rellenar(combinar2,len(combinar2)-1,3)


    

    def new_number_arriba(event):
        global matriz_main,Puntaje,minutos 
        
        nueva_matriz = convertir_arriba(matriz_main)
        Opciones = opciones_direccion(nueva_matriz[0]) or opciones_direccion(nueva_matriz[1]) or opciones_direccion(nueva_matriz[2]) or opciones_direccion(nueva_matriz[3])

        
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)

  
        if (condiciones_ganar_perder()):
            pass
        elif (Opciones == True):
            nueva_matriz[0] = movimientos(nueva_matriz[0],0)
            nueva_matriz[1] = movimientos(nueva_matriz[1],0)
            nueva_matriz[2] = movimientos(nueva_matriz[2],0)
            nueva_matriz[3] = movimientos(nueva_matriz[3],0)
            matriz_main = desconvertir_arriba(nueva_matriz)
            
            fill_screen()
            update_screen(0,0)

        else:
            return 
             
    Juego.bind("<Up>",new_number_arriba)



    def new_number_abajo(event):
        global matriz_main,Puntaje, minutos 
        
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)

        nueva_matriz = convertir_abajo(matriz_main)
        Opciones = opciones_direccion(nueva_matriz[0]) or opciones_direccion(nueva_matriz[1]) or opciones_direccion(nueva_matriz[2]) or opciones_direccion(nueva_matriz[3])


    
        if (condiciones_ganar_perder()):
            pass
        elif (Opciones):
            #Utiliza convertir_arriba porque mas adelante utiliza combina_right 
            nueva_matriz[0] = movimientos(nueva_matriz[0],0)
            nueva_matriz[1] = movimientos(nueva_matriz[1],0)
            nueva_matriz[2] = movimientos(nueva_matriz[2],0)
            nueva_matriz[3] = movimientos(nueva_matriz[3],0)
            matriz_main = desconvertir_abajo(nueva_matriz)

            fill_screen()
    
            update_screen(0,0)
        else:
            return 
         
                    
    Juego.bind("<Down>",new_number_abajo)

    def new_number_izquierda(event):
        global Puntaje 
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)

        Opciones = opciones_direccion(matriz_main[0]) or opciones_direccion(matriz_main[1]) or opciones_direccion(matriz_main[2]) or opciones_direccion(matriz_main[3])


      
        if (condiciones_ganar_perder()):
            pass
        elif (Opciones):
            matriz_main[0] = movimientos(matriz_main[0],0)
            matriz_main[1] = movimientos(matriz_main[1],0)
            matriz_main[2] = movimientos(matriz_main[2],0)
            matriz_main[3] = movimientos(matriz_main[3],0)


            fill_screen()

            update_screen(0,0)
        else:
            return 
            

    Juego.bind("<Left>",new_number_izquierda)            

    def new_number_derecha(event):
        global matriz_main,Puntaje
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)
        matriz = convertir_derecha(matriz_main)
        Opciones = opciones_direccion(matriz[0]) or opciones_direccion(matriz[1]) or opciones_direccion(matriz[2]) or opciones_direccion(matriz[3])

        if (condiciones_ganar_perder()):
            pass
        elif (Opciones):
            matriz[0] = movimientos(matriz[0],0)
            matriz[1] = movimientos(matriz[1],0)
            matriz[2] = movimientos(matriz[2],0)
            matriz[3] = movimientos(matriz[3],0)
            matriz_main = desconvertir_derecha(matriz)
   
            fill_screen()

            update_screen(0,0)
        else:
            return 

    Juego.bind("<Right>",new_number_derecha)





#Funcion y boton para volver al menu principal
    def volver_menu():         
        Juego.destroy()
        leaderboard()
        root.deiconify()

    Volver = Button(Canvas_juego,text = "Volver",font =("Arial",15),width=10,command=volver_menu,bg="red",fg="white",relief='groove',borderwidth=5)
    Volver.place(x=10,y=30)

    Empezar = Button(Canvas_juego,text = "Empezar",font =("Arial",15),width=10,command=empezar_juego,bg="red",fg="white",relief='groove',borderwidth=5)
    Empezar.place(x=10,y=80)

   



#Funcion que registra el nombre del jugador e inicia la pantalla de juego 
def empezar():
    global base
    base.destroy()
    Jugador = str(NombreJugador.get())
    ventana_juego(Jugador)


##########FUNCIONES PARA SELECCIONAR LA BASE
def salir_base_binario():
    global binario,octal,hexadecimal,decimal
    binario=True
    octal = False
    hexadecimal= False
    decimal = False
    empezae()

def salir_base_octal():
    global binario,octal,hexadecimal,decimal
    binario =False
    octal = True
    hexadecimal= False
    decimal = False 
    empezar()

def salir_base_hexadecimal():
    global binario,octal,hexadecimal,decimal
    binario = False
    octal = False
    hexadecimal= True
    decimal = False 
    empezar()

def salir_base_decimal():
    global binario,octal,hexadecimal,decimal
    binario =False
    octal=False
    hexadecimal=False
    decimal = True  
    empezar()



#Boton de play
botonJuego = Button(Canvas_root,text="Play",font=('Arial',15),width=5,command=seleccionar_base,relief="sunken",borderwidth=5,bg="red")
botonJuego.place(x=420,y=300)

Mute = Button(Canvas_root,text="Mute",font=('Arial',15),width=5,command=off,relief="sunken",borderwidth=5,bg="red")
Mute.place(x=420,y=350)


root.mainloop




















    
