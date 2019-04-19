from tkinter import *
import os
import random
from tkinter import messagebox


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
    

    #Matriz principal y puntaje 
    global matriz_main
    matriz_main =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


    #Puntaje del juego

    Score = Label(C_juego,text= "",font=('Arial',30),bg="white",width =5)
    Score.place(x=425,y=50)
                    
    def puntaje(X):
        global Puntaje
        Puntaje = 0

        score = Puntaje + X
        print(score)
        Score['text'] = str(score)
        
        


    #Funcion para actualizar la pantalla de juego 

    def update_screen(i,j):
        if (i < 4):
            if (j <4):
                if (matriz_main[i][j] == 0):
                    matriz2[i][j]['text'] = ""
                    matriz2[i][j]['bg'] = "navajo white3"
                    return update_screen(i,j+1)
                else:
                    if (matriz_main[i][j] == 4):
                        matriz2[i][j]['text'] = str(matriz_main[i][j])
                        matriz2[i][j]['bg'] = "Antique white3"
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] == 8 or matriz_main[i][j] == 16):
                        matriz2[i][j]['text'] = str(matriz_main[i][j])
                        matriz2[i][j]['bg'] = "orange"
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] == 32):
                        matriz2[i][j]['text'] = str(matriz_main[i][j])
                        matriz2[i][j]['bg'] = "dark orange"
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] == 64 ):
                        matriz2[i][j]['text'] = str(matriz_main[i][j])
                        matriz2[i][j]['bg'] = "red"
                        return update_screen(i,j+1)
                    if (matriz_main[i][j] >=128 ):
                        matriz2[i][j]['text'] = str(matriz_main[i][j])
                        matriz2[i][j]['bg'] = "yellow"
                        return update_screen(i,j+1)
                    else:
                        matriz2[i][j]['text'] = str(matriz_main[i][j])
                        matriz2[i][j]['bg'] = 'linen'
                        return update_screen(i,j+1)       
            else:
                return update_screen(i+1,0)
        else:
            return matriz_main



    #Funcion que introduce un nuevo numero en cada movimiento
    def fill_screen():
        numero_aleatorio = random.randrange(2,5,2)
        indices = espacios_vacios()
        aleatorio = random.randint(0,len(indices)-1)
        temp = indices[aleatorio]
        matriz_main[temp[0]][temp[1]] += numero_aleatorio
        

        update_screen(0,0)
        #update_screen(matriz2[temp[0]][temp[1]],numero_aleatorio)


    #Matriz donde se encuentra las cada uno de los labels de la pantalla mostrada al usuario
    matriz2= [[Cuadro1,Cuadro2,Cuadro3,Cuadro4],
             [Cuadro5,Cuadro6,Cuadro7,Cuadro8],
             [Cuadro9,Cuadro10,Cuadro11,Cuadro12],
             [Cuadro13,Cuadro14,Cuadro15,Cuadro16]]




    #Funcion espacios vacios de la matriz

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
                               
    


    #Funcion con los indices de los espacios vacios de la matriz principal 
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



    #Funcion que actualiza los espacios vacios
    """Revisar si se usa"""
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

        #Actualizar la matriz principal
        matriz_main[pos1][pos2] = 2
        matriz_main[pos3][pos4] = aleatorio1

        update_screen(0,0)
       
        

    
    #Funcion que actualiza la matriz con direccion hacia arriba
    def arriba(sub,sub2,con,tem):
        if(con<4):
            if (sub <=2):
                if (matriz_main[sub][sub2] ==0):
                    matriz_main[sub][sub2] = matriz_main[sub+1][sub2]
                    #update_screen(matriz2[sub][sub2],matriz_main[sub+1][sub2])
                    #update_screen(matriz2[sub+1][sub2],0)
                    matriz_main[sub+1][sub2] =0 
                    return arriba(sub+1,sub2,con,tem)
                if (matriz_main[sub][sub2] == matriz_main[sub+1][sub2]):
                    suma = matriz_main[sub][sub2] + matriz_main[sub+1][sub2]
                    puntaje(suma)
                    matriz_main[sub+1][sub2] += matriz_main[sub][sub2]
                    #update_screen(matriz2[sub+1][sub2],suma)
                    matriz_main[sub][sub2] = 0
                    #update_screen(matriz2[sub][sub2],0)
                    return arriba(sub+1,sub2,con,tem)
                else:
                    return arriba(sub+1,sub2,con,tem)
            else:
                return arriba(0,tem,con+1,tem)
        else:
            return matriz_main
      

    def new_number_arriba(event):
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)


        if not (opciones()):
            ask = messagebox.askyesno("Volver a jugar","Volver a jugar")
            if (ask):
                Juego.destroy()
                ventana_juego()
            else:
                volver_menu()
        else:
            arriba(0,0,0,0)
            arriba(0,1,0,1)
            arriba(0,2,0,2)
            arriba(0,3,0,3)
            
            fill_screen()
    
            update_screen(0,0)

                    
    Juego.bind("<Up>",new_number_arriba)



    #Funcion que actualiza la matriz y la pantalla con direccion hacia abajo

    def abajo(sub,sub2,con,tem):
        if(con<4):
            if (sub <=2):
                if (matriz_main[sub+1][sub2] ==0):
                    matriz_main[sub+1][sub2] = matriz_main[sub][sub2]
                    matriz_main[sub][sub2] =0 
                    return abajo(sub+1,sub2,con,tem)
                if (matriz_main[sub][sub2] == matriz_main[sub+1][sub2]):
                    suma = matriz_main[sub][sub2] + matriz_main[sub+1][sub2]
                    matriz_main[sub][sub2] += matriz_main[sub+1][sub2]
                    matriz_main[sub+1][sub2] = 0
                    return abajo(sub+1,sub2,con,tem)
                else:
                    return abajo(sub+1,sub2,con,tem)
            else:
                return abajo(0,tem,con+1,tem)
        else:
            return matriz_main


    def new_number_abajo(event):
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)


        if not (opciones()):
            ask = messagebox.askyesno("Volver a jugar","Volver a jugar")
            if (ask):
                Juego.destroy
                ventana_juego()
            else:
                volver_menu()
        else:
            
            abajo(0,0,0,0)
            abajo(0,1,0,1)
            abajo(0,2,0,2)
            abajo(0,3,0,3)

            fill_screen()
    
            update_screen(0,0)
         
                    
    Juego.bind("<Down>",new_number_abajo)


    #Funcion que actualiza la matriz y la pantalla hacia la izquierda

    def izquierda(matriz,i):
        combinar1 = combinar(matriz,i)
        rellenar1 = rellenar(combinar1,len(combinar1)-1,3)
        suma = sumar(rellenar1,0)
        combinar2 = combinar(suma,0)
        return rellenar(combinar2,len(combinar2)-1,3)
        


    def combinar(matriz,i):
        if (i != 4):
            if (matriz[i] != 0):
                return [matriz[i]] + combinar(matriz,i+1)
            else:
                return combinar(matriz,i+1)
        else:
            return []
   
    def rellenar(matriz,longitud,meta):
        if (longitud != meta):
            matriz +=[0]
            return rellenar(matriz,longitud+1,meta)
        else:
            return matriz


    def sumar(matriz,i):
        if (i<=2):
            if (matriz[i] == matriz[i+1]):
                matriz[i] += matriz[i+1]
                matriz[i+1] = 0
                return sumar(matriz,i+1)
            else:
                return sumar(matriz,i+1)
        else:
            return matriz


    
    def new_number_izquierda(event):
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)


        if not (opciones()):
            ask = messagebox.askyesno("Volver a jugar","Volver a jugar")
            if (ask):
                Juego.destroy()
                ventana_juego()
            else:
                volver_menu()
        else:
            matriz_main[0] = izquierda(matriz_main[0],0)
            matriz_main[1] = izquierda(matriz_main[1],0)
            matriz_main[2] = izquierda(matriz_main[2],0)
            matriz_main[3] = izquierda(matriz_main[3],0)


            fill_screen()

            update_screen(0,0)
            

            

    Juego.bind("<Left>",new_number_izquierda)

    #Funcion que actualiza la matriz y la pantalla con direccion hacia la derecha
    def derecha(matriz,i):
            combinar1 = combinar_right(matriz,i)
            rellenar1 = rellenar_right(combinar1,3,len(combinar1)-1)
            suma = sumar_right(rellenar1,3)
            combinar2 = combinar_right(suma,i)
            return rellenar_right(combinar2,3,len(combinar2)-1)

            


    def combinar_right(matriz,i):
            if (i >= 0):
                if (matriz[i] != 0):
                    return [matriz[i]] + combinar_right(matriz,i-1)
                else:
                    return combinar_right(matriz,i-1)
            else:
                return []
       
    def rellenar_right(matriz,longitud,meta):
            if (longitud != meta):
                matriz = [0] + matriz
                return rellenar_right(matriz,longitud-1,meta)
            else:
                return matriz


    def sumar_right(matriz,i):
            if (i>=1):
                if (matriz[i] == matriz[i-1]):
                    matriz[i] += matriz[i-1]
                    matriz[i-1] = 0
                    return sumar_right(matriz,i-1)
                else:
                    return sumar_right(matriz,i-1)
            else:
                return matriz
            

    def new_number_derecha(event):
        #Numero aleatorio entre 2 y cuatro
        num= random.randrange(2,5,2)


        if not (opciones()):
            ask = messagebox.askyesno("Volver a jugar","Volver a jugar")
            if (ask):
                Juego.destroy()
                ventana_juego()
            else:
                volver_menu()
        else:
            matriz_main[0] = derecha(matriz_main[0],3)
            matriz_main[1] = derecha(matriz_main[1],3)
            matriz_main[2] = derecha(matriz_main[2],3)
            matriz_main[3] = derecha(matriz_main[3],3)

            fill_screen()

            update_screen(0,0)
            
    Juego.bind("<Right>",new_number_derecha)


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




















    
