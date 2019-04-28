

""" multiplicacion de las 3"""

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

#Funcion que convierte de binario a decimales

def bin_dec(X):
    if (X==0):
        return 0
    else:
        return bin_dec_aux(X,0)

def bin_dec_aux(X,exp):
    if (X==0):
        return 0
    else:
        return (X%10)*2**exp + bin_dec_aux(X//10,exp+1)


#Suma de binarios

def suma_bina(X,Y):
    if (X >= Y):
        return suma_bina_aux(X,Y,0,0)
    else:
        return suma_bina_aux(Y,X,0,0)


def suma_bina_aux(X,Y,carry,exp):
        if (X== 0):
            return X*10**exp + carry*10**(exp)
        elif (X%10+Y%10+carry==2):
            a = 1
            return 0*10**exp + suma_bina_aux(X//10,Y//10,a,exp+1)
        elif ((X%10+Y%10+carry==3)):
            a=1
            return 1*10**exp + suma_bina_aux(X//10,Y//10,a,exp+1)
        else:
            if (carry==1):
                return (((X%10)%2+(Y%10)%2)+carry)*10**exp + suma_bina_aux(X//10,Y//10,0,exp+1)
            else:
                return (((X%10)%2+(Y%10)%2)+carry)*10**exp + suma_bina_aux(X//10,Y//10,0,exp+1)





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

#Funcion que convierte de octal a decimal

def octal_decimal(X):
    if (X==0):
        return 0
    else:
        return octal_decimal_aux(X,0)


def octal_decimal_aux(X,exp):
    if (X==0):
        return 0
    else:
        return (X%10)*8**exp + octal_decimal_aux(X//10,exp+1)



#Suma de octal
def suma_octal(X,Y):
    return suma_octal_aux(X,Y,0,0)


def suma_octal_aux(X,Y,carry,exp):
     if (Y==0):
        return carry*10**exp 
     elif (X%10 + Y%10 + carry > 7):
        conv = octal(X%10 + Y%10+ carry)
        carry = conv//10
        return  (conv%10)*10**exp + suma_octal_aux(X//10,Y//10,carry,exp+1)
     else:
        return (X%10 + Y%10+ carry)*10**exp + suma_octal_aux(X//10,Y//10,carry,exp+1)




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
        return str(X)
    else:
        return hexa(X//16) + str(X%16)


#Funcion que convierte de hexadecimal a decimal

def deci_hexa(X):
    if (X==""):
        return ""
    else:
        return deci_hexa_aux(X,0)


def deci_hexa_aux(X,exp):
    if (X == ""):
        return 0
    if (X[-1]=="a"):
        return 10*16**exp + deci_hexa_aux(X[:-1],exp+1)
    if (X[-1]=="b"):
        return 11*16**exp + deci_hexa_aux(X[:-1],exp+1)
    if (X[-1]=="c"):
        return 12*16**exp + deci_hexa_aux(X[:-1],exp+1)
    if (X[-1]=="d"):
        return 13*16**exp + deci_hexa_aux(X[:-1],exp+1)
    if (X[-1]=="e"):
        return 14*16**exp + deci_hexa_aux(X[:-1],exp+1)
    if (X[-1]=="f"):
        return 15*16**exp + deci_hexa_aux(X[:-1],exp+1)
    else:
        return int(X[-1])*16**exp + deci_hexa_aux(X[:-1],exp+1)


#Suma en hexadecimal

"""No esta completa"""
def suma_hexa(X,Y):
    return suma_hexa_aux(X,Y,0,0)


def suma_hexa_aux(X,Y,carry,exp):
     if (Y==0):
        return carry*10**exp
     elif (X%10 + Y%10 + carry > 15):
        conv = int(hexa(X%10 + Y%10+ carry))
        carry = conv//10
        return  (conv%10)*10**exp + suma_hexa_aux(X//10,Y//10,carry,exp+1)
     else:
        return (X%10 + Y%10+ carry)*10**exp + suma_hexa_aux(X//10,Y//10,carry,exp+1)







        



    
    
