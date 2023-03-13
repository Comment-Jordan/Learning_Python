with open(r"C:\Users\Jordan\Documents\Practicas\Python\texto practica_file.txt","r+") as archivo:
        
    una_mueva_cadena="Esta es  otra aún menos nueva cadena!"
    archivo.write(una_mueva_cadena)
    print(archivo.tell())
    archivo.seek(0)
    print(archivo.read())
 
with open(r"C:\Users\Jordan\Documents\Practicas\Python\texto practica_file.txt","r+") as archivo:
            
    print(archivo.read())