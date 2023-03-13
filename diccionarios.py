""" direct=["valor1", "valor2", "valor3"]
relleno=[1,2]

diccionario=dict.fromkeys(direct, relleno) 
print(diccionario) """


""" diccionario1={"valor1":1, "valor2":2}
clave=diccionario1.setdefault("valor3", 3)
print(clave)
print(diccionario1) """

diccionario={"color":"rosa", "talla":"grande"}
""" print(diccionario)
print(diccionario.get("color"))
print(diccionario.get("edad", "no hay edad"))

print("No hay",diccionario.__contains__("color"), "en el diccionario")
 """


""" for clave, valor in diccionario.items():
    print("La clave es {}, con valor {}".format(clave, valor)) """

print(diccionario.keys())    
print(diccionario.values())
print("La longitud de pares del diccionario es:",len(diccionario))