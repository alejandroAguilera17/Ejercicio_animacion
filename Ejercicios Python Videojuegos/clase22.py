import pygame, sys #Importando el modulo de pygame (contiene varias librerias)
from pygame.locals import* #Importamos todas las librerias del modulo pygame

pygame.init()  #Inicializa el pygame

ventana = pygame.display.set_mode((1024,600))
pygame.display.set_caption("Jueguito")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

fondo2 = pygame.image.load("bosque.png").convert()
x=0
y=0
ventana.blit(fondo2,(x,y))

ANCHO, ALTO = 1024, 600
ventana = pygame.display.set_mode((ANCHO,ALTO))
FPS = 60
RELOJ = pygame.time.Clock()



while True: #La ventana itera continuamente hasta que se cierre
    for evento in pygame.event.get():
        if evento.type == QUIT: #Si el evento es igual a salir

            pygame.quit() #Cierra mmodulo de pygame
            sys.exit() #Salir del programa o sistema


    #MOVIMIENTO DEL FONDO
    x_relativa = x % fondo2.get_rect().width

    ventana.blit(fondo2, (x_relativa - fondo2.get_rect().width, 0))
    if x_relativa < ANCHO:
        ventana.blit(fondo2, (x_relativa,0))
        x +=1

    pygame.display.update()  #Actualiza la ejecución de ventana

    #conotrol de FPS
    RELOJ.tick(FPS)