import string

cadena = "rr oadjsihaugfia"

def balance(cadena):
    cadena = cadena.lower()
    contador_r = cadena.count('r') 
    contador_j = cadena.count('j')
    print(contador_r)
    print(contador_j)   
    if contador_r == contador_j:
        return True
    elif contador_j != contador_r:
        return False
    elif contador_j == 0 and contador_r == 0:
        return True


print(balance(cadena))

def banlance_for(cadena):
    cadena = cadena.lower()
    contador_r = 0
    contador_j = 0
    for letra in cadena:
        if letra == 'r':
            contador_r += 1
        elif letra == 'j':
            contador_j += 1
    print(contador_r)
    print(contador_j) 
    return contador_r == contador_j

    


print(banlance_for(cadena))