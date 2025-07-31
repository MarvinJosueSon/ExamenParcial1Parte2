def contarLetras(cadena,letra):
    if cadena=="":
        return 0
    if letra==cadena[0]:
        return 1 + contarLetras(cadena[1:],letra)
    else:
        return contarLetras(cadena[1:],letra)
#print(contarLetras("abracadabra","a"))
def contarDigitos(numero):
    if numero==0:
        return 0
    elif numero<10:
        return 1 + contarDigitos(numero//10)
    else:
        return 1 + contarDigitos(numero//10)
#print(contarDigitos(1234567))

def cadenaRepetida(cadena,veces,i=0,nuevaCadena=""):
    if veces==i:
        return nuevaCadena
    else:
        nuevaCadena=nuevaCadena+cadena
        return cadenaRepetida(cadena,veces,i+1,nuevaCadena)
#print(cadenaRepetida("Hola",5))


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

#print(Binario(125))



def MCD(a,b,i=1,m=1):
    if i>a or i>b:
        return m
    if a%i==0 and b%i==0:
        m=i
    return MCD(a,b,i+1,m)
while True:
    print("==MENU==")
    print("1. Calcular MCD")
    print("2. Crear Cadena repetida N veces")
    print("3. Contar letra en una cadena")
    print("4. Decimal a Binario")
    print("5. Contar Digitos")
    print("6. Salir")
    opcion=input("Ingrese la opcion: ")
    match opcion:
        case "1":
            numero1=int(input("Ingrese numero 1: "))
            numero2=int(input("Ingrese numero 2: "))
            print(f"el MCD de {numero1} y {numero2} es {MCD(numero1,numero2)}")
        case "2":
            cadenaAux=input("Ingrese la cadena : ")
            vecesAux=int(input("Ingrese las veces a repetir: "))
            print(f"La nueva cadena es: {cadenaRepetida(cadenaAux,vecesAux)}")
        case "3":
            cadenaAux=input("Ingrese la cadena : ")
            letraAux=input("Ingrese la letra para contar su cantidad: ")
            print(f"La letra '{letraAux}' aparece {contarLetras(cadenaAux,letraAux)} veces")
        case "4":
            numeroAux=int(input("Ingrese la numero para convertir en binario: "))
            print(f"{numeroAux} En binario es {Binario(numeroAux)}")
        case "5":
            numeroAux=int(input("Ingrese la numero para saber su cantidad de digitos: "))
            print(f"El numero {numeroAux} tiene {contarDigitos(numeroAux)} digitos")
        case "6":
            print("Saliendo...")
        case _:
            print("Opcion no encontrada")