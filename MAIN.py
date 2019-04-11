from tkinter import *
import os
import random


#Ventana principal
root = Tk()
root.minsize(600,550)
root.resizable(width=NO, height =NO)
root.title("PLAY 2048 PLUS")


C_root = Canvas(root,width = 600,height=550,bg = "light yellow")
C_root.place(x=0,y=0)


#Funcion que carga imagenes
def cargarImg(nombre):
    ruta=os.path.join('img2',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

fondoImg=cargarImg('Menu2.gif')
F_juego=Label(C_root, bg='red')
F_juego.place(x=0,y=0)
F_juego.config(image=fondoImg)
F_juego.lower()


#Informacion del jugador 
NombreJugador = Entry(text="Ingrese su nombre",width=15,font=('Arial',20))
NombreJugador.place(x=350,y=250)

Nombrelabel = Label(text= "Ingrese su nombre",font=('Arial',20),bg='light blue')
Nombrelabel.place(x=350,y=200)


#           ____________________
#__________/ Ventana del juego
def ventana_juego():
    root.withdraw()

    #Pantalla del juego
    Juego = Toplevel()
    Juego.minsize(700,700)
    Juego.resizable(width=NO, height =NO)

    #Canvas del juego
    C_juego = Canvas(Juego,width = 700,height=700,bg = "light yellow")
    C_juego.place(x=0,y=0)

    #Cargar cuadrícula del juego
    fondoImg=cargarImg('Fondo.gif')
    F_juego=Label(C_juego, image = fondoImg,bg='light yellow')
    F_juego.place(x=100,y=130)
    F_juego.photo = fondoImg
    F_juego.lower()

    #Texto de puntuacion
    Puntuacion = Label(C_juego,text= "Puntuacion:",font=('Arial',30),bg="light yellow")
    Puntuacion.place(x=200,y=50)
                    

    #Labels de la cuadricula

    Cuadro1 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro1.place(x=5,y=7)

    Cuadro2 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro2.place(x=130,y=7)

    Cuadro3 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro3.place(x=255,y=7)

    Cuadro4 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro4.place(x=380,y=7)

    Cuadro5 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro5.place(x=5,y=130)

    Cuadro6 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro6.place(x=130,y=130)

    Cuadro7 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro7.place(x=255,y=130)

    Cuadro8 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro8.place(x=380,y=130)

    Cuadro9 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro9.place(x=5,y=255)

    Cuadro10 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro10.place(x=130,y=255)

    Cuadro11 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro11.place(x=255,y=255)

    Cuadro12 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro12.place(x=380,y=255)

    Cuadro13 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro13.place(x=5,y=380)

    Cuadro14 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro14.place(x=130,y=380)

    Cuadro15 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro15.place(x=255,y=380)

    Cuadro16 = Label(F_juego,text="",width=6,height=3,font=("Arial Black",20))
    Cuadro16.place(x=380,y=380)

    #Matriz principal
    global matriz_main
    matriz_main =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]



    #Funcion para actualizar la pantalla de juego 

    def update_label(X,num):
        if (num==0):
            X['text'] = ""
        else:
            X['text'] = str(num)

    #Funcion que introduce un nuevo numero en cada movimiento
    def fill_screen(matriz):
        numero_aleatorio = random.randrange(2,5,2)
        indices = espacios_vacios(matriz)
        aleatorio = random.randint(0,len(indices)-1)
        temp = indices[aleatorio]
        matriz_main[temp[0]][temp[1]] = numero_aleatorio
        
        update_label(matriz2[temp[0]][temp[1]],numero_aleatorio)


    #Matriz donde se encuentra las cada uno de los labels de la pantalla mostrada al usuario
    matriz2= [[Cuadro1,Cuadro2,Cuadro3,Cuadro4],
             [Cuadro5,Cuadro6,Cuadro7,Cuadro8],
             [Cuadro9,Cuadro10,Cuadro11,Cuadro12],
             [Cuadro13,Cuadro14,Cuadro15,Cuadro16]]


    #Funcion espacios vacios de la matriz
    def espacio_cantidad(matriz):
        return espacio_aux(matriz,0,0)

    def espacio_aux(matriz,i,j):
        if (i < 4):
            if (j < 4):
                if (matriz[i][j] == 0):
                    return 1 + espacio_aux(matriz,i,j+1)
                else:
                    return espacio_aux(matriz,i,j+1)
            else:
                return espacio_aux(matriz,i+1,0)
        else:
            return 0


    #Funcion con los indices de los espacios vacios de la matriz principal 
    def espacios_vacios(matriz):
        return espacios_vacios_aux(matriz,0,0)

    def espacios_vacios_aux(matriz,i,j):
        if (i<4):
            if (j < 4):
                if (matriz[i][j] == 0):
                    return [[i,j]] + espacios_vacios_aux(matriz,i,j+1)
                else:
                    return espacios_vacios_aux(matriz,i,j+1)
            else:
                return espacios_vacios_aux(matriz,i+1,0)
        else:
            return []


    #Funcion booleana para espacio vacios
    """
    def espacios_vacios(matriz,x,y):
        return espacios_vacios_aux(matriz,0,0,x,y)

    def espacios_vacios_aux(matriz,i,j,x):
        if (i<4):
            if (j < 4):
                if (matriz[i][j] == 0 and x==i and y==j):
                    return True 
                else:
                    return espacios_vacios_aux(matriz,i,j+1,x,y)
            else:
                return espacios_vacios_aux(matriz,i+1,0,x,y)
        else:
            return False

    """
    #Funcion que actualiza los espacios vacios

    def update_empty(matriz):
        return espacios_vacios(matriz)
                    


    """Lista"""
    #Funcion para empezar el juego
    def empezar_juego():
        
        #Posicion para colocar el primer numero al inicio del juego
        pos1 = random.randint(0,3)
        pos2 = random.randint(0,3)

        #Posicion para colocar el segundo numeor al inicio del juego
        pos3 = random.randint(0,3)
        pos4 = random.randint(0,3)

        #Numero aleatorio para colocar al inicio del juego
        aleatorio1 = random.randrange(2,5,2)

        #Actualizar la pantalla del juego
        update_label(matriz2[pos1][pos2],2)
        update_label(matriz2[pos3][pos4],aleatorio1)
        
        #Actualizar la matriz principal
        matriz_main[pos1][pos2] = 2
        matriz_main[pos3][pos4] = aleatorio1

       

        
        



    def arriba(matriz,sub,sub2):
        if (sub <=2):
            if (matriz[sub][sub2]  == matriz[sub+1][sub2]):
                
                matriz[sub][sub2] += matriz[sub+1][sub2]
                temp2 = matriz[sub][sub2] + matriz[sub+1][sub2]
                update_label(matriz2[sub][sub2],temp2)


                             
                temp = matriz[sub][sub2] + matriz[sub+1][sub2]
                update_label(matriz2[sub][sub2],temp)
                
                return arriba(matriz,sub+1,sub2)
            else:
                return arriba(matriz,sub+1,sub2)
        else:
            return matriz




    def new_number(event):
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)


        if (espacios_vacios(matriz_main) ==[]):
            Juego.destroy()
            root.deiconify()

        else:
            #Posiciones de la matriz
            #a = random.randint(0,3)
            #b = random.randint(0,3)

        
            #Lamado a la funcion update_label para cambiar la pantalla del juego
            #update_label(matriz2[a][b],num)

            #matriz_main[a][b] = num

            #arriba(matriz_main,0,0)

            fill_screen(matriz_main)
            print(espacios_vacios(matriz_main))
            

        


        
    Juego.bind("<Up>",new_number)
    

#Funcion y boton para volver al menu principal
    def volver_menu():         
        Juego.destroy()
        root.deiconify()

    Volver = Button(C_juego,text = "Volver",font =("Arial",15),width=10,command=volver_menu,bg="red",fg="white",relief='groove',borderwidth=5)
    Volver.place(x=10,y=30)

    Empezar = Button(C_juego,text = "Empezar",font =("Arial",15),width=10,command=empezar_juego,bg="red",fg="white",relief='groove',borderwidth=5)
    Empezar.place(x=10,y=80)

#Boton de play
botonJuego = Button(C_root,text="Play",font=('Arial',15),width=5,command=ventana_juego,relief="sunken",borderwidth=5,bg="red")
botonJuego.place(x=420,y=300)

root.mainloop



















    
