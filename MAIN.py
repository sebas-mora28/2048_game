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
                    

    cuadro2 = cargarImg("cuadro2.gif")


    def imagen(a,b):
        #C_juego.create_image(130,7, image=cuadro2, tags=("Canvas", "cuadro2"))
        fondoImg=cargarImg('cuadro2.gif')
        Cuadro=Label(F_juego, image = fondoImg,bg='light yellow')
        Cuadro.place(x=a,y=b)
        Cuadro.photo = fondoImg
        Cuadro.lower()



    cuadro1 = [5,7]
    cuadro2 = [130,7]
    cuadro3 = [255,7]
    cuadro4 = [380,7]
    cuadro5 = [5,130]
    cuadro6 = [130,130]
    cuadro7 = [255,130]
    cuadro8 = [380,130]
    cuadro9 = [5,255]
    cuadro10 = [130,255]
    cuadro11= [255,255]
    cuadro12 = [380,255]
    cuadro13 = [5,380]
    cuadro14 = [130,380]
    cuadro15= [255,380]
    cuadro16= [380,380]

    cuadro =[cuadro1,cuadro2,cuadro3,cuadro4,cuadro5,
             cuadro6,cuadro7,cuadro8,cuadro9,cuadro10,cuadro11,
             cuadro12,cuadro13,cuadro14,cuadro15,cuadro16]


    def mover(event):
        

        i = random.randint(0,15)
        b = random.randint(0,1)

        #prueba = [Prueba2,Prueba4]
        

        a = cuadro[i]
        print("xd") 
    
        #prueba[b].place(x=a[0],y=a[1])
        imagen(a[0],a[1])
        

    Juego.bind("<Up>",mover)
    




#Funcion y boton para volver al menu principal
    def volver_menu():         
        Juego.destroy()
        root.deiconify()

    Volver = Button(C_juego,text = "Volver",font =("Arial",15),width=10,command=volver_menu,bg="red",fg="white")
    Volver.place(x=10,y=30)





#Boton de play
botonJuego = Button(C_root,text="Play",font=('Arial',15),width=5,command=ventana_juego)
botonJuego.place(x=420,y=300)






root.mainloop




















    
