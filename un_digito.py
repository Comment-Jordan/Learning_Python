def mi_metodo():
    total=0    
    numero=input("Ingrese número: ")
    try:
        while True:
            if int(numero)>=10:           
                for i in range(len(numero)):
                    total=total+int(numero[i])
                numero=total
            elif int(numero)<=0:
                print("Ingrese un número mayor a 0")
                numero=input("\nIngrese número: ")    
            elif int(numero)<10:
                print("\nEl digito es:",numero)
                break
    except:
        print("Ingrese un número")                
        mi_metodo()
mi_metodo()        