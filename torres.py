
def niveles():
    numero=int(input("Ingrese número de torres: "))    
        
    if numero==1:
        print("0")

    elif numero>1:
        cadena=""        
        for i in range(int(numero)-1):
            cadena+=" "
        cadena+="0"
        print(cadena)    
        for j in range(int(numero)-1):
            
            lista=list(cadena)
            lista[0]=""
            cadena="".join(lista)
            cadena+="00"
            print(cadena)

niveles()            