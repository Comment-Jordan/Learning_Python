#Ejercicio 1
def ejercicio_1():    
    nombre=input("Ingrese nombre: ")
    if len(nombre)<6:
        print("El nombre deusuario debe contener al menos 6 caracteres")
    if len(nombre)>12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    if nombre.isalnum()==False:
        print("El nombre de usuario puede contener solo letras y números")
    if (len(nombre)>=6)==True and (len(nombre)<=12)==True and nombre.isalnum()==True:
        return True
    else:
        print("Usuario no aprobado")
        return False

#Ejercicio 2
def ejercicio_2():
    contraseña=input("Ingrese contraseña: ")

    """ if len(contraseña)<8:
        print("Contraseña con menos de 8 caractéres")

    if contraseña.isupper()==True or contraseña.islower()==True or contraseña.isalpha()==True or contraseña.isalnum()==True :
        print("La contraseña no cumple con los requisitos")        

    if contraseña.count(" ")>=1:
        print("La contraseña no puede contener espacios en blanco") """

    if contraseña.isupper()==False and contraseña.islower()==False and contraseña.isalnum()==False and contraseña.isalpha()==False and contraseña.count(" ")<1:
        return True
    else:
        print("La contraseña elegida no es segura")
        return False



def ejercicio_3():
    usuario=ejercicio_1()
    contraseña=ejercicio_2()
    if usuario==True and contraseña==True:
        print("Usuario y contraseña aprobados")
    else:
        print("Usuario o contraseña no aprobados")        

ejercicio_3()