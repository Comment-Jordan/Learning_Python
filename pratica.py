from typing import Callable


def suma(*parametros):
    total=0
    for numero in parametros:
        total+=numero
    print (total)

def main_suma():
    lista=[]
    while True:    
        numero=input("Ingrese números: ")
        if numero=='=':        
            suma(*lista)
            break
        elif numero!='=':                
            lista.append(int(numero))
            print(lista)        


def otra():
    return "Otra función"

def funcion():
    return "Hola mundo"        

def llamada_de_retorno(func=""):
    return globals()[func]()


#De manera global
#print (llamada_de_retorno("funcion"))
#De manera local
#nombre_de_funcion="funcion"
#print(locals()[nombre_de_funcion]())
""" ----------------No encunetro diferencia alguna, ni mucho menos utilidad---------------- """
def nombre_funcion(nombre):
    return "Hola "+ nombre

def llamada_de_retorno(func=""):    
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]("Yo")
    else:
        return"No se encontro función"

print (llamada_de_retorno("nombre_funcion"))
