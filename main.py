def contarLetras(cadena,letra):
    if cadena=="":
        return 0
    if letra==cadena[0]:
        return 1 + contarLetras(cadena[1:],letra)
    else:
        return contarLetras(cadena[1:],letra)
print(contarLetras("abracadabra","a"))
def contarDigitos(numero):
    if numero==0:
        return 0
    elif numero<10:
        return 1 + contarDigitos(numero//10)
    else:
        return 1 + contarDigitos(numero//10)
print(contarDigitos(1234567))

def cadenaRepetida(cadena,veces,i=0):
    if veces==i:
        return ""
    else:
        print(f"{cadena}")
        return cadenaRepetida(cadena,veces,i+1)
cadenaRepetida("Hola",5)


"""
while numero>1:
    binario=str(numero%2)+binario
    numero=numero//2
print(binario)
"""

def Binario(numero,nuevoNumero=""):
    if numero==0:
        return nuevoNumero
    else:
        nuevoNumero=str(numero%2)+nuevoNumero
        return Binario(numero//2,nuevoNumero)

print(Binario(125))

def mcd(a,b):
    if a%b==0:
        return a
    else:
        return mcd(b,b//a)

def MCD(a,b,i=1,m=1):
    if i>a or i>b:
        return m
    if a%i==0 and b%i==0:
        m=i
    return MCD(a,b,i+1,m)
while True:
    print("==MENU==")
    print("1. Calcular MCD")


