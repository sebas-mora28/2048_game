
"""Falta terminar ultimos casos"""




def adyacente(matriz,pos1,pos2):
    if (pos2 == 0 or pos2 == 3):
        return dayacente_lados
    else:
        return adyacente_arriba(matriz,pos1,pos2)



#             _____________________________
#____________/ Cuatro direcciones

def adyacente_arriba(matriz,pos1,pos2):
    #Arriba
    if (matriz[pos1][pos2] == matriz[pos1-1][pos2]):
        return [[True]] + adyacente_abajo(matriz,pos1,pos2)
    else:
        return [[False]] + adyacente_abajo(matriz,pos1,pos2)

def adyacente_abajo(matriz,pos1,pos2):
    #Abajo
    if (matriz[pos1][pos2] == matriz[pos1+1][pos2]):
        return [[True]] +adyacente_derecha(matriz,pos1,pos2)
    else:
        return [[False]] + adyacente_derecha(matriz,pos1,pos2)


def adyacente_derecha(matriz,pos1,pos2):
    #Derecha
    if (matriz[pos1][pos2] == matriz[pos1][pos2+1]):
        return [[True]] + adyacente_izquierda(matriz,pos1,pos2)
    else:
        return [[False]] + adyacente_izquierda(matriz,pos1,pos2)


def adyacente_izquierda(matriz,pos1,pos2):
    #Izquierda
    if (matriz[pos1][pos2] == matriz[pos1][pos2-1]):
        return [[True]] 
    else:
        return [[False]]


#            __________________________
#___________/ Esquinas

def adyacente_esquina_superior(matriz,pos1,pos2,conteo):
    if (conteo !=3):
        if (conteo ==2):
            if (matriz[pos1][pos2] == matriz[pos1][pos2+1]):
                return [[True]] + adyacente_esquina_superior(matriz,pos1+1,pos2,con+1)
            else:
                return [[False]] + adyacente_esquina_superior(matriz,pos1+1,pos2,con+1)
        else:
            if (matriz[pos1][pos2] == matriz[pos1+1][pos2]):
                return [[True]] + adyacente_esquina_superior(matriz,pos1,pos2,con+1)
            else:
                return [[False]] + adyacente_esquina_superior(matriz,pos1,pos2,con+1)
    else:
        return []


def adyacente_esquina_superior2(matriz,pos1,pos2,conteo):
    if (conteo !=3):
        if (conteo ==2):
            if (matriz[pos1][pos2] == matriz[pos1][pos2-1]):
                return [[True]] + adyacente_esquina_superior2(matriz,pos1+1,pos2,con+1)
            else:
                return [[False]] + adyacente_esquina_superior2(matriz,pos1+1,pos2,con+1)
        else:
            if (matriz[pos1][pos2] == matriz[pos1+1][pos2]):
                return [[True]] + adyacente_esquina_superior2(matriz,pos1,pos2,con+1)
            else:
                return [[False]] + adyacente_esquina_superior2(matriz,pos1,pos2,con+1)
    else:
        return []

def adyacente_esquina_inferior(matriz,pos1,pos2,conteo):
    if (conteo !=3):
        if (conteo ==2):
            if (matriz[pos1][pos2] == matriz[pos1][pos2+1]):
                return [[True]] + adyacente_esquina_inferior(matriz,pos1+1,pos2,con+1)
            else:
                return [[False]] + adyacente_esquina_inferior(matriz,pos1+1,pos2,con+1)
        else:
            if (matriz[pos1][pos2] == matriz[pos1-1][pos2]):
                return [[True]] +adyacente_esquina_inferior(matriz,pos1,pos2,con+1)
            else:
                return [[False]] + adyacente_esquina_inferior(matriz,pos1,pos2,con+1)
    else:
        return []















    

        
        
                
                                    


















    
        































###########################################################################

###########################################################################
"""Funcion espacion en blanco"""

"""
  [[2,2,0,2],
   [4,2,2,2],
   [8,2,0,2],
   [8,0,2,4]]
"""


def espacio(matriz):
    return espacio_aux(matriz,0,0)

def espacio_aux(matriz,sub,sub2):
    if (sub !=4):
        if (sub2 !=4):
            if (matriz[sub][sub2] == 0):
                return [[sub,sub2]] + espacio_aux(matriz,sub,sub2+1)
            else:
                return espacio_aux(matriz,sub,sub2+1)
        else:
            return espacio_aux(matriz,sub+1,0)
    return []
    


















                    
