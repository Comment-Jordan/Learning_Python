
def mi_funcion(x):        
    estado=False        
    contando=len(x)              
    sub_contando=1    
    i=0
    j=-1

    while True:
        if contando==sub_contando: 
            break
        elif x[i]==x[j]:
            estado=True
        elif x[i]!=x[j]:
            estado= False
            break
        i+=1   
        j-=1
        sub_contando+=1
    return estado

x= input("Ingresa una palabra: ")
print(mi_funcion(x))