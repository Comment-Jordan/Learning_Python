class Alimento():
    def __init__(self, categoria, color):
        self.categoria=categoria
        self.color=color
        self.comido=False
        self.vendido=True

    def comer(self):
        self.comido=True        

    def vender(self):
        self.vendido=True

    def estado(self):
        print("Categoria:",self.categoria,"\nColor:", self.color, "\nComido:",self.comido,"\nVendido:", self.vendido)

manzana=Alimento("Fruta", "Rojo")

#manzana.categoria="Fruta"
manzana.color="Amarillo"

manzana.comer()
manzana.estado()

print("----------")

class Platillo(Alimento):
    def vender(self):
        print("No se puede vender\n")
        self.vendido=False

sopa=Platillo("Entrada","Amarillo y verde")

#sopa.categoria="Es sopa"
#sopa.color="Tiene muchos colores"
sopa.comido=True
sopa.vender()
sopa.estado()