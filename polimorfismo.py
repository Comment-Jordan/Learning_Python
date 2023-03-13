class Yate():
    
    def desplazamiento(self):
        print("Se desplaza sin ruedas")


class Moto():

    def desplazamiento(self):
        print("Se desplaza con dos ruedas")

class Auto():

    def desplazamiento(self):
        print("Se desplaza con 4 ruedas")


def diferentes_desplazamientos(vehiculo):
    vehiculo.desplazamiento()


mi_trasnporte= Moto()
#mi_trasnporte.desplazamiento()
diferentes_desplazamientos(mi_trasnporte)