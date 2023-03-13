import sys
import random
import pygame
from pygame import time
from pygame import surface

pygame.init()

def tareas():
    num_tareas=int(input("¿Cúantas tareas se van a ejecutar?: "))
    tareas={}

    for i in range(1,num_tareas):

        tareas["Tarea "+str(i)]=int(random.randrange(1, 51))

    print(tareas)
    return tareas

#Declaro los colores que utilizare
amarillo_patito=255,255,197    
rojo_claro=242,140,116
rojo_top=188,33,28
rosa_sai=238,136,175
azul_sai=129,193,203
verde_suerte=80,99,13
verde_suerte2=11,69,10
azul_overwatch=64,82,117
azul_overwatch2=33,143,254
morado_overwatch=115,89,186
verde_hanzo=185,180,138
crema_overwatch=182,140,82
morado_widow=158,106,168
negro=0,0,0
lista_colores=[rojo_claro, rojo_top, rosa_sai, azul_sai, verde_suerte, verde_suerte2
    ,azul_overwatch, azul_overwatch2, morado_overwatch, verde_hanzo, crema_overwatch, morado_widow]

fps=60

fuente=pygame.font.Font(None, 17)
texto1=fuente.render("Tarea 1", True, negro)

def main():
    estado=True
    clock=pygame.time.Clock()    
    ancho, alto= 1065, 500
    
    pygame.display.set_caption("Multiprogramación")
    
    #Defino los valores de la ventana
    ventana= pygame.display.set_mode((ancho, alto)) #Tamaño de ventana
            
    
    def graficacion(vetana):    
        #Defino los valores de un cuadrado x,y,ancho,alto
        x,y=50,50
        x2, y2= 50,50 #x, y de las rayas          
        num_tiempos=random.randrange(1,50)
        #tamaño de cuadrado=20x20
        indice=random.randrange(len(lista_colores))
        color_random=lista_colores[indice]
        
        for i in range(num_tiempos):
            cuadrado=pygame.Rect(x,y,20,20) #Creo el cuadrado (X,Y, largo, ancho)
            
            pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
            x+=20  
        for j in range(11):
            pygame.draw.line(ventana, negro,(x2, y2),(1040, y2),1) #(x,y) de inicio, (x,y) de fin, ancho
            y2+=20
        
    def pausa():
        pause=True
        while pause:   
            if event.type==pygame.QUIT():
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    pause=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
    
    veces=0
    while estado:
        clock.tick(fps)

        #Con esto creo el evento exit, para salir de la ventana
        for event in pygame.event.get():            
            if event.type==pygame.QUIT:
                estado=False
                        
        #Asigno los valores de mi ventana
        ventana.fill(amarillo_patito)#Color de mi ventana
        #pygame.draw.rect(ventana,verde_hanzo,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)        
        if veces<1:
            graficacion(ventana)
            veces+=1        
            ventana.blit(texto1,(8,53))
            pygame.display.update() #Aquí actualizo mi ventana

main()