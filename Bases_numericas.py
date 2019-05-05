

"""Binario"""

#Convierte de decimal
def dec_bin(X):
    if (X==0):
        return 0
    else:
        return dec_bin_aux(X,0)

def dec_bin_aux(X,exp):
    if (X==0):
        return 0
    else:
        return dec_bin_aux(X//2,exp+1) + (X%2)*10**exp


"""Octal"""
#Funcion que convierte de decimal a octal

def octal_conv(X):
    if (X==0):
        return 0
    else:
        return octal_aux(X,0)
    
def octal_aux(X,exp):
    if (X==0):
        return 0
    else:
        return (X%8)*10**exp + octal_aux(X//8,exp+1)


"""Hexadecimal"""
#Funcion que convierte de decimal a hexadecimal


def hexa(X):
    if (X%16 >= 10):
        if (X%16==10):
            return  hexa(X//16)+ "a"
        if (X%16==11):
            return hexa(X//16) + "b"
        if (X%16==12):
            return hexa(X//16) + "c"
        if (X%16==13):
            return hexa(X//16) + "d"
        if (X%16==14):
            return hexa(X//16) + "e"
        if (X%16==15):
            return hexa(X//16) +"f" 
    elif (X < 9):
        if (X==0):
            return ""
        else:
            return str(X)
    else:
        return hexa(X//16) + str(X%16)






        



    
    
