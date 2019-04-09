

matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]


def combinar_arriba(matriz):
    return combinar_aux(matriz,3,0,1)

def combinar_aux(matriz,sub,sub2,con):
    if (con !=3):
        if (sub != 0):
            if (matriz[sub-1][sub2]==0):
                matriz[sub][sub2] += matriz[sub-1][sub2]
                matriz[sub][sub2] = 0
                return combinar_aux(matriz,sub-1,sub2,con)

            if (matriz[sub][sub2] == matriz[sub-1][sub2]):
                matriz[sub][sub2] += matriz[sub-1][sub2]
                matriz[sub-1][sub2] = 0
                return combinar_aux(matriz,sub-1,sub2,con)#Un nuevo cuadro con la suma de los dos
            else:
                return combinar_aux(matriz,sub-1,sub2,con)
        else:
            return combinar_aux(matriz,3,0,con+1)
    else:
        return matriz #acomodar(matriz,3,0,1)







        
    


