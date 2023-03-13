class Zapato(object):
    medida=0
    tamanio="Esta es la clase Zapato, instanciada en la clase persona"
    def saludo1(self):    
        print("Media es: ")   
class Pie(object):
    medida="Esta es la clase pie instanciada en la clase Persona"
    def met_pie(self):
        return "Hola es la clase Pie"
class Persona(Zapato):
    """ pies=Pie()
    nike=Zapato()
    print(nike.tamanio)
    print(pies.medida) """

    nuevo_pie=Pie()
    #print(nuevo_pie.met_pie())

    def met_persona(self):
        pass



class Transporte(object):
    num_ruedas=0
    placas="00000"
    color="Sin color aún"
    estado=False

    def arrancar(self, estado):
        if estado==True:
            return "El auto esta arrancando......."
        else:
            return "El auto esta apagado, no puede arrancar"            
        
    
    def estado_auto(self, estado):
        if estado==True:
            return "El auto esta encendido"    
        else:
            return "El auto esta apagado"      
        

class Coche(Transporte):
    tsuru=Transporte()
    
    tsuru.num_ruedas=4
    #Imprimo los valores predeterminados en la clase Transporte
    print(tsuru.placas)
    #Cambio los valores del objeto tsuru
    tsuru.placas="A-113"
    #Imprimo el nuevo valor de las nuevas placas de tsuru
    print(tsuru.placas)
    #Imprimo el valor predeterminado de color de nuestro objeto tsuru
    print(tsuru.color)
    #Asigno un nuevo valor del ya establecido en la clase Trasnporte
    tsuru.estado=True
    #Almaceno el valor del estado de mi objeto en una nueva variable
    argumento=tsuru.estado
    print(tsuru.arrancar(argumento))