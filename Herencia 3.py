class Persona():

    def __init__(self, nombre, edad, lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    
    def informacion(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        print("Lugar:",self.lugar)


class Empleado(Persona):

    def __init__(self, sueldo, puesto, nombre, edad, lugar):
        super().__init__(nombre, edad, lugar)
        self.sueldo=sueldo
        self.puesto=puesto        
    
    def informacion(self):
        super().informacion()
        print("\n----------")
        print("Sueldo:",self.sueldo)
        print("Puesto:",self.puesto)        


Esmeralda=Empleado(1500, "CEO", "Esmeralda", 31, "Puebla")
Esmeralda.informacion()        

Laura=Persona("Laura", 51, "Veracruz")

print("¿La instancia Esmeralda pertenece a Empleado?:", isinstance(Esmeralda, Empleado))
print("¿La instancia Esmeralda pertenece a Persona?:", isinstance(Esmeralda, Persona))
print("¿La instancia Laura pertenece a la clase Empleado?:", isinstance(Laura, Empleado))