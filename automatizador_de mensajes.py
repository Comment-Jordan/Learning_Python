from os import truncate
import time
import tkinter
from tkinter import filedialog
import webbrowser
from typing import Text
import pyautogui as auto

def mensaje(contacto, mensaje):    
    webbrowser.open("https://web.whatsapp.com/send?phone={contacto}&text={mensaje}")
    time.sleep(8)
    auto.press('enter')
    #auto.hotkey('ctrl', 'f4')
    #auto.press('enter')


def enviador_manual():
    numero=input("Ingrese un número: ")
    mensa= input("Ingrese un mensaje: ")
    mensaje(numero, mensa)

def enviador_txt(mi_ruta, contacto):
    with open(mi_ruta, "r") as archivo:
        for linea in archivo:
            mensaje= linea
            webbrowser.open(f"https://web.whatsapp.com/send?phone={contacto}&text={mensaje}")
            time.sleep(8)    
            auto.press('enter')
            #auto.hotkey('ctrl', 'f4')
            #auto.press('enter')

def selecciona_ruta():
    #Abre el explorador de archivos
    raiz= tkinter.Tk()    
    raiz.title("Explorador de Archivos") #Ventana padre
    raiz.iconify() #Minimizo la ventana para asi ocultarla    

    #Guarda la ruta    
    ruta=filedialog.askopenfilename()  #Ventana hija
    raiz.destroy()
    return ruta

def abro_archivo(ruta):
    mensaje=[]
    with open (ruta, 'r') as archivo:
        for linea in archivo:
            mensaje.append(linea)
    print (mensaje)
    return mensaje            

def main():
    #1Amor      1:'+5212229223713',
    #Hermano

    dic_contactos={2: '+5212228074578'}

    while True:
        opcion=int(input("1.- Amor\n2.- Hermano\n3.- Salir\nEliga un contacto: "))
        
        
        if opcion==2:                        
            
            contacto=dic_contactos.get(opcion)        
            ruta=selecciona_ruta()            
            archivo=abro_archivo(ruta)
            mensaje(contacto, archivo)
            

            #enviador_txt(ruta, contac)            
                    
        elif opcion==3:
            break
        else:
            print("Seleccione una opción disponible")            

#selecciona_ruta()
#main()        
#enviador()
#enviador_manual()
#ruta=selecciona_ruta()
#abro_archivo(ruta)
main()