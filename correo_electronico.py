correo=input("Ingrese un correo: ")

while True:
    if correo.count("@")!=1 or correo.find("@")==0 or correo.find("@")==len(correo)-1:
        correo=input("Ingres un correo: ")
    else:
        print("Correo aceptado")
        break