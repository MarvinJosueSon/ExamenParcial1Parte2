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


