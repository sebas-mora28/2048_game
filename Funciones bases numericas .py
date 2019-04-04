
#Funcion que convierte de decimales a binario

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


#Funcion que convierte de decimal a octal

def octal(X):
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


#Funcion que convierte a decimal a hexadecimal



def hexa(X):
    if (X//16 < 10):
        if (X%16==10):
            return "A" + hexa(X//10)
        if (X%16==11):
            return "B" + hexa(X//10)
        if (X%16==12):
            return "C" + hexa(X//10)
        if (X%16==13):
            return "D" + hexa(X//10)
        if (X%16==14):
            return "E" + hexa(X//10)
        if (X%16==15):
            return "F" + hexa(X//10)
    else:
        return 

        
        






















    



    
