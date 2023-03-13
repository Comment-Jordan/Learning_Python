import tkinter
from tkinter import font
from turtle import bgcolor, color
from tkinter.font import Font

class main(object):
    def __init__(self, cadena,mayu,minu,total):
        self.cadena=cadena
        self.mayu=mayu
        self.minu=minu
        self.total=total

    def ingreso_cadena(self):
        self.cadena=input("Ingrese cadena: ")
        print("Cadena original: "+ self.cadena)
    
    def mayus(self):
        #self.cadena=self.cadena.upper()
        print("Cadena en mayúsculas:\n"+ self.cadena.upper())
        self.mayus=self.cadena.upper()
        return self.mayus
        
    
    def minus(self):
        #self.cadena=self.cadena.lower()
        print("Cadena en minusulas:\n"+self.cadena.lower())
        self.minus=self.cadena.lower()
        return self.minus
        

    def conta(self):
        print("La longitud de la cadena es de "+str(len(self.cadena))+ " caracteres")
        self.total=str(len(self.cadena))
        return self.total
        


class ventana(main):
    def __init__(self):
        self.root=tkinter.Tk()
        self.label_resultado=""
        #self.cadena=""


    def ventana(self):
        
        def get_val():
           
            #name_entry = tkinter.Entry(self.root,fg="black", bg="white", width=15)
            
            cadena = name_entry.get()#Obtengo el valor del formulario
            mayus=""
            minus=""
            total=""

            nuevo_objeto=main(cadena,mayus,minus,total)
            

            may=nuevo_objeto.mayus()
            min=nuevo_objeto.minus()             
            tot=nuevo_objeto.conta()
            
            operacion= "\n","Mayúsculas: ",may,"\n","Minusculas: ",min,"\n","Longitud: ",tot
            
            imprimir="".join(operacion)
            print(imprimir)
            
            fuente = Font(family="Arial CYR", size=10) 
            
        
            if(self.label_resultado!=""):
                self.label_resultado.destroy()
                if (int(tot)>=20):
                    nueva_x=tot*12
                    self.root.geometry("{}x140".format(nueva_x)) #Aplico los 12px por carac.
                self.label_resultado=tkinter.Label(text=imprimir, bg="sky blue", font=fuente)            
                self.label_resultado.grid(row=3, column=0,columnspan=2)
            else:
                self.label_resultado=tkinter.Label(text=imprimir, bg="sky blue", font= fuente)            
                self.label_resultado.grid(row=3, column=0,columnspan=2)


        def limpiar():                     
            try:
                self.label_resultado.destroy()
                name_entry.delete(0,"end")
                self.root.geometry("240x140")
                #self.label_resultado.grid(row=3,column=0,columnspan=2)
            except:
                self.label_resultado=tkinter.Label(text="")            
                self.label_resultado.grid(row=3, column=0,columnspan=2)
                self.label_resultado.destroy()
                self.root.geometry("240x140")
                print("Hola, llegué aquí")
                pass
                #Esto es por si intentar borrar el textbox(Entry) y el mismo está vacio
            
        '''SVBar = tkinter.Scrollbar(self.root)
        SVBar.pack (side = tkinter.RIGHT,fill = "y")        
        TBox = tkinter.Text(self.root,
               height = 500,
               width = 500,
               yscrollcommand = SVBar.set,
               wrap = "none")
        SVBar.config(command = TBox.xview)'''


        self.root.geometry("240x140")
        self.root.resizable(width=True, height=False)
        self.root.configure(bg="sky blue")
        self.root.title("Caracteres.py")
        self.root.iconbitmap('C:\\Users\\Jordan\\Documents\\Practicas\\Python\\Contador_caracteres\\icono.ico')#Aqui cambio el icono de la ventana
                        
        fuente = Font(family="Arial CYR", size=10)

        label=tkinter.Label(text="Ingrese cadeana:", bg="sky blue",font=fuente)                

        #entry = tkinter.Entry(self.root,fg="black", bg="white", width=15)
        name_entry = tkinter.Entry(self.root,fg="black", bg="white", width=15)#Creo el formulario
        
        boton=tkinter.Button(self.root,text="Enviar", command=get_val,width=8,height=1, bg="dodger blue", fg="azure")
        boton_limpiar=tkinter.Button(self.root,text="Limpiar", command=limpiar,width=8,height=1, bg="dodger blue", fg="azure")
                      
        #iniciador=main(self.cadena)  

        label.grid(row=0,column=0)                                    
        name_entry.grid(row=0,column=1)
        
        boton.grid(row=2,column=0)
        boton_limpiar.grid(row=2,column=1)

        self.root.mainloop()

mostrar_ventana=ventana()
mostrar_ventana.ventana()