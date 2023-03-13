import os
from tkinter import filedialog
import tkinter
import requests

def apagar():
    os.system('shutdown -s')

def evalua_archivo(ruta):
    if os.path.exists(ruta): #Esta linea es para saber si un archivo existe
        print (True)
    else:
        print (False)    

def selecciona_ruta():
    raiz = tkinter.Tk()
    raiz.withdraw()
    ruta = filedialog.askopenfilename()
    print("La ruta es:",ruta)
    return ruta
    
def descargando(ruta):
    #ruta='https://wallpapercave.com/wp/wp1850415.jpg'
    archivo= requests.get(ruta)
    open('D:\\una_imagen.jpg','wb').write(archivo.content)

    

#selecciona_ruta()
#evalua_archivo(selecciona_ruta())
#descargando()
#apagar()
